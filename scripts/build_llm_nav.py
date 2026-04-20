"""Generate LLM navigation files from assembled spoke content.

Reads libraries.yml + each spoke's nav.yml + page front-matter and writes:
  - public/llms.txt          (plain-text site index, llmstxt.org convention)
  - public/site-index.json   (structured JSON page catalog)
  - public/llm-instructions.md (agent onboarding file)

Run after fetch_spokes.py has populated src/content/docs/.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
LIBRARIES_YML = ROOT / "libraries.yml"
CONTENT_DIR = ROOT / "src" / "content" / "docs"
PUBLIC_DIR = ROOT / "public"
BASE_URL = "https://docs.passivehousetools.com"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_libraries() -> list[dict]:
    with open(LIBRARIES_YML) as f:
        data = yaml.safe_load(f)
    return [lib for lib in data.get("libraries", []) if lib.get("enabled", True)]


def load_nav(lib_id: str) -> list:
    nav_path = CONTENT_DIR / lib_id / "nav.yml"
    if not nav_path.exists():
        return []
    with open(nav_path) as f:
        data = yaml.safe_load(f)
    return data.get("nav", [])


def read_frontmatter(path: Path) -> dict:
    """Extract YAML front-matter from a markdown file."""
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    try:
        return yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError:
        return {}


def walk_nav(nav_items: list, lib_id: str, section: str | None = None):
    """Yield (label, path, section) for every leaf in a nav tree."""
    for item in nav_items:
        if isinstance(item, dict):
            for key, value in item.items():
                if isinstance(value, str):
                    # Leaf: {"Label": "path.md"}
                    yield key, value, section
                elif isinstance(value, list):
                    # Group: {"GroupLabel": [children]}
                    yield from walk_nav(value, lib_id, section=key)


def slug_from_path(md_path: str) -> str:
    """Convert 'reference/wufi-xml-schema.md' to 'reference/wufi-xml-schema'."""
    if md_path == "index.md":
        return ""
    return re.sub(r"\.md$", "", md_path)


# ---------------------------------------------------------------------------
# Builders
# ---------------------------------------------------------------------------

def build_page_data(libraries: list[dict]) -> list[dict]:
    """Build structured page data for all libraries."""
    lib_entries = []

    for lib in libraries:
        lib_id = lib["id"]
        nav = load_nav(lib_id)
        if not nav:
            continue

        pages = []
        for label, md_path, section in walk_nav(nav, lib_id):
            slug = slug_from_path(md_path)
            fm = read_frontmatter(CONTENT_DIR / lib_id / md_path)

            page: dict = {
                "title": fm.get("title", label),
                "path": f"/{lib_id}/{slug}/" if slug else f"/{lib_id}/",
                "raw_path": f"/llm/{lib_id}/{md_path}",
                "section": section,
            }

            # Add LLM fields if present
            for field in ("llm_purpose", "llm_use_when"):
                if field in fm:
                    page[field] = fm[field]
            if "llm_related" in fm:
                page["llm_related"] = [
                    f"/llm/{lib_id}/{rel}" for rel in fm["llm_related"]
                ]

            pages.append(page)

        lib_entries.append({
            "id": lib_id,
            "label": lib.get("label", lib_id),
            "description": lib.get("description", ""),
            "pages": pages,
        })

    return lib_entries


def write_llms_txt(lib_entries: list[dict]) -> None:
    """Write /llms.txt — plain-text site index (llmstxt.org convention)."""
    lines = [
        "# PH-Tools Documentation",
        "",
        "> Unified documentation for PH-Tools open-source libraries: Passive House",
        "> modeling, data exchange, and analysis tools for building energy performance.",
        "",
        "## Navigation",
        f"- [LLM Instructions]({BASE_URL}/llm-instructions.md)",
        f"- [Site Index (JSON)]({BASE_URL}/site-index.json)",
        f"- [Raw Markdown Files]({BASE_URL}/llm/) (all docs as clean markdown)",
        "",
    ]

    for lib in lib_entries:
        lines.append(f"## {lib['label']}")
        desc = lib["description"].strip().replace("\n", " ")
        if desc:
            lines.append(desc)
        for page in lib["pages"]:
            title = page["title"]
            raw_url = f"{BASE_URL}{page['raw_path']}"
            section_prefix = f"{page['section']}: " if page["section"] else ""
            lines.append(f"- [{section_prefix}{title}]({raw_url})")
        lines.append("")

    dest = PUBLIC_DIR / "llms.txt"
    dest.write_text("\n".join(lines), encoding="utf-8")
    print(f"[NAV] llms.txt ({len(lines)} lines)")


def write_site_index(lib_entries: list[dict]) -> None:
    """Write /site-index.json — structured JSON page catalog."""
    index = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "base_url": BASE_URL,
        "llm_nav": {
            "instructions": "/llm-instructions.md",
            "site_index": "/site-index.json",
            "llms_txt": "/llms.txt",
            "raw_markdown_root": "/llm/",
        },
        "libraries": lib_entries,
    }

    dest = PUBLIC_DIR / "site-index.json"
    dest.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    page_count = sum(len(lib["pages"]) for lib in lib_entries)
    print(f"[NAV] site-index.json ({len(lib_entries)} libraries, {page_count} pages)")


def write_llm_instructions(lib_entries: list[dict]) -> None:
    """Write /llm-instructions.md — agent onboarding file."""
    lines = [
        "# PH-Tools Documentation — LLM Navigation Guide",
        "",
        "This site hosts documentation for the PH-Tools open-source libraries.",
        "All content is sourced from library repos and rebuilt automatically on every push.",
        "",
        "## How to find content",
        "",
        "1. Fetch `/site-index.json` for a structured catalog of all pages with metadata",
        "2. Match your task against `llm_use_when` fields to find relevant pages",
        "3. Fetch the `raw_path` URL (`.md`) for each relevant page — not the HTML version",
        "",
        "## URL conventions",
        "",
        "| Type | Pattern | Example |",
        "|------|---------|---------|",
        "| HTML (for humans) | `/{lib}/{slug}/` | `" + BASE_URL + "/phx/reference/wufi-xml-schema/` |",
        "| Raw markdown (for LLMs) | `/llm/{lib}/{path}.md` | `" + BASE_URL + "/llm/phx/reference/wufi-xml-schema.md` |",
        "| Site index | `/site-index.json` | `" + BASE_URL + "/site-index.json` |",
        "| This file | `/llm-instructions.md` | `" + BASE_URL + "/llm-instructions.md` |",
        "| LLM site index | `/llms.txt` | `" + BASE_URL + "/llms.txt` |",
        "",
        "## Direct access — common tasks",
        "",
    ]

    # Build direct-access shortcuts from pages that have llm_use_when
    shortcuts = []
    for lib in lib_entries:
        for page in lib["pages"]:
            if "llm_use_when" in page:
                shortcuts.append(page)

    if shortcuts:
        for page in shortcuts:
            use_when = page["llm_use_when"]
            raw_url = f"{BASE_URL}{page['raw_path']}"
            lines.append(f"- **{use_when}**")
            lines.append(f"  `{raw_url}`")
    else:
        lines.append("No pages have `llm_use_when` metadata yet.")

    lines.extend([
        "",
        "## Available libraries",
        "",
    ])

    for lib in lib_entries:
        page_count = len(lib["pages"])
        page_word = "page" if page_count == 1 else "pages"
        lines.append(f"- **{lib['label']}** — {lib['description'].strip().replace(chr(10), ' ')} ({page_count} {page_word})")

    lines.append("")

    dest = PUBLIC_DIR / "llm-instructions.md"
    dest.write_text("\n".join(lines), encoding="utf-8")
    print(f"[NAV] llm-instructions.md ({len(shortcuts)} direct-access shortcuts)")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    if not CONTENT_DIR.is_dir():
        print("[NAV] No content dir found — run fetch_spokes.py first.")
        return

    libraries = load_libraries()
    lib_entries = build_page_data(libraries)

    if not lib_entries:
        print("[NAV] No libraries with nav data found.")
        return

    write_llms_txt(lib_entries)
    write_site_index(lib_entries)
    write_llm_instructions(lib_entries)


if __name__ == "__main__":
    main()
