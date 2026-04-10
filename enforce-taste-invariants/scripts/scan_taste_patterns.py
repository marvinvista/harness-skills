#!/usr/bin/env python3

from __future__ import annotations

import argparse
import fnmatch
import json
import re
from pathlib import Path


def brace_expand(pattern: str) -> list[str]:
    if "{" not in pattern or "}" not in pattern:
        return [pattern]
    prefix, rest = pattern.split("{", 1)
    body, suffix = rest.split("}", 1)
    return [f"{prefix}{option}{suffix}" for option in body.split(",")]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Scan the repo for forbidden taste patterns.")
    parser.add_argument("repo_root", help="Repository root")
    parser.add_argument("rules_path", help="Taste rules JSON path")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    repo_root = Path(args.repo_root).resolve()
    rules = json.loads(Path(args.rules_path).read_text(encoding="utf-8"))
    findings = []

    for rule in rules.get("forbidden_patterns", []):
        globs = brace_expand(rule["glob"])
        regex = re.compile(rule["regex"])
        message = rule["message"]
        for path in repo_root.rglob("*"):
            if not path.is_file():
                continue
            rel_path = str(path.relative_to(repo_root))
            if not any(fnmatch.fnmatch(rel_path, pattern) for pattern in globs):
                continue
            for line_number, line in enumerate(
                path.read_text(encoding="utf-8", errors="replace").splitlines(),
                start=1,
            ):
                if regex.search(line):
                    findings.append(f"{rel_path}:{line_number} {message}")

    for finding in findings:
        print(finding)
    return 0 if findings else 1


if __name__ == "__main__":
    raise SystemExit(main())
