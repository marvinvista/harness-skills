# Harness Skills

Reusable skills for teams that want Codex to do meaningful implementation work inside real repositories.

These skills are most useful for engineering teams that want an agent-friendly repo shape, repeatable debugging and review loops, and lightweight guardrails that keep agent output adaptable instead of brittle.

## Who This Is For

- Teams using Codex heavily across product or infrastructure repos
- Repositories that need better docs, plan artifacts, validation loops, and reproducible debugging workflows
- Users willing to adapt templates, scripts, and checklists to their own stack instead of treating this repo as a drop-in framework

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

The goal is not to preserve these skills verbatim. The goal is to help your team reach a repo shape that your agents and humans can both navigate confidently.

## Included Skills

- `capture-repo-knowledge`: Turn external or tacit project knowledge into repository-local artifacts such as ADRs, design docs, product specs, and reference notes. Use when important decisions live in Slack, meetings, PR threads, or people’s heads and need to become legible to future agent runs.
- `clean-agent-drift`: Scan a repository for repeated agent-written drift patterns such as duplicated snippets, unsafe boundary shortcuts, and one-off abstractions, then group them into small cleanup batches. Use when agent throughput is creating recurring "AI slop", when you want recurring cleanup work, or when review comments keep repeating the same structural complaints.
- `enforce-layered-architecture`: Check a repository for dependency-direction and layering violations, scaffold or tighten structural rules, and summarize boundary failures that should become mechanical checks. Use when a codebase needs strict domain layering, provider boundaries, parse-at-the-boundary discipline, or custom lint rules that keep agent-written code from drifting.
- `enforce-taste-invariants`: Enforce agreed mechanical style rules such as structured logging, file-size limits, filename conventions, and banned patterns, then summarize violations that should become lint checks. Use when review comments keep repeating taste-level issues that are not architecture boundaries but still need consistent, automated enforcement.
- `garden-repo-docs`: Audit repository documentation for staleness, broken cross-links, missing indexes, and mismatches with current code behavior, then apply or propose targeted fixes. Use when docs may have drifted after refactors, when AGENTS.md or index files feel stale, or when the repo treats docs as the system of record.
- `manage-exec-plans`: Create, update, and close repository-local execution plans for complex work, including scope, milestones, progress logs, decision logs, and next actions. Use when a task is too large for ephemeral chat planning, when work must continue across runs, or when Codex needs a durable plan artifact checked into the repo.
- `provision-worktree-stack`: Prepare, health-check, and tear down an isolated app stack for a git worktree, including deterministic port allocation, env-file rendering, and local process cleanup. Use when a branch or worktree needs its own runnable environment so agents can test, debug, and validate changes without colliding with shared dev servers.
- `record-bug-evidence`: Create a before-and-after evidence bundle for a bug, including repro notes, artifact manifests, and summary markdown. Use when a fix needs reviewable proof, when a bug must be handed off with clear repro context, or when screenshots, recordings, logs, or traces should be packaged consistently.
- `run-pr-review-loop`: Drive a pull request through an agent-first review loop by self-reviewing diffs, gathering additional review feedback, applying fixes, responding to comments, rerunning validations, and repeating until the PR is ready or human judgment is required. Use when Codex should finish the review-feedback loop rather than stopping after the first patch.
- `scaffold-agent-repo`: Bootstrap a new or early-stage repository for agent-first development with a short AGENTS.md, an indexed docs system of record, execution-plan folders, and starter architecture, quality, reliability, and security docs. Use when starting an empty repo, when migrating away from one giant AGENTS.md, or when you need consistent agent-legible scaffolding before handing more implementation work to Codex.
- `triage-observability`: Query logs, metrics, and traces for a local or worktree-specific app instance, check performance budgets, correlate failures, and summarize the likely cause. Use when a task depends on runtime behavior, slow paths, startup regressions, or user journeys that need observability evidence instead of code inspection alone.
- `update-quality-grades`: Score repository domains or architectural layers against a defined quality rubric, render a quality report, and highlight the weakest areas for follow-up work. Use when the repo maintains a QUALITY_SCORE-style document, when cleanup work needs prioritization, or when you want a repeatable grading pass instead of ad hoc quality opinions.
- `verify-ui-journeys`: Boot an app in an isolated worktree, drive key UI journeys with browser tooling, capture snapshots or recordings, reproduce bugs, validate fixes, and summarize before-and-after evidence. Use when a task involves user-visible behavior, browser-based repro steps, or regression verification.

## Why This Repo Is Small

This public repository intentionally contains only the user-facing runtime surface:

- `index.md`
- each exported skill's `SKILL.md`
- each exported skill's `agents/openai.yaml`
- the `scripts/`, `references/`, and `assets/` files linked from `SKILL.md`

Current exported file count: `119`

See `PUBLIC_MANIFEST.md` for the exact file list. The private authoring repository keeps the broader maintenance workflow and its separate commit history.
