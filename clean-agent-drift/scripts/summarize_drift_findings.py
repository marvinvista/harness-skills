#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Group drift findings by finding id into markdown.")
    parser.add_argument("findings_path", help="JSON file with drift findings")
    parser.add_argument("--output", help="Optional output markdown path")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    findings = json.loads(Path(args.findings_path).read_text(encoding="utf-8"))
    groups: dict[str, list[dict]] = defaultdict(list)
    for finding in findings:
        groups[finding["id"]].append(finding)

    lines = ["# Drift Findings Summary", ""]
    for finding_id in sorted(groups):
        items = groups[finding_id]
        lines.append(f"## {finding_id}")
        lines.append("")
        lines.append(f"- Count: {len(items)}")
        for item in items[:10]:
            lines.append(f"- {item['path']}:{item['line']} {item['message']}")
        lines.append("")

    output = "\n".join(lines).rstrip() + "\n"
    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(args.output)
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
