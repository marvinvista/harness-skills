#!/usr/bin/env python3

from __future__ import annotations

import argparse
import fnmatch
import json
import re
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Scan a repo with regex-based drift patterns.")
    parser.add_argument("repo_root", help="Repository root to scan")
    parser.add_argument("patterns_path", help="JSON file containing scan patterns")
    parser.add_argument("--format", choices=("text", "json"), default="text", help="Output format")
    return parser


def load_patterns(path: str) -> list[dict]:
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise ValueError("patterns file must contain a JSON array")
    return raw


def matches_any_glob(path: str, globs: list[str]) -> bool:
    return any(fnmatch.fnmatch(path, pattern) for pattern in globs)


def main() -> int:
    args = build_parser().parse_args()
    repo_root = Path(args.repo_root).resolve()
    patterns = load_patterns(args.patterns_path)
    findings: list[dict[str, object]] = []

    for file_path in repo_root.rglob("*"):
        if not file_path.is_file():
            continue
        rel_path = str(file_path.relative_to(repo_root))
        text = file_path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        for pattern in patterns:
            globs = pattern.get("globs", ["**/*"])
            if not matches_any_glob(rel_path, globs):
                continue
            regex = re.compile(pattern["regex"])
            for line_number, line in enumerate(lines, start=1):
                if regex.search(line):
                    findings.append(
                        {
                            "id": pattern["id"],
                            "path": rel_path,
                            "line": line_number,
                            "message": pattern["message"],
                        }
                    )

    if args.format == "json":
        print(json.dumps(findings, indent=2))
        return 0 if findings else 1

    for finding in findings:
        print(f"{finding['id']}: {finding['path']}:{finding['line']} {finding['message']}")
    return 0 if findings else 1


if __name__ == "__main__":
    raise SystemExit(main())
