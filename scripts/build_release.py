#!/usr/bin/env python3
"""Build and validate compact upload ZIPs for Gemini Apps and ChatGPT Skills."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
import zipfile
from pathlib import Path

SKILL_NAME = "ebook-writer"
GEMINI_MAX_BYTES = 100 * 1024 * 1024
CHATGPT_MAX_BYTES = 512 * 1024 * 1024
GEMINI_MAX_FILES = 10
CHATGPT_MAX_FILES = 20
TEXT_SUFFIXES = {".md", ".txt", ".json", ".yaml", ".yml"}


def read_source_markdown(root: Path) -> list[tuple[Path, str]]:
    files = []
    for path in sorted(root.rglob("*.md")):
        relative = path.relative_to(root)
        if ".git" in relative.parts or relative.parts[0] == "dist":
            continue
        if relative.name in {"SKILL.md", "README.md"}:
            continue
        files.append((relative, path.read_text(encoding="utf-8")))
    return files


def build_bundle(root: Path, destination: Path) -> None:
    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    sources = read_source_markdown(root)
    if "name: ebook-writer" not in skill or "description:" not in skill:
        raise ValueError("SKILL.md is missing required frontmatter.")

    appendix = [
        "# Ebook Writer Supporting Materials",
        "",
        "This file bundles the Markdown resources for upload hosts that require a small file count.",
        "Each section preserves its source path in the repository.",
        "",
    ]
    for path, content in sources:
        appendix.extend(
            [
                f"<!-- BEGIN {path} -->",
                "",
                content.rstrip(),
                "",
                f"<!-- END {path} -->",
                "",
            ]
        )

    upload_note = (
        "\n\n## Upload bundle mode\n\n"
        "When this skill is uploaded as a compact ZIP, read "
        "`supporting-materials.md` for the bundled contents of the referenced "
        "protocol, reference, checklist, and workflow files. The repository "
        "layout remains authoritative for local installations.\n"
    )
    (destination / "SKILL.md").write_text(skill.rstrip() + upload_note, encoding="utf-8")
    (destination / "supporting-materials.md").write_text(
        "\n".join(appendix), encoding="utf-8"
    )


def validate_zip(path: Path, max_bytes: int, max_files: int) -> dict[str, int]:
    size = path.stat().st_size
    if size > max_bytes:
        raise ValueError(f"{path.name} exceeds {max_bytes} bytes.")
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        if len(names) > max_files:
            raise ValueError(f"{path.name} has {len(names)} files; maximum is {max_files}.")
        if "SKILL.md" not in names:
            raise ValueError(f"{path.name} must contain SKILL.md at archive root.")
        if any(name.startswith(("/", ".", "__MACOSX/")) for name in names):
            raise ValueError(f"{path.name} contains hidden or absolute archive paths.")
        if any(Path(name).suffix.lower() not in TEXT_SUFFIXES for name in names):
            raise ValueError(f"{path.name} contains an unsupported non-text file.")
        skill = archive.read("SKILL.md").decode("utf-8")
        if not re.search(r"^name:\s*ebook-writer\s*$", skill, re.MULTILINE):
            raise ValueError(f"{path.name} has invalid skill name frontmatter.")
        if not re.search(r"^description:\s*.+$", skill, re.MULTILINE):
            raise ValueError(f"{path.name} has invalid description frontmatter.")
        return {"bytes": size, "files": len(names), "skill_lines": skill.count("\n") + 1}


def make_zip(source: Path, output: Path, name: str) -> dict[str, int]:
    archive_path = output / f"{name}.zip"
    with zipfile.ZipFile(
        archive_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for path in sorted(source.iterdir()):
            archive.write(path, arcname=path.name)
    return validate_zip(
        archive_path,
        GEMINI_MAX_BYTES if name.endswith("-gemini") else CHATGPT_MAX_BYTES,
        GEMINI_MAX_FILES if name.endswith("-gemini") else CHATGPT_MAX_FILES,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).parents[1])
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    root = args.root.resolve()
    output = (args.output or root / "dist").resolve()
    staging = output / "_staging"
    if staging.exists():
        shutil.rmtree(staging)
    output.mkdir(parents=True, exist_ok=True)
    staging.mkdir()

    try:
        build_bundle(root, staging)
        reports = {
            "gemini": make_zip(staging, output, f"{SKILL_NAME}-gemini"),
            "chatgpt": make_zip(staging, output, f"{SKILL_NAME}-chatgpt"),
        }
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        print(f"Release package validation failed: {exc}", file=sys.stderr)
        return 1
    finally:
        if staging.exists():
            shutil.rmtree(staging)

    for target, report in reports.items():
        print(
            f"{target}: {report['bytes']} bytes, {report['files']} files, "
            f"{report['skill_lines']} SKILL.md lines"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
