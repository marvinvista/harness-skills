#!/usr/bin/env python3
from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys


def repo_root_from_cwd() -> pathlib.Path:
    completed = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        check=True,
        capture_output=True,
        text=True,
    )
    return pathlib.Path(completed.stdout.strip())


def run_step(label: str, command: list[str], repo_root: pathlib.Path) -> None:
    print(f"==> {label}", flush=True)
    completed = subprocess.run(command, cwd=repo_root)
    if completed.returncode != 0:
        raise SystemExit(completed.returncode)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run the repo-wide validation harness for the Harness Skills project."
    )
    parser.add_argument(
        "--enforce-public-commit-email",
        action="store_true",
        help="Require repo-local git user.email to use a GitHub noreply address.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    repo_root = repo_root_from_cwd()
    python_executable = sys.executable
    safety_script = repo_root / "scripts" / "check_public_repo_safety.py"

    safety_command = [python_executable, str(safety_script)]
    if args.enforce_public_commit_email:
        safety_command.append("--check-git-email")

    run_step("public-repo-safety", safety_command, repo_root)
    print("Skill pack validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
