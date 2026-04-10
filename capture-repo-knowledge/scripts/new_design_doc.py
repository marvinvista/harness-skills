#!/usr/bin/env python3

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create a new dated design doc from the skill template.")
    parser.add_argument("title", help="Design doc title")
    parser.add_argument("--root", default="docs/design-docs", help="Design doc directory")
    parser.add_argument("--owner", default="unassigned", help="Document owner")
    parser.add_argument("--date", help="ISO date override, defaults to today")
    parser.add_argument("--template", help="Optional template override")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = Path(args.root)
    root.mkdir(parents=True, exist_ok=True)
    date_text = args.date or dt.date.today().isoformat()
    slug = slugify(args.title)
    template_path = Path(args.template) if args.template else Path(__file__).resolve().parents[1] / "references" / "design-doc-template.md"
    template = template_path.read_text(encoding="utf-8")

    output_path = root / f"{date_text}-{slug}.md"
    body = (
        template.replace("{{TITLE}}", args.title)
        .replace("{{DATE}}", date_text)
        .replace("{{OWNER}}", args.owner)
    )
    output_path.write_text(body, encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
