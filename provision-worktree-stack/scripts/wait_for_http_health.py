#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys
import time
import urllib.error
import urllib.request


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Wait for an HTTP endpoint to return a healthy response.")
    parser.add_argument("url", help="URL to poll")
    parser.add_argument("--timeout", type=int, default=60, help="Seconds to wait before failing")
    parser.add_argument("--contains", help="Optional response text that must be present")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    deadline = time.time() + args.timeout

    while time.time() < deadline:
        try:
            with urllib.request.urlopen(args.url) as response:
                body = response.read().decode("utf-8", errors="replace")
                if args.contains and args.contains not in body:
                    time.sleep(1)
                    continue
                print(f"ready:{args.url}")
                return 0
        except urllib.error.URLError:
            time.sleep(1)

    print(f"Timed out waiting for {args.url}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
