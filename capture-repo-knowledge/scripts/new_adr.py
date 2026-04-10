#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
from pathlib import Path


ADR_RE = re.compile(r"^(\d{4})-")


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def next_number(root: Path) -> str:
    numbers = []
    for path in root.glob("*.md"):
        match = ADR_RE.match(path.name)
        if match:
            numbers.append(int(match.group(1)))
    return f"{(max(numbers) + 1) if numbers else 1:04d}"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create a new ADR from the skill template.")
    parser.add_argument("title", help="ADR title")
    parser.add_argument("--root", default="docs/adr", help="ADR directory")
    parser.add_argument("--template", help="Optional template override")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = Path(args.root)
    root.mkdir(parents=True, exist_ok=True)
    number = next_number(root)
    slug = slugify(args.title)
    template_path = Path(args.template) if args.template else Path(__file__).resolve().parents[1] / "references" / "adr-template.md"
    template = template_path.read_text(encoding="utf-8")

    output_path = root / f"{number}-{slug}.md"
    body = template.replace("{{NUMBER}}", number).replace("{{TITLE}}", args.title)
    output_path.write_text(body, encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
