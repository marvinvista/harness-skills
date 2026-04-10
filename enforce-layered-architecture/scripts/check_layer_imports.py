#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


IMPORT_RE = re.compile(
    r"^\s*(?:from\s+([A-Za-z0-9_./-]+)\s+import|import\s+([A-Za-z0-9_./-]+))",
    re.MULTILINE,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Check imports against a simple layered architecture rule file.")
    parser.add_argument("repo_root", help="Repository root to scan")
    parser.add_argument("rules_path", help="Path to the architecture rules JSON file")
    return parser


def load_rules(path: str) -> dict:
    rules = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(rules, dict):
        raise ValueError("rules file must contain a JSON object")
    return rules


def detect_layer(rel_path: str, rules: dict) -> str | None:
    for layer_name, prefixes in rules["layers"].items():
        for prefix in prefixes:
            if rel_path.startswith(prefix):
                return layer_name
    return None


def normalize_import(raw_import: str) -> str:
    if "/" in raw_import:
        return raw_import.lstrip("./")
    return raw_import.replace(".", "/").lstrip("/")


def main() -> int:
    args = build_parser().parse_args()
    repo_root = Path(args.repo_root).resolve()
    rules = load_rules(args.rules_path)
    layer_order: list[str] = rules["layer_order"]
    layer_index = {name: index for index, name in enumerate(layer_order)}
    allowed_direction = rules.get("allowed_direction", "forward")
    violations: list[str] = []

    for source_path in repo_root.rglob("*"):
        if source_path.suffix not in {".py", ".ts", ".tsx", ".js", ".jsx"}:
            continue
        rel_path = str(source_path.relative_to(repo_root))
        source_layer = detect_layer(rel_path, rules)
        if source_layer is None:
            continue

        content = source_path.read_text(encoding="utf-8", errors="replace")
        for match in IMPORT_RE.finditer(content):
            raw_import = match.group(1) or match.group(2)
            target_layer = detect_layer(normalize_import(raw_import), rules)
            if target_layer is None:
                continue
            source_i = layer_index[source_layer]
            target_i = layer_index[target_layer]
            is_violation = (
                target_i < source_i if allowed_direction == "forward" else target_i > source_i
            )
            if is_violation:
                violations.append(
                    f"{rel_path}: {source_layer} cannot depend on {target_layer} via import '{raw_import}'"
                )

    if violations:
        for violation in violations:
            print(violation)
        return 1

    print("No layering violations found.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
