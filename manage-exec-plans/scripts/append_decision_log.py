#!/usr/bin/env python3

from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path


HEADING = "## Decision Log"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Append a dated decision entry to a plan.")
    parser.add_argument("plan_path", help="Path to the execution plan markdown file")
    parser.add_argument("message", help="Decision summary to append")
    parser.add_argument("--date", help="ISO date override, defaults to today")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    path = Path(args.plan_path)
    date_text = args.date or dt.date.today().isoformat()
    entry = f"- {date_text}: {args.message}"

    content = path.read_text(encoding="utf-8")
    if HEADING not in content:
        if not content.endswith("\n"):
            content += "\n"
        content += f"\n{HEADING}\n{entry}\n"
        path.write_text(content, encoding="utf-8")
        print(path)
        return 0

    lines = content.splitlines()
    output: list[str] = []
    inserted = False
    in_section = False

    for line in lines:
        output.append(line)
        if line.strip() == HEADING:
            in_section = True
            continue
        if in_section and line.startswith("## "):
            output.insert(len(output) - 1, entry)
            inserted = True
            in_section = False

    if in_section and not inserted:
        output.append(entry)
        inserted = True

    if not inserted:
        output.append("")
        output.append(HEADING)
        output.append(entry)

    path.write_text("\n".join(output) + "\n", encoding="utf-8")
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
