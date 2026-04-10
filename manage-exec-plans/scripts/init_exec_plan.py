#!/usr/bin/env python3

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not slug:
        raise ValueError("title must contain at least one alphanumeric character")
    return slug


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create a new execution plan from the skill template.")
    parser.add_argument("title", help="Human-readable plan title")
    parser.add_argument("--root", default="docs/exec-plans/active", help="Directory where the plan should be created")
    parser.add_argument("--slug", help="Optional filename slug override")
    parser.add_argument("--date", help="ISO date override, defaults to today")
    parser.add_argument(
        "--template",
        help="Optional template path; defaults to ../references/plan-template.md relative to this script",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    date_text = args.date or dt.date.today().isoformat()
    slug = args.slug or slugify(args.title)
    root = Path(args.root)
    root.mkdir(parents=True, exist_ok=True)

    template_path = Path(args.template) if args.template else Path(__file__).resolve().parents[1] / "references" / "plan-template.md"
    template = template_path.read_text(encoding="utf-8")

    output_path = root / f"{date_text}-{slug}.md"
    if output_path.exists():
        parser.error(f"refusing to overwrite existing file: {output_path}")

    body = (
        template.replace("{{TITLE}}", args.title)
        .replace("{{DATE}}", date_text)
        .replace("{{SLUG}}", slug)
    )
    output_path.write_text(body, encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
