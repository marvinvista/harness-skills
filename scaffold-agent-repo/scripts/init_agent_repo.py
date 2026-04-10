#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_DIRS = [
    "docs/design-docs",
    "docs/exec-plans/active",
    "docs/exec-plans/completed",
    "docs/generated",
    "docs/product-specs",
    "docs/references",
]


def agents_md(repo_name: str) -> str:
    return f"""# AGENTS

This repository is optimized for agent legibility. Use this file as a map to the real sources of truth.

## Start Here

- Architecture map: [ARCHITECTURE.md](ARCHITECTURE.md)
- Design and product guides: [docs/DESIGN.md](docs/DESIGN.md), [docs/PRODUCT_SENSE.md](docs/PRODUCT_SENSE.md)
- Planning system: [docs/PLANS.md](docs/PLANS.md)
- Quality and operations: [docs/QUALITY_SCORE.md](docs/QUALITY_SCORE.md), [docs/RELIABILITY.md](docs/RELIABILITY.md), [docs/SECURITY.md](docs/SECURITY.md)
- Deep docs: [docs/design-docs/index.md](docs/design-docs/index.md), [docs/product-specs/index.md](docs/product-specs/index.md), [docs/references/index.md](docs/references/index.md)

## Working Rules

- Keep this file short and navigational.
- Put durable project knowledge in repo-local markdown, not only in chat or external docs.
- Use `docs/exec-plans/active/` for multi-step work that will outlive one run.
- Keep indexes and cross-links current when adding docs.
- Prefer boring, legible abstractions over clever opaque ones.

## Repo

- Name: {repo_name}
- Status: replace this with your current project stage and any critical constraints.
"""


FILES = {
    "ARCHITECTURE.md": """# Architecture

## Domains

- Describe the main business domains here.

## Layers

- Describe the allowed dependency flow here.

## Cross-Cutting Concerns

- Telemetry
- Auth
- Feature flags
""",
    "docs/DESIGN.md": """# Design

Document durable UX and system design principles here.
""",
    "docs/FRONTEND.md": """# Frontend

Document frontend conventions, shared patterns, and UI constraints here.
""",
    "docs/PLANS.md": """# Plans

- Active execution plans live in `docs/exec-plans/active/`
- Completed plans live in `docs/exec-plans/completed/`
- Technical debt tracking lives in `docs/exec-plans/tech-debt-tracker.md`
""",
    "docs/PRODUCT_SENSE.md": """# Product Sense

Capture stable product principles, acceptance criteria patterns, and user-value heuristics here.
""",
    "docs/QUALITY_SCORE.md": """# Quality Score

Track quality grades for domains or layers here.
""",
    "docs/RELIABILITY.md": """# Reliability

Document reliability expectations, SLOs, health checks, and operational assumptions here.
""",
    "docs/SECURITY.md": """# Security

Document security constraints, boundary validation rules, and sensitive data handling here.
""",
    "docs/design-docs/index.md": """# Design Docs Index

- Add design docs here and keep this index current.
""",
    "docs/product-specs/index.md": """# Product Specs Index

- Add product specs here and keep this index current.
""",
    "docs/references/index.md": """# References Index

- Add stable reference material here and keep this index current.
""",
    "docs/generated/db-schema.md": """# DB Schema

Replace this placeholder with a generated schema document or point to the generation process.
""",
    "docs/exec-plans/tech-debt-tracker.md": """# Tech Debt Tracker

- Record durable technical debt items here.
""",
    "docs/exec-plans/active/.gitkeep": "",
    "docs/exec-plans/completed/.gitkeep": "",
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Initialize an agent-first repository scaffold.")
    parser.add_argument("repo_root", help="Repository root to scaffold")
    parser.add_argument("--repo-name", help="Optional repo name override")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    return parser


def write_file(path: Path, content: str, force: bool) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        return "skipped"
    path.write_text(content, encoding="utf-8")
    return "created"


def main() -> int:
    args = build_parser().parse_args()
    repo_root = Path(args.repo_root).resolve()
    repo_root.mkdir(parents=True, exist_ok=True)
    repo_name = args.repo_name or repo_root.name

    for relative_dir in REQUIRED_DIRS:
        (repo_root / relative_dir).mkdir(parents=True, exist_ok=True)

    results: list[str] = []
    results.append(f"AGENTS.md {write_file(repo_root / 'AGENTS.md', agents_md(repo_name), args.force)}")
    for relative_path, content in FILES.items():
        status = write_file(repo_root / relative_path, content, args.force)
        results.append(f"{relative_path} {status}")

    for line in results:
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
