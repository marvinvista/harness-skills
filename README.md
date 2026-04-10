# Harness Skills

Public runtime surface for the Harness skills pack.

This repository intentionally contains only the files a user needs to use the skills:

- `index.md`
- each exported skill's `SKILL.md`
- each exported skill's `agents/openai.yaml`
- the `scripts/`, `references/`, and `assets/` files directly linked from `SKILL.md`

The private authoring repository keeps the full source workflow and the complete commit history. This public repository has its own separate history.

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

## Export Policy

- Exported file count: `119`
- See `PUBLIC_MANIFEST.md` for the exact file list.
