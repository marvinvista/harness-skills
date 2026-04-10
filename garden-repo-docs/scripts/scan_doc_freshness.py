#!/usr/bin/env python3

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
DATE_FIELD_RE = re.compile(r"^(reviewed_at|updated_at):\s*['\"]?([0-9]{4}-[0-9]{2}-[0-9]{2})", re.MULTILINE)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Scan markdown files for freshness metadata.")
    parser.add_argument("root", nargs="?", default=".", help="Directory to scan")
    parser.add_argument("--max-age-days", type=int, default=90, help="Consider dated docs stale after this many days")
    parser.add_argument("--fail-on-findings", action="store_true", help="Exit nonzero when findings exist")
    return parser


def extract_date(text: str) -> dt.date | None:
    frontmatter_match = FRONTMATTER_RE.match(text)
    if not frontmatter_match:
        return None
    field_match = DATE_FIELD_RE.search(frontmatter_match.group(1))
    if not field_match:
        return None
    return dt.date.fromisoformat(field_match.group(2))


def main() -> int:
    args = build_parser().parse_args()
    root = Path(args.root).resolve()
    today = dt.date.today()
    findings: list[str] = []

    for markdown_file in sorted(root.rglob("*.md")):
        date_value = extract_date(markdown_file.read_text(encoding="utf-8"))
        relative_path = markdown_file.relative_to(root)
        if date_value is None:
            findings.append(f"{relative_path}: missing reviewed_at/updated_at")
            continue
        age = (today - date_value).days
        if age > args.max_age_days:
            findings.append(f"{relative_path}: stale ({age} days since {date_value.isoformat()})")

    if findings:
        for finding in findings:
            print(finding)
        return 1 if args.fail_on_findings else 0

    print(f"No stale docs found under {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
