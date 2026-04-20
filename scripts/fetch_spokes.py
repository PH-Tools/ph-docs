"""Fetch spoke docs into src/content/docs/ via sparse checkout.

Reads libraries.yml, sparse-clones each enabled spoke's /docs folder,
validates required files, and writes a build manifest.

Always exits 0 — partial builds are valid. Failures are logged and skipped.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
LIBRARIES_YML = ROOT / "libraries.yml"
CONTENT_DIR = ROOT / "src" / "content" / "docs"
MANIFEST_PATH = CONTENT_DIR / "build_manifest.json"
REQUIRED_FILES = ["index.md", "nav.yml"]


def load_libraries() -> list[dict]:
    with open(LIBRARIES_YML) as f:
        data = yaml.safe_load(f)
    return data.get("libraries", [])


def sparse_clone(repo: str, branch: str, docs_path: str, dest: Path) -> None:
    """Sparse-clone a single spoke's docs folder into dest."""
    url = f"https://github.com/{repo}.git"
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp) / "repo"
        subprocess.run(
            [
                "git", "clone",
                "--filter=blob:none",
                "--sparse",
                "--depth", "1",
                "--branch", branch,
                url,
                str(tmp_path),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        subprocess.run(
            ["git", "sparse-checkout", "set", docs_path],
            cwd=tmp_path,
            check=True,
            capture_output=True,
            text=True,
        )

        src = tmp_path / docs_path
        if not src.is_dir():
            raise FileNotFoundError(f"{docs_path} not found in {repo}")

        # Copy docs into destination, replacing any previous content
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(src, dest)


def validate_required(dest: Path) -> None:
    """Check that required files exist in the cloned docs."""
    missing = [f for f in REQUIRED_FILES if not (dest / f).exists()]
    if missing:
        raise FileNotFoundError(f"Missing required files: {', '.join(missing)}")


def main() -> None:
    libraries = load_libraries()
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)

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
        dest = CONTENT_DIR / lib_id

        try:
            print(f"[FETCH] {lib_id} from {repo} ({branch})...")
            sparse_clone(repo, branch, docs_path, dest)
            validate_required(dest)
            succeeded.append(lib_id)
            print(f"[OK]    {lib_id}")
        except Exception as e:
            skipped.append({"id": lib_id, "reason": str(e)})
            print(f"[SKIP]  {lib_id}: {e}")
            # Clean up partial clone
            if dest.exists():
                shutil.rmtree(dest)

    manifest = {"succeeded": succeeded, "skipped": skipped}
    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"\nBuild manifest: {len(succeeded)} succeeded, {len(skipped)} skipped")


if __name__ == "__main__":
    main()
