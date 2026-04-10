#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from pathlib import Path


DEFAULT_RULES = {
    "file_size_limits": [
        {"glob": "**/*.ts", "max_lines": 400, "message": "keep TS files focused"},
        {"glob": "**/*.py", "max_lines": 300, "message": "keep Python files focused"},
    ],
    "filename_patterns": [
        {"glob": "**/*.ts", "regex": r"^[a-z0-9-]+\.ts$", "message": "prefer kebab-case TypeScript filenames"},
        {"glob": "**/*.py", "regex": r"^[a-z0-9_]+\.py$", "message": "prefer snake_case Python filenames"},
    ],
    "forbidden_patterns": [
        {"glob": "**/*.{ts,tsx,js,jsx}", "regex": r"\bconsole\.log\(", "message": "prefer structured logging"},
        {"glob": "**/*.{ts,tsx}", "regex": r"@ts-ignore", "message": "avoid ignored type errors"},
    ],
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create a starter taste rules JSON file.")
    parser.add_argument("output_path", help="Where to write the rules JSON")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    output = Path(args.output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(DEFAULT_RULES, indent=2) + "\n", encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
