---
name: scaffold-agent-repo
description: Bootstrap a new or early-stage repository for agent-first development with a short AGENTS.md, an indexed docs system of record, execution-plan folders, and starter architecture, quality, reliability, and security docs. Use when starting an empty repo, when migrating away from one giant AGENTS.md, or when you need consistent agent-legible scaffolding before handing more implementation work to Codex.
---

# Scaffold Agent Repo

## Overview

Create the smallest durable scaffold that makes the repository legible to future agent runs. Keep `AGENTS.md` short, move depth into indexed docs, and lay down enough structure that plans, specs, and quality loops have an obvious home from day one.

## Workflow

1. Choose whether this is a fresh bootstrap or a migration.
- Read [`references/repo-layout.md`](references/repo-layout.md) and [`references/conversion-strategy.md`](references/conversion-strategy.md).
- Prefer adding structure incrementally rather than rewriting the whole repo at once.

2. Initialize the scaffold.
- Use [`scripts/init_agent_repo.py`](scripts/init_agent_repo.py) against the target repository root.
- Start with the default structure unless the repo already has clearly better conventions.

3. Keep `AGENTS.md` short and navigational.
- Use [`references/agents-md-guidelines.md`](references/agents-md-guidelines.md) and [`references/starter-file-purpose.md`](references/starter-file-purpose.md).
- Treat `AGENTS.md` as the map, not the encyclopedia.

4. Rebuild and verify indexes.
- Use [`scripts/rebuild_markdown_index.py`](scripts/rebuild_markdown_index.py) for `design-docs/`, `product-specs/`, or `references/` directories.
- Use [`scripts/check_agent_repo_layout.py`](scripts/check_agent_repo_layout.py) to verify the expected scaffold exists.

## Quality Bar

- `AGENTS.md` should stay short enough to fit comfortably in context.
- Docs should be indexed and discoverable.
- Execution plans, product specs, and references should each have a stable home.
- The scaffold should help future runs navigate, not create another pile of stale docs.

## Resources

- [`scripts/init_agent_repo.py`](scripts/init_agent_repo.py): Create the default agent-first repo structure and starter files.
- [`scripts/check_agent_repo_layout.py`](scripts/check_agent_repo_layout.py): Validate the required scaffold and flag oversize `AGENTS.md`.
- [`scripts/rebuild_markdown_index.py`](scripts/rebuild_markdown_index.py): Rebuild a simple `index.md` for a markdown directory.
- [`references/repo-layout.md`](references/repo-layout.md): Suggested repository tree.
- [`references/agents-md-guidelines.md`](references/agents-md-guidelines.md): Rules for a short, useful `AGENTS.md`.
- [`references/starter-file-purpose.md`](references/starter-file-purpose.md): Why each starter file exists.
- [`references/conversion-strategy.md`](references/conversion-strategy.md): How to migrate an existing repo toward this shape.
