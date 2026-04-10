#!/usr/bin/env python3

from __future__ import annotations

import argparse
import fnmatch
import json
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Check files against configured max-line limits.")
    parser.add_argument("repo_root", help="Repository root")
    parser.add_argument("rules_path", help="Taste rules JSON path")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    repo_root = Path(args.repo_root).resolve()
    rules = json.loads(Path(args.rules_path).read_text(encoding="utf-8"))
    findings = []

    for rule in rules.get("file_size_limits", []):
        glob = rule["glob"]
        max_lines = int(rule["max_lines"])
        message = rule["message"]
        for path in repo_root.rglob("*"):
            if not path.is_file():
                continue
            rel_path = str(path.relative_to(repo_root))
            if not fnmatch.fnmatch(rel_path, glob):
                continue
            line_count = len(path.read_text(encoding="utf-8", errors="replace").splitlines())
            if line_count > max_lines:
                findings.append(f"{rel_path}: {line_count} lines > {max_lines} ({message})")

    for finding in findings:
        print(finding)
    return 0 if findings else 1


if __name__ == "__main__":
    raise SystemExit(main())
