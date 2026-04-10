#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote


LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
IGNORED_PREFIXES = ("http://", "https://", "mailto:", "#", "app://", "plugin://")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate relative markdown links under a directory.")
    parser.add_argument("root", nargs="?", default=".", help="Directory to scan")
    return parser


def resolve_target(root: Path, source: Path, raw_target: str) -> Path | None:
    target = unquote(raw_target.split("#", 1)[0].strip())
    if not target or target.startswith(IGNORED_PREFIXES):
        return None
    if target.startswith("/"):
        return root / target.lstrip("/")
    return source.parent / target


def main() -> int:
    args = build_parser().parse_args()
    root = Path(args.root).resolve()
    failures: list[str] = []

    for markdown_file in root.rglob("*.md"):
        content = markdown_file.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(content):
            resolved = resolve_target(root, markdown_file, match.group(1))
            if resolved is None:
                continue
            if not resolved.exists():
                relative_source = markdown_file.relative_to(root)
                failures.append(f"{relative_source}: missing target {match.group(1)}")

    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1

    print(f"All markdown links resolved under {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
