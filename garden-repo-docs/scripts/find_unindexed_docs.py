#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote


LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+\.md(?:#[^)]+)?)\)")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Report markdown files that are not linked from any index.md file.")
    parser.add_argument("root", nargs="?", default=".", help="Directory to scan")
    parser.add_argument("--fail-on-findings", action="store_true", help="Exit nonzero when unindexed docs are found")
    return parser


def collect_index_targets(root: Path) -> set[Path]:
    targets: set[Path] = set()
    for index_file in root.rglob("index.md"):
        content = index_file.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(content):
            raw_target = unquote(match.group(1).split("#", 1)[0])
            candidate = (index_file.parent / raw_target).resolve()
            if candidate.exists():
                targets.add(candidate)
    return targets


def main() -> int:
    args = build_parser().parse_args()
    root = Path(args.root).resolve()
    indexed = collect_index_targets(root)

    findings = []
    for markdown_file in sorted(root.rglob("*.md")):
        if markdown_file.name == "index.md":
            continue
        if markdown_file.resolve() not in indexed:
            findings.append(markdown_file.relative_to(root))

    if findings:
        for path in findings:
            print(path)
        return 1 if args.fail_on_findings else 0

    print(f"No unindexed markdown files found under {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
