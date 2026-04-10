#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_PATHS = [
    "AGENTS.md",
    "ARCHITECTURE.md",
    "docs/DESIGN.md",
    "docs/FRONTEND.md",
    "docs/PLANS.md",
    "docs/PRODUCT_SENSE.md",
    "docs/QUALITY_SCORE.md",
    "docs/RELIABILITY.md",
    "docs/SECURITY.md",
    "docs/design-docs/index.md",
    "docs/product-specs/index.md",
    "docs/references/index.md",
    "docs/generated/db-schema.md",
    "docs/exec-plans/tech-debt-tracker.md",
    "docs/exec-plans/active",
    "docs/exec-plans/completed",
]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Check that an agent-first repo scaffold exists.")
    parser.add_argument("repo_root", help="Repository root to check")
    parser.add_argument("--max-agents-lines", type=int, default=120, help="Maximum AGENTS.md line count")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    repo_root = Path(args.repo_root).resolve()
    findings = []

    for relative_path in REQUIRED_PATHS:
        if not (repo_root / relative_path).exists():
            findings.append(f"missing: {relative_path}")

    agents_path = repo_root / "AGENTS.md"
    if agents_path.exists():
        line_count = len(agents_path.read_text(encoding="utf-8", errors="replace").splitlines())
        if line_count > args.max_agents_lines:
            findings.append(f"AGENTS.md too long: {line_count} lines > {args.max_agents_lines}")

    if findings:
        for finding in findings:
            print(finding)
        return 1

    print("Agent repo scaffold looks valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
