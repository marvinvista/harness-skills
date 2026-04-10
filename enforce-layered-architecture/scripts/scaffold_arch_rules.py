#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from pathlib import Path


DEFAULT_RULES = {
    "allowed_direction": "forward",
    "layer_order": ["types", "config", "repo", "service", "runtime", "ui"],
    "layers": {
        "types": ["src/types/", "src/domains/types/"],
        "config": ["src/config/"],
        "repo": ["src/repo/"],
        "service": ["src/service/"],
        "runtime": ["src/runtime/"],
        "ui": ["src/ui/"],
    },
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create a starter architecture rules JSON file.")
    parser.add_argument("output_path", help="Where to write the rules JSON")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    output_path = Path(args.output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(DEFAULT_RULES, indent=2) + "\n", encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
