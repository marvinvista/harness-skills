#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path


def normalize_line(line: str) -> str:
    return line.strip().lstrip("-").strip()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Convert rough meeting notes into structured markdown.")
    parser.add_argument("input_path", help="Path to a plain-text or markdown note file")
    parser.add_argument("--output", help="Optional output path; defaults to stdout")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    input_path = Path(args.input_path)
    text = input_path.read_text(encoding="utf-8")

    decisions: list[str] = []
    actions: list[str] = []
    questions: list[str] = []
    notes: list[str] = []

    for raw_line in text.splitlines():
        line = normalize_line(raw_line)
        if not line:
            continue
        lower = line.lower()
        if lower.startswith("decision:"):
            decisions.append(line.split(":", 1)[1].strip())
        elif lower.startswith("action:"):
            actions.append(line.split(":", 1)[1].strip())
        elif lower.startswith("question:"):
            questions.append(line.split(":", 1)[1].strip())
        else:
            notes.append(line)

    summary = " ".join(notes[:3]) if notes else "Summarize the meeting before checking this in."

    sections = [
        "# Structured Notes",
        "",
        "## Summary",
        "",
        summary,
        "",
        "## Decisions",
        "",
    ]
    sections.extend([f"- {item}" for item in decisions] or ["- None captured yet."])
    sections.extend(["", "## Action Items", ""])
    sections.extend([f"- {item}" for item in actions] or ["- None captured yet."])
    sections.extend(["", "## Open Questions", ""])
    sections.extend([f"- {item}" for item in questions] or ["- None captured yet."])
    sections.extend(["", "## Supporting Notes", ""])
    sections.extend([f"- {item}" for item in notes] or ["- No additional notes."])

    output = "\n".join(sections) + "\n"
    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(args.output)
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
