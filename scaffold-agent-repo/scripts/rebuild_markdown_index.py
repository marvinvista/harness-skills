#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Rebuild a simple markdown index for a directory.")
    parser.add_argument("target_dir", help="Directory containing markdown files")
    parser.add_argument("--title", help="Index title override")
    parser.add_argument("--output", default="index.md", help="Index filename")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    target_dir = Path(args.target_dir).resolve()
    output_path = target_dir / args.output
    title = args.title or f"{target_dir.name.replace('-', ' ').title()} Index"

    entries = []
    for path in sorted(target_dir.glob("*.md")):
        if path.name == args.output:
            continue
        label = path.stem.replace("-", " ").replace("_", " ").title()
        entries.append(f"- [{label}]({path.name})")

    content = "\n".join([f"# {title}", "", *entries, ""]) if entries else f"# {title}\n\n- No entries yet.\n"
    output_path.write_text(content, encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
