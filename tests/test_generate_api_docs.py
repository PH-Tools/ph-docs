"""Tests for the API documentation generator.

Covers: type comment parsing, type inference, docstring section parsing,
AST extraction, file filtering, markdown rendering, and end-to-end generation.
"""

from __future__ import annotations

import ast
import textwrap
from pathlib import Path

import pytest

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from generate_api_docs import (
    ArgInfo,
    AttributeInfo,
    ClassInfo,
    MethodInfo,
    ModuleInfo,
    PropertyInfo,
    extract_base_names,
    extract_class,
    extract_enum_values,
    extract_init_attributes,
    extract_methods,
    extract_module,
    extract_properties,
    extract_standard_enum_members,
    get_first_line,
    get_output_subdir,
    infer_type_from_value,
    is_enum_class,
    parse_docstring_section,
    parse_enum_values_section,
    parse_inline_type_comment,
    parse_method_type_comment,
    render_class_md,
    render_module_md,
    should_include_file,
)


# -----------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------

def parse_first_class(source: str) -> ast.ClassDef:
    """Parse source and return the first ClassDef node."""
    tree = ast.parse(textwrap.dedent(source))
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.ClassDef):
            return node
    raise ValueError("No ClassDef found in source")


def parse_first_func(source: str) -> ast.FunctionDef:
    """Parse source and return the first FunctionDef node."""
    tree = ast.parse(textwrap.dedent(source))
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            return node
    raise ValueError("No FunctionDef found in source")


# -----------------------------------------------------------------------
# Type comment parsing
# -----------------------------------------------------------------------

class TestParseMethodTypeComment:
    def test_simple_method(self):
        source = textwrap.dedent("""\
            def add(self, segment):
                # type: (SpaceFloorSegment) -> None
                pass
        """)
        lines = source.split("\n")
        func = parse_first_func(source)
        arg_types, ret = parse_method_type_comment(lines, func)
        assert arg_types == ["SpaceFloorSegment"]
        assert ret == "None"

    def test_multi_arg_method(self):
        source = textwrap.dedent("""\
            def process(self, name, count, flag):
                # type: (str, int, bool) -> Dict[str, Any]
                pass
        """)
        lines = source.split("\n")
        func = parse_first_func(source)
        arg_types, ret = parse_method_type_comment(lines, func)
        assert arg_types == ["str", "int", "bool"]
        assert ret == "Dict[str, Any]"

    def test_property_type_comment(self):
        source = textwrap.dedent("""\
            def weighted_area(self):
                # type: () -> float
                return 0.0
        """)
        lines = source.split("\n")
        func = parse_first_func(source)
        arg_types, ret = parse_method_type_comment(lines, func)
        assert arg_types == []
        assert ret == "float"

    def test_no_type_comment(self):
        source = textwrap.dedent("""\
            def foo(self, x):
                return x
        """)
        lines = source.split("\n")
        func = parse_first_func(source)
        arg_types, ret = parse_method_type_comment(lines, func)
        assert arg_types == []
        assert ret == ""


class TestParseInlineTypeComment:
    def test_simple_type(self):
        assert parse_inline_type_comment("self.x = None  # type: Optional[LBFace3D]") == "Optional[LBFace3D]"

    def test_float_type(self):
        assert parse_inline_type_comment("self.factor = 1.0  # type: float") == "float"

    def test_no_comment(self):
        assert parse_inline_type_comment("self.x = 42") == ""

    def test_non_type_comment(self):
        assert parse_inline_type_comment("self.x = 42  # some comment") == ""


# -----------------------------------------------------------------------
# Type inference from literals
# -----------------------------------------------------------------------

class TestInferTypeFromValue:
    def _infer(self, expr_str: str) -> str:
        node = ast.parse(expr_str, mode="eval").body
        return infer_type_from_value(node)

    def test_float(self):
        assert self._infer("1.0") == "float"

    def test_int(self):
        assert self._infer("42") == "int"

    def test_string(self):
        assert self._infer('"hello"') == "str"

    def test_bool_true(self):
        assert self._infer("True") == "bool"

    def test_bool_false(self):
        assert self._infer("False") == "bool"

    def test_none(self):
        assert self._infer("None") == "Optional[unknown]"

    def test_empty_list(self):
        assert self._infer("[]") == "List"

    def test_empty_dict(self):
        assert self._infer("{}") == "Dict"

    def test_constructor_call(self):
        assert self._infer("SomeClass()") == "SomeClass"

    def test_unknown_expression(self):
        assert self._infer("a + b") == ""


# -----------------------------------------------------------------------
# Docstring section parsing
# -----------------------------------------------------------------------

class TestParseDocstringSection:
    def test_attributes_google_style(self):
        doc = textwrap.dedent("""\
            A space floor segment.

            Attributes:
                geometry (Optional[LBFace3D]): The planar 3D geometry.
                weighting_factor (float): Multiplier for area calc.
                    Default: 1.0 (no reduction).
        """)
        result = parse_docstring_section(doc, "Attributes")
        assert "geometry" in result
        assert "planar 3D geometry" in result["geometry"]
        assert "weighting_factor" in result
        assert "Default: 1.0" in result["weighting_factor"]

    def test_arguments_honeybee_style(self):
        doc = textwrap.dedent("""\
            Add a floor segment.

            Arguments:
            ----------
                * segment (SpaceFloorSegment): The floor segment to add.
                * factor (float): Weighting factor.
        """)
        result = parse_docstring_section(doc, "Arguments")
        assert "segment" in result
        assert "floor segment to add" in result["segment"]
        assert "factor" in result

    def test_empty_docstring(self):
        assert parse_docstring_section("", "Attributes") == {}

    def test_missing_section(self):
        assert parse_docstring_section("Just a summary.", "Attributes") == {}


class TestParseEnumValuesSection:
    def test_values_section(self):
        doc = textwrap.dedent("""\
            Classification of foundation types.

            Values:
                1-HEATED_BASEMENT: Fully conditioned basement.
                2-UNHEATED_BASEMENT: Unconditioned basement.
                3-SLAB_ON_GRADE: Foundation slab on soil.
        """)
        result = parse_enum_values_section(doc)
        assert result["1-HEATED_BASEMENT"] == "Fully conditioned basement."
        assert result["2-UNHEATED_BASEMENT"] == "Unconditioned basement."
        assert result["3-SLAB_ON_GRADE"] == "Foundation slab on soil."

    def test_no_values_section(self):
        assert parse_enum_values_section("Just a summary.") == {}


class TestGetFirstLine:
    def test_multiline(self):
        assert get_first_line("First line.\nSecond line.") == "First line."

    def test_empty(self):
        assert get_first_line("") == ""

    def test_leading_blank(self):
        assert get_first_line("\n\nActual first.") == "Actual first."


# -----------------------------------------------------------------------
# AST extraction
# -----------------------------------------------------------------------

class TestExtractBaseNames:
    def test_simple_base(self):
        source = "class Foo(Bar): pass"
        cls = parse_first_class(source)
        assert extract_base_names(cls) == ["Bar"]

    def test_dotted_base(self):
        source = "class Foo(_base._Base): pass"
        cls = parse_first_class(source)
        assert extract_base_names(cls) == ["_base._Base"]

    def test_multiple_bases(self):
        source = "class Foo(Bar, Baz): pass"
        cls = parse_first_class(source)
        assert extract_base_names(cls) == ["Bar", "Baz"]

    def test_object_base(self):
        source = "class Foo(object): pass"
        cls = parse_first_class(source)
        assert extract_base_names(cls) == ["object"]


class TestIsEnumClass:
    def test_custom_enum_base(self):
        source = textwrap.dedent("""\
            class MyEnum(enumerables.CustomEnum):
                allowed = ["A", "B"]
        """)
        cls = parse_first_class(source)
        assert is_enum_class(cls) is True

    def test_has_allowed_attribute(self):
        source = textwrap.dedent("""\
            class MyEnum(object):
                allowed = ["A", "B"]
        """)
        cls = parse_first_class(source)
        assert is_enum_class(cls) is True

    def test_standard_enum_base(self):
        source = textwrap.dedent("""\
            class FaceType(Enum):
                WALL = 1
                FLOOR = 2
        """)
        cls = parse_first_class(source)
        assert is_enum_class(cls) is True

    def test_normal_class(self):
        source = textwrap.dedent("""\
            class Foo(object):
                def __init__(self):
                    self.x = 1
        """)
        cls = parse_first_class(source)
        assert is_enum_class(cls) is False


class TestExtractEnumValues:
    def test_string_values(self):
        source = textwrap.dedent("""\
            class MyEnum(object):
                allowed = ["1-FOO", "2-BAR", "3-BAZ"]
        """)
        cls = parse_first_class(source)
        assert extract_enum_values(cls) == ["1-FOO", "2-BAR", "3-BAZ"]

    def test_no_allowed(self):
        source = "class Foo(object): pass"
        cls = parse_first_class(source)
        assert extract_enum_values(cls) == []


class TestExtractStandardEnumMembers:
    def test_integer_members(self):
        source = textwrap.dedent("""\
            class FaceType(Enum):
                NONE = 0
                WALL = 1
                FLOOR = 2
        """)
        cls = parse_first_class(source)
        members = extract_standard_enum_members(cls)
        assert members == [("NONE", "0"), ("WALL", "1"), ("FLOOR", "2")]

    def test_negative_members(self):
        source = textwrap.dedent("""\
            class Exposure(Enum):
                NONE = 0
                EXTERIOR = -1
                GROUND = -2
        """)
        cls = parse_first_class(source)
        members = extract_standard_enum_members(cls)
        assert members == [("NONE", "0"), ("EXTERIOR", "-1"), ("GROUND", "-2")]

    def test_skips_private_and_dunder(self):
        source = textwrap.dedent("""\
            class MyEnum(Enum):
                GOOD = 1
                _PRIVATE = 2
                __DUNDER = 3
        """)
        cls = parse_first_class(source)
        members = extract_standard_enum_members(cls)
        assert members == [("GOOD", "1")]

    def test_no_members(self):
        source = "class Foo(object): pass"
        cls = parse_first_class(source)
        assert extract_standard_enum_members(cls) == []


class TestExtractInitAttributes:
    def test_typed_attributes(self):
        source = textwrap.dedent("""\
            class Foo(object):
                def __init__(self):
                    self.name = ""  # type: str
                    self.count = 0  # type: int
                    self.data = None  # type: Optional[List]
        """)
        cls = parse_first_class(source)
        lines = source.split("\n")
        attrs = extract_init_attributes(cls, lines)
        assert len(attrs) == 3
        assert attrs[0].name == "name"
        assert attrs[0].type_str == "str"
        assert attrs[1].name == "count"
        assert attrs[1].type_str == "int"
        assert attrs[2].name == "data"
        assert attrs[2].type_str == "Optional[List]"

    def test_inferred_types(self):
        source = textwrap.dedent("""\
            class Foo(object):
                def __init__(self):
                    self.factor = 1.0
                    self.label = "default"
                    self.active = True
        """)
        cls = parse_first_class(source)
        lines = source.split("\n")
        attrs = extract_init_attributes(cls, lines)
        assert attrs[0].type_str == "float"
        assert attrs[1].type_str == "str"
        assert attrs[2].type_str == "bool"

    def test_skips_private_attrs(self):
        source = textwrap.dedent("""\
            class Foo(object):
                def __init__(self):
                    self._internal = 0
                    self.public = 1
        """)
        cls = parse_first_class(source)
        lines = source.split("\n")
        attrs = extract_init_attributes(cls, lines)
        assert len(attrs) == 1
        assert attrs[0].name == "public"

    def test_no_init(self):
        source = "class Foo(object): pass"
        cls = parse_first_class(source)
        assert extract_init_attributes(cls, []) == []


class TestExtractProperties:
    def test_property_with_type(self):
        source = textwrap.dedent("""\
            class Foo(object):
                @property
                def area(self):
                    # type: () -> float
                    \"\"\"The total area.\"\"\"
                    return 0.0
        """)
        cls = parse_first_class(source)
        lines = source.split("\n")
        props = extract_properties(cls, lines)
        assert len(props) == 1
        assert props[0].name == "area"
        assert props[0].return_type == "float"
        assert props[0].docstring == "The total area."

    def test_skips_private_property(self):
        source = textwrap.dedent("""\
            class Foo(object):
                @property
                def _internal(self):
                    return 0
                @property
                def public(self):
                    return 1
        """)
        cls = parse_first_class(source)
        lines = source.split("\n")
        props = extract_properties(cls, lines)
        assert len(props) == 1
        assert props[0].name == "public"


class TestExtractMethods:
    def test_public_method(self):
        source = textwrap.dedent("""\
            class Foo(object):
                def process(self, name, count):
                    # type: (str, int) -> bool
                    \"\"\"Process the data.\"\"\"
                    return True
        """)
        cls = parse_first_class(source)
        lines = source.split("\n")
        methods = extract_methods(cls, lines, skip_methods=["to_dict"])
        assert len(methods) == 1
        assert methods[0].name == "process"
        assert methods[0].return_type == "bool"
        assert len(methods[0].args) == 2
        assert methods[0].args[0].name == "name"
        assert methods[0].args[0].type_str == "str"

    def test_skips_configured_methods(self):
        source = textwrap.dedent("""\
            class Foo(object):
                def to_dict(self):
                    pass
                def from_dict(self, d):
                    pass
                def real_method(self):
                    pass
        """)
        cls = parse_first_class(source)
        lines = source.split("\n")
        methods = extract_methods(cls, lines, skip_methods=["to_dict", "from_dict"])
        assert len(methods) == 1
        assert methods[0].name == "real_method"

    def test_skips_private_methods(self):
        source = textwrap.dedent("""\
            class Foo(object):
                def _helper(self):
                    pass
                def public(self):
                    pass
        """)
        cls = parse_first_class(source)
        lines = source.split("\n")
        methods = extract_methods(cls, lines, skip_methods=[])
        assert len(methods) == 1
        assert methods[0].name == "public"

    def test_classmethod(self):
        source = textwrap.dedent("""\
            class Foo(object):
                @classmethod
                def create(cls, data):
                    # type: (dict) -> Foo
                    pass
        """)
        cls = parse_first_class(source)
        lines = source.split("\n")
        methods = extract_methods(cls, lines, skip_methods=[])
        assert len(methods) == 1
        assert methods[0].is_classmethod is True
        assert methods[0].args[0].name == "data"

    def test_staticmethod(self):
        source = textwrap.dedent("""\
            class Foo(object):
                @staticmethod
                def helper(x):
                    # type: (int) -> int
                    pass
        """)
        cls = parse_first_class(source)
        lines = source.split("\n")
        methods = extract_methods(cls, lines, skip_methods=[])
        assert len(methods) == 1
        assert methods[0].is_staticmethod is True

    def test_does_not_include_properties(self):
        source = textwrap.dedent("""\
            class Foo(object):
                @property
                def area(self):
                    return 0.0
                def method(self):
                    pass
        """)
        cls = parse_first_class(source)
        lines = source.split("\n")
        methods = extract_methods(cls, lines, skip_methods=[])
        assert len(methods) == 1
        assert methods[0].name == "method"


# -----------------------------------------------------------------------
# File filtering
# -----------------------------------------------------------------------

class TestShouldIncludeFile:
    def _check(self, filename, *, exclude_modules=None, exclude_patterns=None, include_patterns=None):
        """Helper: create a fake file path and check inclusion."""
        root = Path("/fake/cache/honeybee_ph")
        fp = root / filename
        return should_include_file(
            fp, root,
            exclude_modules=exclude_modules or [],
            exclude_patterns=exclude_patterns or ["_*", "test_*"],
            include_patterns=include_patterns or ["_base.py"],
        )

    def test_normal_file(self):
        assert self._check("space.py") is True

    def test_private_file_excluded(self):
        assert self._check("_internal.py") is False

    def test_base_file_included(self):
        assert self._check("_base.py") is True

    def test_test_file_excluded(self):
        assert self._check("test_space.py") is False

    def test_init_excluded(self):
        assert self._check("__init__.py") is False

    def test_exclude_module_dir(self):
        root = Path("/fake/cache")
        fp = root / "honeybee_ph" / "cli" / "export.py"
        assert should_include_file(
            fp,
            root / "honeybee_ph",
            exclude_modules=["honeybee_ph/cli"],
            exclude_patterns=["_*"],
            include_patterns=[],
        ) is False


# -----------------------------------------------------------------------
# Output path mapping
# -----------------------------------------------------------------------

class TestGetOutputSubdir:
    def test_strips_common_prefix(self):
        assert get_output_subdir("honeybee_phhvac", "honeybee_ph") == "hvac"

    def test_same_path(self):
        assert get_output_subdir("honeybee_ph", "honeybee_ph") == "honeybee_ph"

    def test_no_common_prefix(self):
        assert get_output_subdir("PHX", "honeybee_ph") == "PHX"


# -----------------------------------------------------------------------
# Markdown rendering
# -----------------------------------------------------------------------

class TestRenderClassMd:
    def test_basic_class(self):
        cls = ClassInfo(
            name="MyClass",
            bases=["_Base"],
            docstring="A useful class.",
            attributes=[
                AttributeInfo("name", "str", "The name."),
                AttributeInfo("count", "int", "The count."),
            ],
        )
        md = render_class_md(cls)
        assert "## MyClass" in md
        assert "A useful class." in md
        assert "`_Base`" in md
        assert "| `name` | `str` | The name. |" in md

    def test_custom_enum_class(self):
        cls = ClassInfo(
            name="FoundationType",
            is_enum=True,
            enum_values=[
                ("1-HEATED", "", "Heated basement."),
                ("2-SLAB", "", "Slab on grade."),
            ],
            docstring="Foundation types.",
        )
        md = render_class_md(cls)
        assert "### Values" in md
        assert "| Value | Meaning |" in md
        assert '`"1-HEATED"`' in md
        assert "Heated basement." in md

    def test_standard_enum_class(self):
        cls = ClassInfo(
            name="FaceType",
            bases=["Enum"],
            is_enum=True,
            enum_values=[
                ("NONE", "0", "Unclassified face type."),
                ("WALL", "1", "Vertical wall surface."),
            ],
            docstring="Face orientations.",
        )
        md = render_class_md(cls)
        assert "### Values" in md
        assert "| Member | Value | Meaning |" in md
        assert "| `NONE` | `0` | Unclassified face type. |" in md
        assert "| `WALL` | `1` | Vertical wall surface. |" in md

    def test_class_with_methods(self):
        cls = ClassInfo(
            name="Worker",
            docstring="Does work.",
            methods=[
                MethodInfo(
                    name="run",
                    args=[ArgInfo("task", "str", "Task name.")],
                    return_type="bool",
                    docstring="Run a task.",
                ),
            ],
        )
        md = render_class_md(cls)
        assert "### Methods" in md
        assert "#### run(task)" in md
        assert "Run a task." in md
        assert "**Returns**: `bool`" in md

    def test_no_docstring(self):
        cls = ClassInfo(name="Empty")
        md = render_class_md(cls)
        assert "No description available." in md


class TestRenderModuleMd:
    def test_first_file_has_card_frontmatter(self):
        module = ModuleInfo(
            name="space",
            source_path="honeybee_ph/space.py",
            docstring="PH Space Objects.",
            classes=[ClassInfo(name="Space", docstring="A space.")],
        )
        md = render_module_md(module, is_first_file=True)
        assert "card_title: API Reference" in md
        assert 'card_index: "99"' in md

    def test_non_first_file_no_card_frontmatter(self):
        module = ModuleInfo(
            name="zone",
            source_path="honeybee_ph/zone.py",
            classes=[ClassInfo(name="Zone", docstring="A zone.")],
        )
        md = render_module_md(module, is_first_file=False)
        assert "card_title" not in md


# -----------------------------------------------------------------------
# End-to-end: source → ModuleInfo
# -----------------------------------------------------------------------

class TestExtractModule:
    """Integration test: parse a realistic Python 2.7-style source file."""

    FIXTURE_SOURCE = textwrap.dedent('''\
        # -*- coding: utf-8 -*-
        # -*- Python Version: 2.7 -*-

        """PH Foundation Objects."""

        try:
            from typing import Any, Dict, List, Optional
        except ImportError:
            pass

        from honeybee_ph import _base
        from honeybee_ph import enumerables


        class PhFoundationType(enumerables.CustomEnum):
            """Classification of foundation types.

            Values:
                1-HEATED_BASEMENT: Heated basement.
                2-SLAB_ON_GRADE: Slab on grade.
                3-NONE: No foundation.
            """
            allowed = [
                "1-HEATED_BASEMENT",
                "2-SLAB_ON_GRADE",
                "3-NONE",
            ]


        class PhFoundation(_base._Base):
            """Base class for all foundation types.

            Attributes:
                foundation_type (PhFoundationType): The foundation classification.
            """

            def __init__(self):
                super(PhFoundation, self).__init__()
                self.foundation_type = None  # type: Optional[PhFoundationType]

            def add_segment(self, segment):
                # type: (Any) -> None
                """Add a foundation segment.

                Arguments:
                ----------
                    * segment (Any): The segment to add.

                Returns:
                --------
                    * None
                """
                pass

            def to_dict(self):
                pass

            def _private_method(self):
                pass

            @property
            def area(self):
                # type: () -> float
                """Total foundation area."""
                return 0.0


        class _PrivateClass(object):
            """Should be skipped."""
            pass
    ''')

    def test_extract(self, tmp_path):
        """Write fixture to disk and extract module."""
        py_file = tmp_path / "foundations.py"
        py_file.write_text(self.FIXTURE_SOURCE)

        module = extract_module(py_file, "honeybee_ph", skip_methods=["to_dict", "from_dict"])

        assert module is not None
        assert module.name == "foundations"
        assert module.docstring == "PH Foundation Objects."

        # Should have 2 classes: PhFoundationType and PhFoundation
        # _PrivateClass should be skipped
        assert len(module.classes) == 2
        names = [c.name for c in module.classes]
        assert "PhFoundationType" in names
        assert "PhFoundation" in names
        assert "_PrivateClass" not in names

        # Check enum
        enum_cls = next(c for c in module.classes if c.name == "PhFoundationType")
        assert enum_cls.is_enum is True
        assert len(enum_cls.enum_values) == 3
        assert enum_cls.enum_values[0] == ("1-HEATED_BASEMENT", "", "Heated basement.")

        # Check regular class
        found_cls = next(c for c in module.classes if c.name == "PhFoundation")
        assert found_cls.is_enum is False
        assert found_cls.bases == ["_base._Base"]

        # Attributes
        assert len(found_cls.attributes) == 1
        assert found_cls.attributes[0].name == "foundation_type"
        assert found_cls.attributes[0].type_str == "Optional[PhFoundationType]"
        assert "classification" in found_cls.attributes[0].description.lower()

        # Properties
        assert len(found_cls.properties) == 1
        assert found_cls.properties[0].name == "area"
        assert found_cls.properties[0].return_type == "float"

        # Methods — to_dict and _private_method should be excluded
        assert len(found_cls.methods) == 1
        assert found_cls.methods[0].name == "add_segment"
        assert found_cls.methods[0].return_type == "None"
        assert found_cls.methods[0].args[0].name == "segment"
        assert found_cls.methods[0].args[0].type_str == "Any"

    def test_standard_enum_extraction(self, tmp_path):
        """Standard Python Enum members should be extracted with values."""
        source = textwrap.dedent('''\
            """Building enums."""

            from enum import Enum

            class FaceType(Enum):
                """Classification of face orientations.

                Values:
                    NONE: Unclassified face type.
                    WALL: Vertical wall surface.
                    FLOOR: Horizontal floor surface.
                """
                NONE = 0
                WALL = 1
                FLOOR = 2
        ''')
        py_file = tmp_path / "building.py"
        py_file.write_text(source)

        module = extract_module(py_file, "PHX", skip_methods=[])
        assert module is not None

        cls = module.classes[0]
        assert cls.name == "FaceType"
        assert cls.is_enum is True
        assert len(cls.enum_values) == 3
        assert cls.enum_values[0] == ("NONE", "0", "Unclassified face type.")
        assert cls.enum_values[1] == ("WALL", "1", "Vertical wall surface.")
        assert cls.enum_values[2] == ("FLOOR", "2", "Horizontal floor surface.")

        # Should not have attributes/properties/methods
        assert cls.attributes == []
        assert cls.properties == []
        assert cls.methods == []

    def test_standard_enum_negative_values(self, tmp_path):
        """Standard Enum with negative values should extract correctly."""
        source = textwrap.dedent('''\
            """Exposure enums."""

            from enum import Enum

            class Exposure(Enum):
                """Exterior exposure.

                Values:
                    NONE: No exposure.
                    EXTERIOR: Outdoor air.
                """
                NONE = 0
                EXTERIOR = -1
        ''')
        py_file = tmp_path / "exposure.py"
        py_file.write_text(source)

        module = extract_module(py_file, "PHX", skip_methods=[])
        assert module is not None

        cls = module.classes[0]
        assert cls.enum_values[1] == ("EXTERIOR", "-1", "Outdoor air.")

    def test_syntax_error_returns_none(self, tmp_path):
        """A file with a syntax error should return None, not crash."""
        py_file = tmp_path / "broken.py"
        py_file.write_text("class Broken(:\n    pass")
        module = extract_module(py_file, "pkg", skip_methods=[])
        assert module is None

    def test_empty_module_returns_none(self, tmp_path):
        """A module with no public classes should return None."""
        py_file = tmp_path / "empty.py"
        py_file.write_text('"""Empty module."""\n\ndef helper():\n    pass\n')
        module = extract_module(py_file, "pkg", skip_methods=[])
        assert module is None

    def test_missing_docstrings_still_work(self, tmp_path):
        """Classes without docstrings should still be extracted."""
        source = textwrap.dedent("""\
            class Bare(object):
                def __init__(self):
                    self.x = 1.0
                def do_thing(self):
                    pass
        """)
        py_file = tmp_path / "bare.py"
        py_file.write_text(source)
        module = extract_module(py_file, "pkg", skip_methods=[])
        assert module is not None
        assert module.classes[0].name == "Bare"
        assert module.classes[0].docstring == ""
        assert module.classes[0].attributes[0].name == "x"
        assert module.classes[0].attributes[0].type_str == "float"


# -----------------------------------------------------------------------
# Full render round-trip
# -----------------------------------------------------------------------

class TestFullRoundTrip:
    """End-to-end: fixture source → extract → render → check markdown."""

    def test_render_output(self, tmp_path):
        source = textwrap.dedent('''\
            """Test module."""

            class Widget(object):
                """A widget.

                Attributes:
                    size (float): The size.
                """

                def __init__(self):
                    self.size = 0.0  # type: float

                @property
                def volume(self):
                    # type: () -> float
                    """The volume."""
                    return 0.0

                def resize(self, factor):
                    # type: (float) -> None
                    """Resize the widget."""
                    pass
        ''')
        py_file = tmp_path / "widget.py"
        py_file.write_text(source)

        module = extract_module(py_file, "test_pkg", skip_methods=[])
        assert module is not None

        md = render_module_md(module, is_first_file=True)

        # Front-matter
        assert 'title: "widget"' in md
        assert "card_title: API Reference" in md

        # Module header
        assert "# widget" in md
        assert "Test module." in md
        assert "**Source**: `test_pkg/widget.py`" in md

        # Class
        assert "## Widget" in md
        assert "A widget." in md

        # Attributes table
        assert "| `size` | `float` | The size. |" in md

        # Properties table
        assert "| `volume` | `float` | The volume. |" in md

        # Methods
        assert "#### resize(factor)" in md
        assert "Resize the widget." in md
        assert "**Returns**: `None`" in md
