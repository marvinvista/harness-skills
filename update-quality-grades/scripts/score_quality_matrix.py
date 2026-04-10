#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from pathlib import Path


def letter_grade(percent: float) -> str:
    if percent >= 90:
        return "A"
    if percent >= 80:
        return "B"
    if percent >= 70:
        return "C"
    if percent >= 60:
        return "D"
    return "F"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Render a weighted quality score report from rubric and evidence.")
    parser.add_argument("rubric_path", help="Rubric JSON path")
    parser.add_argument("evidence_path", help="Evidence JSON path")
    parser.add_argument("--output", help="Optional output markdown path")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    rubric = json.loads(Path(args.rubric_path).read_text(encoding="utf-8"))
    evidence = json.loads(Path(args.evidence_path).read_text(encoding="utf-8"))
    evidence_map = {
        section["name"]: {criterion["name"]: criterion for criterion in section["criteria"]}
        for section in evidence["sections"]
    }

    lines = ["# Quality Score Report", ""]

    for section in rubric["sections"]:
        section_name = section["name"]
        lines.append(f"## {section_name}")
        lines.append("")
        lines.append("| Criterion | Score | Max | Weight | Note |")
        lines.append("| --- | ---: | ---: | ---: | --- |")

        weighted_total = 0.0
        weighted_max = 0.0
        for criterion in section["criteria"]:
            criterion_name = criterion["name"]
            max_score = float(criterion["max_score"])
            weight = float(criterion["weight"])
            evidence_item = evidence_map.get(section_name, {}).get(criterion_name, {})
            score = float(evidence_item.get("score", 0))
            note = evidence_item.get("note", "")
            weighted_total += score * weight
            weighted_max += max_score * weight
            lines.append(f"| {criterion_name} | {score:g} | {max_score:g} | {weight:g} | {note} |")

        percent = (weighted_total / weighted_max * 100) if weighted_max else 0.0
        lines.append("")
        lines.append(f"- Weighted score: {weighted_total:.2f} / {weighted_max:.2f}")
        lines.append(f"- Grade: {letter_grade(percent)} ({percent:.1f}%)")
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
