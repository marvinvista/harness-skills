#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compare metric values against simple budget rules.")
    parser.add_argument("metrics_path", help="Path to a JSON object of metric_name -> numeric value")
    parser.add_argument("budgets_path", help="Path to a JSON object of metric_name -> max value")
    return parser


def load_json(path: str) -> dict[str, float]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def main() -> int:
    args = build_parser().parse_args()
    metrics = load_json(args.metrics_path)
    budgets = load_json(args.budgets_path)

    violations = []
    for name, budget in budgets.items():
        value = metrics.get(name)
        if value is None:
            violations.append(f"{name}: missing metric")
            continue
        if float(value) > float(budget):
            violations.append(f"{name}: {value} > {budget}")

    if violations:
        print("Budget violations:")
        for violation in violations:
            print(f"- {violation}")
        return 1

    print("All metric budgets satisfied.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
