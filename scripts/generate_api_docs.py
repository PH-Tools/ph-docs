"""Generate API reference markdown from Python source files.

Reads libraries.yml for autodoc configuration, parses Python 2.7-compatible
source files using ast, and writes markdown into src/content/docs/{lib}/api/.

Runs between fetch_spokes.py and pnpm build. Always exits 0 — generation
failures are logged, not fatal.

Usage:
    python scripts/generate_api_docs.py
    python scripts/generate_api_docs.py --library honeybee-ph
    python scripts/generate_api_docs.py --verbose
    python scripts/generate_api_docs.py --dry-run
"""

from __future__ import annotations

import argparse
import ast
import fnmatch
import os
import re
import sys
import textwrap
from dataclasses import dataclass, field
from pathlib import Path

import yaml

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent
LIBRARIES_YML = ROOT / "libraries.yml"
CONTENT_DIR = ROOT / "src" / "content" / "docs"
CACHE_DIR = ROOT / ".cache" / "spokes"

# ---------------------------------------------------------------------------
# Regex patterns for # type: comments
# ---------------------------------------------------------------------------

# Method/property type comment: # type: (ArgType, ...) -> ReturnType
METHOD_TYPE_RE = re.compile(r"#\s*type:\s*\(([^)]*)\)\s*->\s*(.+)")

# Inline attribute type comment: self.x = value  # type: SomeType
INLINE_TYPE_RE = re.compile(r"#\s*type:\s*(.+)")

# ---------------------------------------------------------------------------
# Default autodoc config
# ---------------------------------------------------------------------------

DEFAULT_AUTODOC = {
    "enabled": True,
    "exclude_modules": [],
    "exclude_patterns": ["_*", "test_*"],
    "include_patterns": ["_base.py"],
    "skip_methods": [
        "to_dict", "from_dict", "duplicate", "__copy__",
        "__str__", "__repr__", "__hash__", "ToString",
    ],
    "output_dir": "api",
}


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class ArgInfo:
    name: str
    type_str: str = ""
    description: str = ""


@dataclass
class AttributeInfo:
    name: str
    type_str: str = ""
    description: str = ""


@dataclass
class PropertyInfo:
    name: str
    return_type: str = ""
    docstring: str = ""


@dataclass
class MethodInfo:
    name: str
    args: list[ArgInfo] = field(default_factory=list)
    return_type: str = ""
    docstring: str = ""
    is_classmethod: bool = False
    is_staticmethod: bool = False


@dataclass
class ClassInfo:
    name: str
    module_path: str = ""
    bases: list[str] = field(default_factory=list)
    docstring: str = ""
    attributes: list[AttributeInfo] = field(default_factory=list)
    properties: list[PropertyInfo] = field(default_factory=list)
    methods: list[MethodInfo] = field(default_factory=list)
    is_enum: bool = False
    enum_values: list[tuple[str, str]] = field(default_factory=list)


@dataclass
class ModuleInfo:
    name: str
    source_path: str = ""
    docstring: str = ""
    classes: list[ClassInfo] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Type comment parsing
# ---------------------------------------------------------------------------

def parse_method_type_comment(source_lines: list[str], func_node: ast.FunctionDef) -> tuple[list[str], str]:
    """Extract arg types and return type from a # type: comment after def line.

    Returns (arg_types, return_type). arg_types excludes self/cls.
    """
    # The type comment is on the first line inside the function body.
    # It appears *after* the def line, at func_node.body[0].lineno or
    # between the def line end and the first statement.
    # We scan the lines between the end of the def signature and the
    # first body statement for a # type: comment.
    body_start = func_node.body[0].lineno if func_node.body else func_node.lineno + 1
    # Scan from the line after def up to (and including) the first body line
    for lineno in range(func_node.lineno, min(body_start + 1, len(source_lines) + 1)):
        line = source_lines[lineno - 1] if lineno <= len(source_lines) else ""
        m = METHOD_TYPE_RE.search(line)
        if m:
            raw_args = m.group(1).strip()
            raw_return = m.group(2).strip()
            arg_types = [a.strip() for a in raw_args.split(",")] if raw_args else []
            return arg_types, raw_return

    return [], ""


def parse_inline_type_comment(line: str) -> str:
    """Extract type from an inline # type: comment on an assignment line."""
    m = INLINE_TYPE_RE.search(line)
    if m:
        return m.group(1).strip()
    return ""


def infer_type_from_value(node: ast.expr) -> str:
    """Infer a type string from a literal assignment value."""
    if isinstance(node, ast.Constant):
        v = node.value
        if v is None:
            return "Optional[unknown]"
        if isinstance(v, bool):
            return "bool"
        if isinstance(v, int):
            return "int"
        if isinstance(v, float):
            return "float"
        if isinstance(v, str):
            return "str"
    if isinstance(node, ast.List):
        return "List"
    if isinstance(node, ast.Dict):
        return "Dict"
    if isinstance(node, ast.Call):
        if isinstance(node.func, ast.Name):
            return node.func.id
        if isinstance(node.func, ast.Attribute):
            return node.func.attr
    return ""


# ---------------------------------------------------------------------------
# Docstring parsing
# ---------------------------------------------------------------------------

def parse_docstring_section(docstring: str, section_name: str) -> dict[str, str]:
    """Extract entries from a named docstring section.

    Handles Google-style sections like:
        Attributes:
            name (Type): Description that may
                continue on the next line.

    Also handles the honeybee-ph style with dashes and bullets:
        Arguments:
        ----------
            * name (Type): Description.

    Returns a dict mapping entry names to their descriptions.
    """
    if not docstring:
        return {}

    lines = docstring.split("\n")
    result: dict[str, str] = {}

    # Find the section header line
    section_idx = -1
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.lower().startswith(section_name.lower()) and stripped.endswith(":"):
            section_idx = i
            break

    if section_idx < 0:
        return result

    # Parse entries below the section header.
    # Key insight: entry lines have a base indentation, continuation lines
    # are indented further. We detect the base indent from the first entry.
    current_name = ""
    current_desc = ""
    base_indent: int | None = None
    entry_re = re.compile(
        r"^\s*(?:\*\s+)?"          # optional bullet
        r"(\w+)"                    # name
        r"(?:\s*\([^)]*\))?"       # optional (Type)
        r"\s*:\s*"                  # colon separator
        r"(.*)"                     # description
    )

    for line in lines[section_idx + 1:]:
        stripped = line.strip()
        indent = len(line) - len(line.lstrip())

        # Stop at next section header, blank line after content, or end
        if stripped and stripped.endswith(":") and not stripped.startswith("*") and not stripped.startswith("-"):
            if re.match(r"^[A-Z]\w+:$", stripped) and (base_indent is None or indent <= base_indent):
                break

        # Skip separator lines (----------)
        if stripped and all(c == "-" for c in stripped):
            continue

        # Skip blank lines at the start
        if not stripped and not current_name:
            continue

        # If blank line after we've been collecting entries, stop
        if not stripped and current_name:
            result[current_name] = current_desc.strip()
            break

        # Determine if this is a new entry or a continuation line.
        # A continuation line is indented deeper than the base entry indent.
        is_continuation = base_indent is not None and indent > base_indent
        m = entry_re.match(stripped)

        if m and not is_continuation:
            # Save previous entry
            if current_name:
                result[current_name] = current_desc.strip()
            current_name = m.group(1)
            current_desc = m.group(2)
            if base_indent is None:
                base_indent = indent
        elif current_name:
            # Continuation line
            current_desc += " " + stripped

    # Save last entry
    if current_name:
        result[current_name] = current_desc.strip()

    return result


def parse_enum_values_section(docstring: str) -> dict[str, str]:
    """Extract enum values from a 'Values:' docstring section.

    Format: value: Description
    """
    if not docstring:
        return {}

    lines = docstring.split("\n")
    result: dict[str, str] = {}

    section_idx = -1
    for i, line in enumerate(lines):
        if line.strip().lower().startswith("values") and line.strip().endswith(":"):
            section_idx = i
            break

    if section_idx < 0:
        return result

    value_re = re.compile(r"^\s*(\S+)\s*:\s*(.*)")

    for line in lines[section_idx + 1:]:
        stripped = line.strip()
        if not stripped:
            break
        if stripped.endswith(":") and re.match(r"^[A-Z]\w+:$", stripped):
            break
        m = value_re.match(stripped)
        if m:
            result[m.group(1)] = m.group(2).strip()

    return result


def get_first_line(docstring: str) -> str:
    """Return the first non-empty line of a docstring."""
    if not docstring:
        return ""
    for line in docstring.strip().split("\n"):
        stripped = line.strip()
        if stripped:
            return stripped
    return ""


# ---------------------------------------------------------------------------
# AST extraction
# ---------------------------------------------------------------------------

def has_decorator(node: ast.FunctionDef, name: str) -> bool:
    """Check if a function/method has a specific decorator."""
    for dec in node.decorator_list:
        if isinstance(dec, ast.Name) and dec.id == name:
            return True
        if isinstance(dec, ast.Attribute) and dec.attr == name:
            return True
    return False


def extract_base_names(class_node: ast.ClassDef) -> list[str]:
    """Extract base class names from a ClassDef node."""
    bases = []
    for base in class_node.bases:
        if isinstance(base, ast.Name):
            bases.append(base.id)
        elif isinstance(base, ast.Attribute):
            # e.g. _base._Base → "_base._Base"
            parts = []
            node = base
            while isinstance(node, ast.Attribute):
                parts.append(node.attr)
                node = node.value
            if isinstance(node, ast.Name):
                parts.append(node.id)
            bases.append(".".join(reversed(parts)))
    return bases


def is_enum_class(class_node: ast.ClassDef) -> bool:
    """Detect if a class is an enum (inherits from CustomEnum or has 'allowed' list)."""
    base_names = extract_base_names(class_node)
    for name in base_names:
        if "CustomEnum" in name or "Enum" in name.split(".")[-1]:
            return True
    # Also check for an 'allowed' class attribute
    for item in class_node.body:
        if isinstance(item, ast.Assign):
            for target in item.targets:
                if isinstance(target, ast.Name) and target.id == "allowed":
                    return True
    return False


def extract_enum_values(class_node: ast.ClassDef) -> list[str]:
    """Extract the 'allowed' list values from an enum class."""
    for item in class_node.body:
        if isinstance(item, ast.Assign):
            for target in item.targets:
                if isinstance(target, ast.Name) and target.id == "allowed":
                    if isinstance(item.value, ast.List):
                        values = []
                        for elt in item.value.elts:
                            if isinstance(elt, ast.Constant) and isinstance(elt.value, str):
                                values.append(elt.value)
                        return values
    return []


def extract_init_attributes(
    class_node: ast.ClassDef,
    source_lines: list[str],
) -> list[AttributeInfo]:
    """Extract instance attributes from __init__ body (self.x = ...)."""
    init_method = None
    for item in class_node.body:
        if isinstance(item, ast.FunctionDef) and item.name == "__init__":
            init_method = item
            break

    if init_method is None:
        return []

    attrs: list[AttributeInfo] = []
    seen: set[str] = set()

    for stmt in ast.walk(init_method):
        if not isinstance(stmt, ast.Assign):
            continue
        for target in stmt.targets:
            if not isinstance(target, ast.Attribute):
                continue
            if not isinstance(target.value, ast.Name):
                continue
            if target.value.id != "self":
                continue

            attr_name = target.attr
            if attr_name.startswith("_") or attr_name in seen:
                continue
            seen.add(attr_name)

            # Try to get type from inline comment
            line = source_lines[stmt.lineno - 1] if stmt.lineno <= len(source_lines) else ""
            type_str = parse_inline_type_comment(line)

            # Fallback: infer from literal value
            if not type_str and stmt.value is not None:
                type_str = infer_type_from_value(stmt.value)

            attrs.append(AttributeInfo(name=attr_name, type_str=type_str))

    return attrs


def extract_properties(
    class_node: ast.ClassDef,
    source_lines: list[str],
) -> list[PropertyInfo]:
    """Extract @property definitions from a class."""
    props: list[PropertyInfo] = []

    for item in class_node.body:
        if not isinstance(item, ast.FunctionDef):
            continue
        if not has_decorator(item, "property"):
            continue
        if item.name.startswith("_"):
            continue

        docstring = ast.get_docstring(item) or ""
        _, return_type = parse_method_type_comment(source_lines, item)

        props.append(PropertyInfo(
            name=item.name,
            return_type=return_type,
            docstring=get_first_line(docstring),
        ))

    return props


def extract_methods(
    class_node: ast.ClassDef,
    source_lines: list[str],
    skip_methods: list[str],
) -> list[MethodInfo]:
    """Extract public methods from a class, excluding properties and skip list."""
    methods: list[MethodInfo] = []

    for item in class_node.body:
        if not isinstance(item, ast.FunctionDef):
            continue

        name = item.name
        # Skip private, dunder (except __init__ which we handle separately), properties
        if name.startswith("_"):
            continue
        if name in skip_methods:
            continue
        if has_decorator(item, "property"):
            continue
        # Skip setter/deleter
        if any(
            isinstance(d, ast.Attribute) and d.attr in ("setter", "deleter")
            for d in item.decorator_list
        ):
            continue

        is_cls = has_decorator(item, "classmethod")
        is_static = has_decorator(item, "staticmethod")

        # Parse type comment
        arg_types, return_type = parse_method_type_comment(source_lines, item)

        # Build arg list (exclude self/cls)
        func_args = item.args
        arg_names: list[str] = []
        for a in func_args.args:
            aname = a.arg if hasattr(a, "arg") else a.id  # type: ignore[attr-defined]
            if aname in ("self", "cls"):
                continue
            arg_names.append(aname)

        # Include *args and **kwargs
        if func_args.vararg:
            vararg = func_args.vararg
            arg_names.append("*" + (vararg.arg if hasattr(vararg, "arg") else vararg))  # type: ignore[arg-type]
        if func_args.kwarg:
            kwarg = func_args.kwarg
            arg_names.append("**" + (kwarg.arg if hasattr(kwarg, "arg") else kwarg))  # type: ignore[arg-type]

        # Match arg types positionally
        args: list[ArgInfo] = []
        docstring = ast.get_docstring(item) or ""
        arg_descs = parse_docstring_section(docstring, "Arguments")

        for i, aname in enumerate(arg_names):
            clean_name = aname.lstrip("*")
            atype = arg_types[i] if i < len(arg_types) else ""
            adesc = arg_descs.get(clean_name, "")
            args.append(ArgInfo(name=aname, type_str=atype, description=adesc))

        methods.append(MethodInfo(
            name=name,
            args=args,
            return_type=return_type,
            docstring=get_first_line(docstring),
            is_classmethod=is_cls,
            is_staticmethod=is_static,
        ))

    return methods


def extract_class(
    class_node: ast.ClassDef,
    source_lines: list[str],
    skip_methods: list[str],
    module_path: str,
) -> ClassInfo:
    """Extract all documentation info from a single class."""
    docstring = ast.get_docstring(class_node) or ""
    bases = extract_base_names(class_node)
    enum = is_enum_class(class_node)

    info = ClassInfo(
        name=class_node.name,
        module_path=module_path,
        bases=bases,
        docstring=docstring,
        is_enum=enum,
    )

    if enum:
        raw_values = extract_enum_values(class_node)
        value_descs = parse_enum_values_section(docstring)
        info.enum_values = [(v, value_descs.get(v, "")) for v in raw_values]
    else:
        # Attribute descriptions from class docstring
        attr_descs = parse_docstring_section(docstring, "Attributes")
        attrs = extract_init_attributes(class_node, source_lines)
        for attr in attrs:
            attr.description = attr_descs.get(attr.name, "")
        info.attributes = attrs
        info.properties = extract_properties(class_node, source_lines)
        info.methods = extract_methods(class_node, source_lines, skip_methods)

    return info


def extract_module(
    file_path: Path,
    source_path: str,
    skip_methods: list[str],
) -> ModuleInfo | None:
    """Parse a .py file and extract all public classes.

    Returns None if the module has no public classes.
    """
    try:
        source = file_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"  [WARN] Cannot read {file_path}: {e}")
        return None

    try:
        tree = ast.parse(source, filename=str(file_path))
    except SyntaxError as e:
        print(f"  [WARN] Syntax error in {file_path}: {e}")
        return None

    source_lines = source.split("\n")
    module_docstring = ast.get_docstring(tree) or ""
    module_name = file_path.stem

    classes: list[ClassInfo] = []
    for node in ast.iter_child_nodes(tree):
        if not isinstance(node, ast.ClassDef):
            continue
        # Skip private classes (but include _Base classes)
        if node.name.startswith("_") and not node.name.startswith("_Base"):
            continue

        cls_info = extract_class(
            node, source_lines, skip_methods,
            module_path=f"{source_path}/{file_path.name}",
        )
        classes.append(cls_info)

    if not classes:
        return None

    return ModuleInfo(
        name=module_name,
        source_path=f"{source_path}/{file_path.name}",
        docstring=get_first_line(module_docstring),
        classes=classes,
    )


# ---------------------------------------------------------------------------
# File discovery + filtering
# ---------------------------------------------------------------------------

def should_include_file(
    file_path: Path,
    source_path_root: Path,
    exclude_modules: list[str],
    exclude_patterns: list[str],
    include_patterns: list[str],
) -> bool:
    """Determine whether a .py file should be processed."""
    filename = file_path.name

    # Check include_patterns first (overrides exclude)
    for pattern in include_patterns:
        if fnmatch.fnmatch(filename, pattern):
            return True

    # Check exclude_patterns
    for pattern in exclude_patterns:
        if fnmatch.fnmatch(filename, pattern):
            return False

    # Check exclude_modules (relative path from cache root)
    rel = file_path.relative_to(source_path_root.parent)
    rel_dir = str(rel.parent)
    for excl in exclude_modules:
        # Match directory prefixes: "honeybee_ph/cli" matches any file under cli/
        if rel_dir == excl or rel_dir.startswith(excl + "/"):
            return False
        # Also check the full relative path without extension
        rel_no_ext = str(rel.with_suffix(""))
        if rel_no_ext == excl:
            return False

    # __init__.py files generally don't have interesting classes
    if filename == "__init__.py":
        return False

    return True


def discover_modules(
    source_root: Path,
    source_path_name: str,
    exclude_modules: list[str],
    exclude_patterns: list[str],
    include_patterns: list[str],
) -> list[Path]:
    """Walk a source directory and return .py files that pass filtering."""
    source_dir = source_root / source_path_name
    if not source_dir.is_dir():
        print(f"  [WARN] Source directory not found: {source_dir}")
        return []

    results: list[Path] = []
    for py_file in sorted(source_dir.rglob("*.py")):
        if should_include_file(
            py_file, source_dir, exclude_modules,
            exclude_patterns, include_patterns,
        ):
            results.append(py_file)

    return results


# ---------------------------------------------------------------------------
# Markdown rendering
# ---------------------------------------------------------------------------

def render_class_md(cls: ClassInfo) -> str:
    """Render a single class as markdown."""
    lines: list[str] = []

    # Class heading
    lines.append(f"## {cls.name}")
    lines.append("")

    # Docstring summary
    summary = get_first_line(cls.docstring) if cls.docstring else "No description available."
    lines.append(summary)
    lines.append("")

    # Inheritance
    if cls.bases and cls.bases != ["object"]:
        bases_str = ", ".join(f"`{b}`" for b in cls.bases)
        lines.append(f"**Inherits from**: {bases_str}")
        lines.append("")

    # Enum values table
    if cls.is_enum and cls.enum_values:
        lines.append("### Values")
        lines.append("")
        lines.append("| Value | Meaning |")
        lines.append("|-------|---------|")
        for value, desc in cls.enum_values:
            lines.append(f"| `\"{value}\"` | {desc or '—'} |")
        lines.append("")

    # Attributes table
    if cls.attributes:
        lines.append("### Attributes")
        lines.append("")
        lines.append("| Attribute | Type | Description |")
        lines.append("|-----------|------|-------------|")
        for attr in cls.attributes:
            type_col = f"`{attr.type_str}`" if attr.type_str else "—"
            desc_col = attr.description or "—"
            lines.append(f"| `{attr.name}` | {type_col} | {desc_col} |")
        lines.append("")

    # Properties table
    if cls.properties:
        lines.append("### Properties")
        lines.append("")
        lines.append("| Property | Type | Description |")
        lines.append("|----------|------|-------------|")
        for prop in cls.properties:
            type_col = f"`{prop.return_type}`" if prop.return_type else "—"
            desc_col = prop.docstring or "—"
            lines.append(f"| `{prop.name}` | {type_col} | {desc_col} |")
        lines.append("")

    # Methods
    if cls.methods:
        lines.append("### Methods")
        lines.append("")
        for method in cls.methods:
            # Method signature
            arg_strs = [a.name for a in method.args]
            sig = ", ".join(arg_strs)
            prefix = ""
            if method.is_classmethod:
                prefix = "*classmethod* "
            elif method.is_staticmethod:
                prefix = "*staticmethod* "
            lines.append(f"#### {prefix}{method.name}({sig})")
            lines.append("")

            # Docstring summary
            if method.docstring:
                lines.append(method.docstring)
                lines.append("")

            # Args table
            if method.args:
                lines.append("| Arg | Type | Description |")
                lines.append("|-----|------|-------------|")
                for arg in method.args:
                    type_col = f"`{arg.type_str}`" if arg.type_str else "—"
                    desc_col = arg.description or "—"
                    lines.append(f"| `{arg.name}` | {type_col} | {desc_col} |")
                lines.append("")

            # Return type
            if method.return_type:
                lines.append(f"**Returns**: `{method.return_type}`")
                lines.append("")

    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def render_module_md(module: ModuleInfo, is_first_file: bool) -> str:
    """Render a full module page as markdown."""
    lines: list[str] = []

    # Front-matter
    lines.append("---")
    lines.append(f'title: "{module.name}"')
    if is_first_file:
        lines.append("card_title: API Reference")
        lines.append('card_description: "Auto-generated reference for the public API."')
        lines.append('card_index: "99"')
    lines.append("---")
    lines.append("")

    # Module heading
    lines.append(f"# {module.name}")
    lines.append("")
    if module.docstring:
        lines.append(module.docstring)
        lines.append("")
    lines.append(f"**Source**: `{module.source_path}`")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Classes
    for cls in module.classes:
        lines.append(render_class_md(cls))

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Output path mapping
# ---------------------------------------------------------------------------

def get_output_subdir(source_path: str, primary_source_path: str) -> str:
    """Derive output subdirectory for a non-primary source path.

    Strips the common prefix with the primary source path.
    e.g. primary="honeybee_ph", source="honeybee_phhvac" → "hvac"
    """
    prefix = os.path.commonprefix([primary_source_path, source_path])
    remainder = source_path[len(prefix):].lstrip("_")
    return remainder if remainder else source_path


def get_output_path(
    py_file: Path,
    source_dir: Path,
    source_path_name: str,
    primary_source_path: str,
    output_dir: str,
) -> Path:
    """Compute the output .md path for a given .py file."""
    # Relative path within the source package (handles subdirectories)
    rel = py_file.relative_to(source_dir / source_path_name)
    md_name = rel.with_suffix(".md")

    if source_path_name == primary_source_path:
        return Path(output_dir) / md_name
    else:
        subdir = get_output_subdir(source_path_name, primary_source_path)
        return Path(output_dir) / subdir / md_name


# ---------------------------------------------------------------------------
# Main generation pipeline
# ---------------------------------------------------------------------------

def get_autodoc_config(lib: dict) -> dict:
    """Merge per-library autodoc config with defaults."""
    autodoc = lib.get("autodoc", {})
    config = dict(DEFAULT_AUTODOC)
    config.update(autodoc)
    return config


def generate_library(
    lib: dict,
    verbose: bool = False,
    dry_run: bool = False,
) -> tuple[int, int, int]:
    """Generate API docs for a single library.

    Returns (modules_processed, classes_documented, files_skipped).
    """
    lib_id = lib["id"]
    source_paths = lib.get("source_paths", [])
    config = get_autodoc_config(lib)

    if not source_paths:
        if verbose:
            print(f"  [SKIP] {lib_id}: no source_paths configured")
        return 0, 0, 0

    if not config.get("enabled", True):
        if verbose:
            print(f"  [SKIP] {lib_id}: autodoc disabled")
        return 0, 0, 0

    cache_root = CACHE_DIR / lib_id
    if not cache_root.is_dir():
        print(f"  [WARN] Cache directory not found: {cache_root}")
        return 0, 0, 0

    output_base = CONTENT_DIR / lib_id / config["output_dir"]
    primary_source = source_paths[0]

    modules_processed = 0
    classes_documented = 0
    files_skipped = 0
    generated_files: list[str] = []
    is_first_file = True

    for source_path_name in source_paths:
        py_files = discover_modules(
            cache_root, source_path_name,
            config["exclude_modules"],
            config["exclude_patterns"],
            config["include_patterns"],
        )

        if verbose:
            print(f"  [{source_path_name}] Found {len(py_files)} source files")

        for py_file in py_files:
            module = extract_module(py_file, source_path_name, config["skip_methods"])
            if module is None:
                files_skipped += 1
                continue

            output_path = get_output_path(
                py_file, cache_root, source_path_name,
                primary_source, config["output_dir"],
            )
            full_output = CONTENT_DIR / lib_id / output_path

            md_content = render_module_md(module, is_first_file)
            is_first_file = False

            if dry_run:
                print(f"  [DRY] Would write: {full_output} ({len(module.classes)} classes)")
            else:
                full_output.parent.mkdir(parents=True, exist_ok=True)
                full_output.write_text(md_content, encoding="utf-8")
                if verbose:
                    print(f"  [WRITE] {full_output} ({len(module.classes)} classes)")

            generated_files.append(str(output_path))
            modules_processed += 1
            classes_documented += sum(1 for _ in module.classes)

    # Write generated files manifest
    if not dry_run and generated_files:
        manifest_path = output_base / ".generated_files"
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text("\n".join(generated_files) + "\n", encoding="utf-8")

    # Write nav fragment
    if not dry_run and generated_files:
        nav_lines = ["# Auto-generated nav fragment for API Reference", "# Copy relevant entries into your spoke's docs/nav.yml", ""]
        for gf in generated_files:
            # Strip output_dir prefix for the nav path
            label = Path(gf).stem
            nav_lines.append(f"    - {label}: {gf}")
        fragment_path = output_base / "_nav_fragment.yml"
        fragment_path.write_text("\n".join(nav_lines) + "\n", encoding="utf-8")

    return modules_processed, classes_documented, files_skipped


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate API reference docs from spoke source code.")
    parser.add_argument("--library", help="Process only this library (by id)")
    parser.add_argument("--verbose", action="store_true", help="Detailed per-file logging")
    parser.add_argument("--dry-run", action="store_true", help="Print what would be generated without writing")
    args = parser.parse_args()

    try:
        with open(LIBRARIES_YML) as f:
            data = yaml.safe_load(f)
        libraries = data.get("libraries", [])
    except Exception as e:
        print(f"[ERROR] Cannot read {LIBRARIES_YML}: {e}")
        sys.exit(0)

    total_modules = 0
    total_classes = 0
    total_skipped = 0

    for lib in libraries:
        lib_id = lib["id"]
        if args.library and lib_id != args.library:
            continue
        if not lib.get("enabled", True):
            continue

        print(f"[AUTODOC] {lib_id}...")
        try:
            m, c, s = generate_library(lib, verbose=args.verbose, dry_run=args.dry_run)
            total_modules += m
            total_classes += c
            total_skipped += s
            print(f"[OK]      {lib_id}: {m} modules, {c} classes ({s} files skipped)")
        except Exception as e:
            print(f"[ERROR]   {lib_id}: {e}")
            if args.verbose:
                import traceback
                traceback.print_exc()

    print(f"\nAPI docs: {total_modules} modules, {total_classes} classes, {total_skipped} skipped")


if __name__ == "__main__":
    main()
