#!/usr/bin/env python3

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Move a finished execution plan into the completed directory.")
    parser.add_argument("source", help="Path to the active execution plan")
    parser.add_argument(
        "--destination-root",
        default="docs/exec-plans/completed",
        help="Directory where completed plans live",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    source = Path(args.source)
    destination_root = Path(args.destination_root)
    destination_root.mkdir(parents=True, exist_ok=True)
    destination = destination_root / source.name

    if destination.exists():
        raise SystemExit(f"refusing to overwrite existing file: {destination}")

    shutil.move(str(source), str(destination))
    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
