#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path


def parse_env_lines(text: str) -> dict[str, str]:
    values: dict[str, str] = {}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip()
    return values


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Render an env file from a base file and inline overrides.")
    parser.add_argument("--base-file", help="Optional existing env file to read first")
    parser.add_argument("--set", action="append", default=[], metavar="KEY=VALUE", help="Override value")
    parser.add_argument("--output", required=True, help="Output env file path")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    merged: dict[str, str] = {}

    if args.base_file:
        merged.update(parse_env_lines(Path(args.base_file).read_text(encoding="utf-8")))

    for assignment in args.set:
        key, value = assignment.split("=", 1)
        merged[key] = value

    lines = [f"{key}={value}" for key, value in sorted(merged.items())]
    Path(args.output).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
