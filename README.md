# Harness Skills

Reusable skills for teams that want Codex to do meaningful implementation work inside real repositories.

Use this repo as a starting point for building your own internal skill pack or adapting specific skills into an existing Codex workflow.

## Start Here

1. Read [`index.md`](index.md) and choose the closest workflow to your current pain.
2. Start with one or two skills, not the whole pack.
3. Copy the skill folders you need into your own setup or use them as references for your internal skill library.
4. Rewrite the linked `references/`, `scripts/`, and `assets/` files so they match your repo layout, commands, and team conventions.

## Good First Adoption Paths

- New repo or migration: `scaffold-agent-repo` -> `capture-repo-knowledge` -> `manage-exec-plans`
- Browser-visible bug or regression: `provision-worktree-stack` -> `verify-ui-journeys` -> `record-bug-evidence`
- Cleanup and quality loop: `triage-observability` -> `clean-agent-drift` -> `enforce-layered-architecture` -> `enforce-taste-invariants` -> `update-quality-grades`

## What You Will Usually Adapt

- Repo structure assumptions such as docs folders, plan locations, and `AGENTS.md` conventions
- Validation commands, CI checks, and PR review routines
- Route maps, local test accounts, flaky-flow notes, and environment bootstrap commands
- Architecture rules, naming rules, logging conventions, and quality rubrics

See [`index.md`](index.md) for the full skill map and use [`PUBLIC_MANIFEST.md`](PUBLIC_MANIFEST.md) if you need the exact exported file list.
