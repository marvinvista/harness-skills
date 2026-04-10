#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Summarize spans from a JSON array export and flag slow ones.")
    parser.add_argument("trace_path", help="Path to a JSON array of spans")
    parser.add_argument("--budget-ms", type=float, default=1000.0, help="Flag spans slower than this threshold")
    parser.add_argument("--limit", type=int, default=20, help="Maximum number of slow spans to print")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    spans = json.loads(Path(args.trace_path).read_text(encoding="utf-8"))
    if not isinstance(spans, list):
        print("trace file must contain a JSON array", file=sys.stderr)
        return 2

    slow = []
    for span in spans:
        if not isinstance(span, dict):
            continue
        duration = span.get("duration_ms")
        if duration is None:
            continue
        if float(duration) > args.budget_ms:
            slow.append(span)

    slow.sort(key=lambda span: float(span.get("duration_ms", 0.0)), reverse=True)

    if not slow:
        print("No spans exceeded the budget.")
        return 0

    print(f"Spans slower than {args.budget_ms} ms:")
    for span in slow[: args.limit]:
        name = span.get("name", "unknown-span")
        service = span.get("service", "unknown-service")
        trace_id = span.get("trace_id", "unknown-trace")
        duration = span.get("duration_ms")
        print(f"- {service} {name} trace={trace_id} duration_ms={duration}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
