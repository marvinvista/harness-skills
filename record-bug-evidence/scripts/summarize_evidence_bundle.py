#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path


def list_files(path: Path) -> list[str]:
    return sorted(str(file.relative_to(path.parent)) for file in path.rglob("*") if file.is_file())


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Summarize a bug evidence bundle into markdown.")
    parser.add_argument("bundle_root", help="Bundle root directory")
    parser.add_argument("--output", help="Optional markdown output path")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = Path(args.bundle_root)
    lines = ["# Bug Evidence Summary", ""]
    for section in ("before", "after", "logs", "notes"):
        section_path = root / section
        lines.append(f"## {section.capitalize()}")
        lines.append("")
        files = list_files(section_path) if section_path.exists() else []
        lines.extend([f"- {file}" for file in files] or ["- No files found."])
        lines.append("")

    output = "\n".join(lines).rstrip() + "\n"
    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(args.output)
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
