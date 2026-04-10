#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path


def normalize_block(lines: list[str]) -> str:
    return "\n".join(line.strip() for line in lines if line.strip())


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Find repeated normalized line blocks across files.")
    parser.add_argument("repo_root", help="Repository root to scan")
    parser.add_argument("--min-lines", type=int, default=4, help="Minimum block size")
    parser.add_argument("--min-chars", type=int, default=20, help="Minimum normalized block length")
    parser.add_argument("--max-results", type=int, default=20, help="Maximum duplicate groups to print")
    parser.add_argument("--format", choices=("text", "json"), default="text", help="Output format")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    repo_root = Path(args.repo_root).resolve()
    blocks: dict[str, list[dict[str, object]]] = defaultdict(list)

    for file_path in repo_root.rglob("*"):
        if not file_path.is_file() or file_path.suffix in {".png", ".jpg", ".jpeg", ".gif", ".svg"}:
            continue
        lines = file_path.read_text(encoding="utf-8", errors="replace").splitlines()
        for start in range(0, max(0, len(lines) - args.min_lines + 1)):
            block = normalize_block(lines[start : start + args.min_lines])
            if len(block) < args.min_chars:
                continue
            fingerprint = hashlib.sha1(block.encode("utf-8")).hexdigest()
            blocks[fingerprint].append(
                {
                    "path": str(file_path.relative_to(repo_root)),
                    "line": start + 1,
                    "preview": block[:160],
                }
            )

    duplicates = [
        {"fingerprint": key, "occurrences": value}
        for key, value in blocks.items()
        if len(value) > 1
    ]
    duplicates.sort(key=lambda item: len(item["occurrences"]), reverse=True)
    duplicates = duplicates[: args.max_results]

    if args.format == "json":
        print(json.dumps(duplicates, indent=2))
        return 0 if duplicates else 1

    for group in duplicates:
        print(f"duplicate-group {group['fingerprint']} count={len(group['occurrences'])}")
        for occurrence in group["occurrences"]:
            print(f"  - {occurrence['path']}:{occurrence['line']} {occurrence['preview']}")
    return 0 if duplicates else 1


if __name__ == "__main__":
    raise SystemExit(main())
