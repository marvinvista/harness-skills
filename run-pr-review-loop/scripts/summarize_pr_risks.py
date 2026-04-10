#!/usr/bin/env python3

from __future__ import annotations

import argparse
import subprocess
import sys
from collections import Counter


def run_git(args: list[str]) -> str:
    completed = subprocess.run(
        ["git", *args],
        check=True,
        text=True,
        capture_output=True,
    )
    return completed.stdout


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Summarize high-level risk signals in the current git diff.")
    parser.add_argument(
        "--base",
        help="Optional base ref. When omitted, inspect the working tree with git status --short.",
    )
    return parser


def load_rows(base: str | None) -> list[tuple[str, str]]:
    if base:
        output = run_git(["diff", "--name-status", "--find-renames", f"{base}...HEAD"])
    else:
        output = run_git(["status", "--short"])

    rows = []
    for raw_line in output.splitlines():
        parts = raw_line.split(maxsplit=1)
        if len(parts) != 2:
            continue
        rows.append((parts[0], parts[1]))
    return rows


def main() -> int:
    args = build_parser().parse_args()
    try:
        rows = load_rows(args.base)
    except subprocess.CalledProcessError as exc:
        print(exc.stderr.strip() or str(exc), file=sys.stderr)
        return exc.returncode

    if not rows:
        print("No changed files detected.")
        return 0

    counts = Counter()
    risky_paths: list[str] = []
    for status, path in rows:
        normalized_path = path.split("->")[-1].strip()
        counts["total"] += 1
        if "test" in normalized_path.lower():
            counts["tests"] += 1
        if any(part in normalized_path for part in ("package.json", "pnpm-lock", "poetry.lock", ".github/", "Dockerfile", "schema", "migration")):
            risky_paths.append(normalized_path)
        if status.startswith("D"):
            counts["deleted"] += 1
        if normalized_path.endswith((".yml", ".yaml", ".json", ".toml")):
            counts["config"] += 1

    print("PR Risk Summary")
    print(f"- Total changed files: {counts['total']}")
    print(f"- Test-related files: {counts['tests']}")
    print(f"- Deleted files: {counts['deleted']}")
    print(f"- Config-like files: {counts['config']}")
    if risky_paths:
        print("- Review carefully:")
        for path in risky_paths:
            print(f"  - {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
