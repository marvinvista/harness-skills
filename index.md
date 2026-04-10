# Skills Index

This repo contains an agent-first skill set for bootstrapping, running, and maintaining repositories where Codex does a large share of the implementation work.

Repo-wide validation: [`scripts/validate_skill_pack.py`](scripts/validate_skill_pack.py)

## Start Here

- New repo or migration: [scaffold-agent-repo](scaffold-agent-repo/SKILL.md)
- Large multi-step change: [manage-exec-plans](manage-exec-plans/SKILL.md)
- Browser-visible bug or regression: [verify-ui-journeys](verify-ui-journeys/SKILL.md)
- Runtime failure or performance regression: [triage-observability](triage-observability/SKILL.md)
- Repeated cleanup or quality work: [clean-agent-drift](clean-agent-drift/SKILL.md), [update-quality-grades](update-quality-grades/SKILL.md)

## Bootstrap And Knowledge

- [scaffold-agent-repo](scaffold-agent-repo/SKILL.md): Bootstrap a new or early-stage repository for agent-first development with a short `AGENTS.md`, indexed docs, execution-plan folders, and starter architecture, quality, reliability, and security docs.
- [capture-repo-knowledge](capture-repo-knowledge/SKILL.md): Turn external or tacit project knowledge into repository-local artifacts such as ADRs, design docs, product specs, and reference notes.
- [garden-repo-docs](garden-repo-docs/SKILL.md): Audit repository documentation for staleness, broken cross-links, missing indexes, and mismatches with current code behavior.
- [manage-exec-plans](manage-exec-plans/SKILL.md): Create, update, and close repository-local execution plans for complex work, including scope, milestones, progress logs, decision logs, and next actions.

## Runtime And Delivery

- [provision-worktree-stack](provision-worktree-stack/SKILL.md): Prepare, health-check, and tear down an isolated app stack for a git worktree, including deterministic port allocation, env-file rendering, and local process cleanup.
- [verify-ui-journeys](verify-ui-journeys/SKILL.md): Boot an app in an isolated worktree, drive key UI journeys with browser tooling, capture snapshots or recordings, reproduce bugs, validate fixes, and summarize before-and-after evidence.
- [record-bug-evidence](record-bug-evidence/SKILL.md): Create a before-and-after evidence bundle for a bug, including repro notes, artifact manifests, and summary markdown.
- [triage-observability](triage-observability/SKILL.md): Query logs, metrics, and traces for a local or worktree-specific app instance, check performance budgets, correlate failures, and summarize the likely cause.
- [run-pr-review-loop](run-pr-review-loop/SKILL.md): Drive a pull request through an agent-first review loop by self-reviewing diffs, gathering additional review feedback, applying fixes, responding to comments, rerunning validations, and repeating until the PR is ready or human judgment is required.

## Guardrails And Cleanup

- [enforce-layered-architecture](enforce-layered-architecture/SKILL.md): Check a repository for dependency-direction and layering violations, scaffold or tighten structural rules, and summarize boundary failures that should become mechanical checks.
- [enforce-taste-invariants](enforce-taste-invariants/SKILL.md): Enforce agreed mechanical style rules such as structured logging, file-size limits, filename conventions, and banned patterns, then summarize violations that should become lint checks.
- [clean-agent-drift](clean-agent-drift/SKILL.md): Scan a repository for repeated agent-written drift patterns such as duplicated snippets, unsafe boundary shortcuts, and one-off abstractions, then group them into small cleanup batches.
- [update-quality-grades](update-quality-grades/SKILL.md): Score repository domains or architectural layers against a defined quality rubric, render a quality report, and highlight the weakest areas for follow-up work.

## Suggested Flows

- New repo setup:
  [scaffold-agent-repo](scaffold-agent-repo/SKILL.md) ->
  [capture-repo-knowledge](capture-repo-knowledge/SKILL.md) ->
  [manage-exec-plans](manage-exec-plans/SKILL.md)

- Bug-to-proof loop:
  [provision-worktree-stack](provision-worktree-stack/SKILL.md) ->
  [verify-ui-journeys](verify-ui-journeys/SKILL.md) ->
  [record-bug-evidence](record-bug-evidence/SKILL.md) ->
  [run-pr-review-loop](run-pr-review-loop/SKILL.md)

- Continuous quality loop:
  [triage-observability](triage-observability/SKILL.md) ->
  [clean-agent-drift](clean-agent-drift/SKILL.md) ->
  [enforce-layered-architecture](enforce-layered-architecture/SKILL.md) ->
  [enforce-taste-invariants](enforce-taste-invariants/SKILL.md) ->
  [update-quality-grades](update-quality-grades/SKILL.md)
