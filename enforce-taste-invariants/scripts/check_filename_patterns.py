#!/usr/bin/env python3

from __future__ import annotations

import argparse
import fnmatch
import json
import re
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Check repository filenames against configured regex rules.")
    parser.add_argument("repo_root", help="Repository root")
    parser.add_argument("rules_path", help="Taste rules JSON path")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    repo_root = Path(args.repo_root).resolve()
    rules = json.loads(Path(args.rules_path).read_text(encoding="utf-8"))
    findings = []

    for rule in rules.get("filename_patterns", []):
        glob = rule["glob"]
        regex = re.compile(rule["regex"])
        message = rule["message"]
        for path in repo_root.rglob("*"):
            if not path.is_file():
                continue
            rel_path = str(path.relative_to(repo_root))
            if not fnmatch.fnmatch(rel_path, glob):
                continue
            if not regex.match(path.name):
                findings.append(f"{rel_path}: {message}")

    for finding in findings:
        print(finding)
    return 0 if findings else 1


if __name__ == "__main__":
    raise SystemExit(main())
