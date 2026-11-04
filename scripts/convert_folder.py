#!/usr/bin/env python3
"""Convert supported files in a folder to Markdown with Microsoft MarkItDown."""

from __future__ import annotations

import argparse
import importlib.util
import subprocess
import sys
from pathlib import Path

SKIP_DIRS = {".git", ".hg", ".svn", ".venv", "venv", "__pycache__", "__MACOSX", "converted"}
SKIP_FILES = {".DS_Store"}


def load_markitdown(install_missing: bool):
    if importlib.util.find_spec("markitdown") is None:
        if not install_missing:
            raise RuntimeError(
                "Microsoft MarkItDown tidak ditemukan. Pasang dengan: "
                "python -m pip install 'markitdown[all]' "
                "atau ulangi dengan --install-missing."
            )
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "markitdown[all]"]
        )
    from markitdown import MarkItDown

    return MarkItDown()


def iter_files(root: Path):
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        if path.name in SKIP_FILES or path.suffix.lower() == ".md":
            continue
        yield path


def safe_name(path: Path, root: Path) -> Path:
    rel = path.relative_to(root)
    stem = "__".join(rel.with_suffix("").parts)
    return Path(f"{stem}.md")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("-o", "--output", type=Path, default=None)
    parser.add_argument(
        "--install-missing",
        action="store_true",
        help="Install Microsoft MarkItDown when it is unavailable.",
    )
    args = parser.parse_args()

    root = args.source.expanduser().resolve()
    if not root.is_dir():
        print(f"Folder sumber tidak ditemukan atau bukan folder: {root}", file=sys.stderr)
        return 2
    output = (args.output or root / "converted").expanduser().resolve()
    if output == root:
        print("Folder output tidak boleh sama dengan folder sumber.", file=sys.stderr)
        return 2
    output.mkdir(parents=True, exist_ok=True)

    try:
        converter = load_markitdown(args.install_missing)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 3

    rows = ["# Source Manifest", "", "| Source | Output | Status | Error |", "|---|---|---|---|"]
    files = list(iter_files(root))
    for source in files:
        target = output / safe_name(source, root)
        try:
            result = converter.convert(str(source))
            target.write_text(result.markdown, encoding="utf-8")
            rows.append(f"| `{source.relative_to(root)}` | `{target.name}` | OK | — |")
        except Exception as exc:  # conversion errors must be reported, not hidden
            message = str(exc).replace("|", "\\|").replace("\n", " ")
            rows.append(f"| `{source.relative_to(root)}` | — | ERROR | {message} |")

    (output / "source-manifest.md").write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(f"Converted {len(files)} file(s) into {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
