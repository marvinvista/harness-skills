#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Write a markdown repro note for a bug evidence bundle.")
    parser.add_argument("output_path", help="Path to the markdown note")
    parser.add_argument("--title", required=True, help="Bug title")
    parser.add_argument("--expected", required=True, help="Expected behavior")
    parser.add_argument("--actual", required=True, help="Actual behavior")
    parser.add_argument("--steps", action="append", default=[], help="Repeatable repro step")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    lines = [
        f"# {args.title}",
        "",
        "## Expected",
        "",
        args.expected,
        "",
        "## Actual",
        "",
        args.actual,
        "",
        "## Steps To Reproduce",
        "",
    ]
    lines.extend([f"- {step}" for step in args.steps] or ["- Add repro steps here."])
    Path(args.output_path).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(args.output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
