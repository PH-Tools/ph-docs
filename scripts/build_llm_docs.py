"""Copy fetched spoke docs to public/llm/ as clean, LLM-ready markdown.

Strips HTML block elements and YAML front-matter so the output is pure
markdown suitable for programmatic retrieval (WebFetch, curl, etc.).

Run after fetch_spokes.py has populated src/content/docs/.
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "src" / "content" / "docs"
LLM_DIR = ROOT / "public" / "llm"

# Files that are build artifacts or nav metadata, not prose docs
SKIP_FILES = {"nav.yml", "build_manifest.json"}


def strip_frontmatter(text: str) -> str:
    """Remove YAML front-matter (--- delimited block at start of file)."""
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    if end == -1:
        return text
    # Skip past the closing --- and any trailing blank lines
    return text[end + 4:].lstrip("\n")


def strip_html_blocks(text: str) -> str:
    """Remove HTML block elements (div, p with classes, etc.) from markdown.

    Tracks nesting depth so nested <div> blocks are fully removed.
    Preserves inline HTML and non-block elements.
    """
    lines = text.split("\n")
    result: list[str] = []
    depth = 0

    for line in lines:
        stripped = line.strip()

        # Track opening block tags
        if re.match(r"<div[\s>]", stripped) or stripped == "<div>":
            depth += 1
            continue
        if stripped == "</div>":
            depth = max(0, depth - 1)
            continue

        # Skip lines inside HTML blocks
        if depth > 0:
            continue

        result.append(line)

    return "\n".join(result)


def collapse_blank_runs(text: str) -> str:
    """Collapse runs of 3+ blank lines down to 2 (one visual break)."""
    return re.sub(r"\n{4,}", "\n\n\n", text)


def process_file(src: Path, dest: Path) -> None:
    """Read a markdown file, clean it, and write to dest."""
    raw = src.read_text(encoding="utf-8")
    clean = strip_frontmatter(raw)
    clean = strip_html_blocks(clean)
    clean = collapse_blank_runs(clean)
    clean = clean.strip() + "\n"

    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(clean, encoding="utf-8")


def main() -> None:
    if not CONTENT_DIR.is_dir():
        print("[LLM] No content dir found — run fetch_spokes.py first.")
        return

    # Clean slate
    if LLM_DIR.exists():
        shutil.rmtree(LLM_DIR)

    count = 0
    for md_file in sorted(CONTENT_DIR.rglob("*.md")):
        if md_file.name in SKIP_FILES:
            continue

        # Relative path preserves lib/section structure
        rel = md_file.relative_to(CONTENT_DIR)
        dest = LLM_DIR / rel

        process_file(md_file, dest)
        count += 1
        print(f"[LLM] {rel}")

    print(f"\n[LLM] Wrote {count} clean markdown files to public/llm/")


if __name__ == "__main__":
    main()
