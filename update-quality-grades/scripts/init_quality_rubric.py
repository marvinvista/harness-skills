#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from pathlib import Path


DEFAULT_RUBRIC = {
    "sections": [
        {
            "name": "example-domain",
            "criteria": [
                {"name": "correctness", "max_score": 5, "weight": 3},
                {"name": "tests", "max_score": 5, "weight": 2},
                {"name": "docs", "max_score": 5, "weight": 1},
                {"name": "observability", "max_score": 5, "weight": 1},
            ],
        }
    ]
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create a starter quality rubric JSON file.")
    parser.add_argument("output_path", help="Path to write the rubric JSON")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    output = Path(args.output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(DEFAULT_RUBRIC, indent=2) + "\n", encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
