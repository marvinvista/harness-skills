#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Derive deterministic local ports from a worktree path.")
    parser.add_argument("worktree_path", help="Absolute or relative worktree path")
    parser.add_argument("--base", type=int, default=3000, help="Base port")
    parser.add_argument("--count", type=int, default=3, help="Number of ports to produce")
    parser.add_argument("--step", type=int, default=1, help="Port spacing")
    parser.add_argument("--format", choices=("env", "json"), default="env", help="Output format")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    normalized = str(Path(args.worktree_path).resolve())
    digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
    offset = int(digest[:4], 16) % 500
    ports = [args.base + offset + index * args.step for index in range(args.count)]

    if args.format == "json":
        print("{")
        for index, port in enumerate(ports, start=1):
            suffix = "," if index < len(ports) else ""
            print(f'  "PORT_{index}": {port}{suffix}')
        print("}")
        return 0

    for index, port in enumerate(ports, start=1):
        print(f"PORT_{index}={port}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
