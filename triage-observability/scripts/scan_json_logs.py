#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Filter newline-delimited JSON logs by common fields.")
    parser.add_argument("log_path", help="Path to a newline-delimited JSON log file")
    parser.add_argument("--level", help="Only keep records whose level matches")
    parser.add_argument("--service", help="Only keep records whose service matches")
    parser.add_argument("--contains", help="Only keep records whose serialized content contains this text")
    parser.add_argument("--limit", type=int, default=20, help="Maximum number of matching records to print")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    path = Path(args.log_path)
    matches = 0

    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw_line.strip():
            continue
        try:
            record = json.loads(raw_line)
        except json.JSONDecodeError:
            continue

        if args.level and str(record.get("level")) != args.level:
            continue
        if args.service and str(record.get("service")) != args.service:
            continue
        serialized = json.dumps(record, sort_keys=True)
        if args.contains and args.contains not in serialized:
            continue

        print(f"line={line_number} {serialized}")
        matches += 1
        if matches >= args.limit:
            break

    if matches == 0:
        print("No matching log records found.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
