#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Highlight low scores from a quality evidence JSON file.")
    parser.add_argument("evidence_path", help="Evidence JSON path")
    parser.add_argument("--threshold", type=float, default=3.0, help="Flag scores at or below this value")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    evidence = json.loads(Path(args.evidence_path).read_text(encoding="utf-8"))
    findings = []
    for section in evidence["sections"]:
        for criterion in section["criteria"]:
            score = float(criterion["score"])
            if score <= args.threshold:
                findings.append((score, section["name"], criterion["name"], criterion.get("note", "")))

    findings.sort(key=lambda item: (item[0], item[1], item[2]))
    for score, section_name, criterion_name, note in findings:
        print(f"{section_name}: {criterion_name} score={score:g} {note}".rstrip())
    return 0 if findings else 1


if __name__ == "__main__":
    raise SystemExit(main())
