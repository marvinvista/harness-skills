#!/usr/bin/env python3
from __future__ import annotations

import argparse
import pathlib
import re
import subprocess
import sys
from dataclasses import dataclass


TRACKED_PATH_PATTERNS = [
    (
        "tracked-secret-file",
        re.compile(
            r"(^|/)(\.env($|\.)|.*\.(pem|key|p12|pfx|mobileprovision|db|sqlite)(-|$|\.))",
            re.IGNORECASE,
        ),
        "Tracked secret or local data file",
    ),
]

EMAIL_PATTERN = re.compile(r"\b[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})\b")
PHONE_PATTERN = re.compile(
    r"(?<!\w)(?:\+\d{1,3}[\s-]?)?(?:\(?\d{2,4}\)?[\s-]){2,}\d{2,4}(?!\w)"
)
SECRET_ASSIGNMENT_PATTERN = re.compile(
    r"""(?ix)
    \b(?:api[_-]?key|access[_-]?token|auth[_-]?token|client[_-]?secret|password)\b
    \s*[:=]\s*
    ["']?[A-Za-z0-9_./+=:@-]{8,}
    """
)

CONTENT_PATTERNS = [
    (
        "private-key",
        re.compile(r"-----BEGIN (?:RSA|OPENSSH|EC|DSA|PGP) PRIVATE KEY-----"),
        "Private key material",
    ),
    (
        "aws-access-key",
        re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
        "AWS access key",
    ),
    (
        "google-api-key",
        re.compile(r"\bAIza[0-9A-Za-z\-_]{35}\b"),
        "Google API key",
    ),
    (
        "github-token",
        re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b"),
        "GitHub token",
    ),
    (
        "slack-token",
        re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b"),
        "Slack token",
    ),
    (
        "stripe-secret",
        re.compile(r"\bsk_(?:live|test)_[A-Za-z0-9]{16,}\b"),
        "Stripe secret key",
    ),
    (
        "macos-home-path",
        re.compile(r"/Users/[^/\s]+/[^/\s]+"),
        "macOS home-directory path",
    ),
    (
        "secret-assignment",
        SECRET_ASSIGNMENT_PATTERN,
        "Secret-like assignment",
    ),
]

SAFE_EMAIL_DOMAINS = {
    "example.com",
    "example.org",
    "example.net",
    "localhost",
}
@dataclass
class Finding:
    kind: str
    path: str
    line_no: int | None
    detail: str
    line: str | None = None


def run_git(repo_root: pathlib.Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(repo_root), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout


def repo_root_from_cwd() -> pathlib.Path:
    completed = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        check=True,
        capture_output=True,
        text=True,
    )
    return pathlib.Path(completed.stdout.strip())


def tracked_paths(repo_root: pathlib.Path, staged_only: bool) -> list[pathlib.Path]:
    if staged_only:
        raw = run_git(repo_root, "diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z")
    else:
        raw = run_git(repo_root, "ls-files", "-z")
    return [repo_root / path for path in raw.split("\0") if path]


def is_probably_binary(data: bytes) -> bool:
    if not data:
        return False
    return b"\0" in data


def is_safe_email(match: str) -> bool:
    _, _, domain = match.partition("@")
    return (
        domain in SAFE_EMAIL_DOMAINS
        or domain == "users.noreply.github.com"
        or domain.endswith(".users.noreply.github.com")
    )


def scan_path(path: pathlib.Path, repo_root: pathlib.Path) -> list[Finding]:
    findings: list[Finding] = []
    rel_path = path.relative_to(repo_root).as_posix()

    for kind, pattern, detail in TRACKED_PATH_PATTERNS:
        if pattern.search(rel_path):
            findings.append(Finding(kind, rel_path, None, detail))

    if not path.exists() or path.is_dir():
        return findings

    data = path.read_bytes()
    if is_probably_binary(data):
        return findings

    text = data.decode("utf-8", errors="replace")
    for line_no, line in enumerate(text.splitlines(), start=1):
        for kind, pattern, detail in CONTENT_PATTERNS:
            if rel_path == "scripts/check_public_repo_safety.py" and kind == "macos-home-path":
                continue
            if pattern.search(line):
                findings.append(Finding(kind, rel_path, line_no, detail, line.strip()))

        for match in EMAIL_PATTERN.finditer(line):
            email = match.group(0)
            if not is_safe_email(email):
                findings.append(
                    Finding("email-address", rel_path, line_no, "Personal email address", line.strip())
                )

        if PHONE_PATTERN.search(line):
            findings.append(
                Finding("phone-number", rel_path, line_no, "Phone-like value", line.strip())
            )

    return findings


def check_git_email(repo_root: pathlib.Path) -> list[Finding]:
    try:
        email = run_git(repo_root, "config", "--get", "user.email").strip()
    except subprocess.CalledProcessError:
        return [Finding("git-config", ".git/config", None, "Missing repo-local git user.email")]

    if email.endswith("@users.noreply.github.com"):
        return []

    return [
        Finding(
            "git-config",
            ".git/config",
            None,
            "Repo-local git user.email should use a GitHub noreply address",
            email,
        )
    ]


def format_finding(finding: Finding) -> str:
    location = finding.path
    if finding.line_no is not None:
        location = f"{location}:{finding.line_no}"
    message = f"{location}: {finding.detail}"
    if finding.line:
        message = f"{message} -> {finding.line}"
    return message


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan tracked repo content for secrets and personal data before publishing."
    )
    parser.add_argument(
        "--staged",
        action="store_true",
        help="Scan only staged files instead of all tracked files.",
    )
    parser.add_argument(
        "--check-git-email",
        action="store_true",
        help="Fail if repo-local git user.email is not a GitHub noreply address.",
    )
    args = parser.parse_args()

    repo_root = repo_root_from_cwd()
    findings: list[Finding] = []

    for path in tracked_paths(repo_root, staged_only=args.staged):
        findings.extend(scan_path(path, repo_root))

    if args.check_git_email:
        findings.extend(check_git_email(repo_root))

    if findings:
        print("Public repo safety check failed:", file=sys.stderr)
        for finding in findings:
            print(f"  - {format_finding(finding)}", file=sys.stderr)
        return 1

    scope = "staged files" if args.staged else "tracked files"
    print(f"Public repo safety check passed for {scope}.")
    if args.check_git_email:
        print("Repo-local git email uses a GitHub noreply address.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
