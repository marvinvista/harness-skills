#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create a standard bug evidence bundle directory.")
    parser.add_argument("bundle_root", help="Path to the bundle root")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = Path(args.bundle_root)
    for relative in ("before", "after", "logs", "notes"):
        (root / relative).mkdir(parents=True, exist_ok=True)
    manifest = root / "notes" / "manifest.md"
    if not manifest.exists():
        manifest.write_text("# Evidence Manifest\n\n", encoding="utf-8")
    print(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
