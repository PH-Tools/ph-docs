"""Fetch spoke docs and source into local directories via sparse checkout.

Reads libraries.yml, sparse-clones each enabled spoke's /docs folder
(and optionally source packages for API doc generation), validates
required files, and writes a build manifest.

Docs land in src/content/docs/{lib-id}/.
Source stays in .cache/spokes/{lib-id}/ for generate_api_docs.py.

Always exits 0 — partial builds are valid. Failures are logged and skipped.
"""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
LIBRARIES_YML = ROOT / "libraries.yml"
CONTENT_DIR = ROOT / "src" / "content" / "docs"
CACHE_DIR = ROOT / ".cache" / "spokes"
MANIFEST_PATH = CONTENT_DIR / "build_manifest.json"
REQUIRED_FILES = ["index.md", "nav.yml"]


def load_libraries() -> list[dict]:
    with open(LIBRARIES_YML) as f:
        data = yaml.safe_load(f)
    return data.get("libraries", [])


def sparse_clone(
    repo: str,
    branch: str,
    sparse_paths: list[str],
    dest: Path,
) -> None:
    """Sparse-clone a repo into dest with the given paths."""
    url = f"https://github.com/{repo}.git"
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True, exist_ok=True)

    subprocess.run(
        [
            "git", "clone",
            "--filter=blob:none",
            "--sparse",
            "--depth", "1",
            "--branch", branch,
            url,
            str(dest),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    subprocess.run(
        ["git", "sparse-checkout", "set"] + sparse_paths,
        cwd=dest,
        check=True,
        capture_output=True,
        text=True,
    )


def copy_docs(cache_dest: Path, docs_path: str, content_dest: Path) -> None:
    """Copy docs from the cache clone into the content directory."""
    src = cache_dest / docs_path
    if not src.is_dir():
        raise FileNotFoundError(f"{docs_path} not found in clone")
    if content_dest.exists():
        shutil.rmtree(content_dest)
    shutil.copytree(src, content_dest)


def validate_required(dest: Path) -> None:
    """Check that required files exist in the cloned docs."""
    missing = [f for f in REQUIRED_FILES if not (dest / f).exists()]
    if missing:
        raise FileNotFoundError(f"Missing required files: {', '.join(missing)}")


def main() -> None:
    libraries = load_libraries()
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    succeeded: list[str] = []
    skipped: list[dict[str, str]] = []

    for lib in libraries:
        lib_id = lib["id"]
        if not lib.get("enabled", True):
            skipped.append({"id": lib_id, "reason": "disabled"})
            print(f"[SKIP] {lib_id}: disabled")
            continue

        repo = lib["repo"]
        branch = lib.get("branch", "main")
        docs_path = lib.get("docs_path", "docs/")
        source_paths = lib.get("source_paths", [])
        content_dest = CONTENT_DIR / lib_id
        cache_dest = CACHE_DIR / lib_id

        # Build list of paths to sparse-checkout
        sparse_paths = [docs_path] + source_paths

        try:
            print(f"[FETCH] {lib_id} from {repo} ({branch})...")
            sparse_clone(repo, branch, sparse_paths, cache_dest)
            copy_docs(cache_dest, docs_path, content_dest)
            validate_required(content_dest)
            succeeded.append(lib_id)
            print(f"[OK]    {lib_id}")
        except Exception as e:
            skipped.append({"id": lib_id, "reason": str(e)})
            print(f"[SKIP]  {lib_id}: {e}")
            # Clean up partial content (leave cache for debugging)
            if content_dest.exists():
                shutil.rmtree(content_dest)

    manifest = {"succeeded": succeeded, "skipped": skipped}
    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"\nBuild manifest: {len(succeeded)} succeeded, {len(skipped)} skipped")


if __name__ == "__main__":
    main()
