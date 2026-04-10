---
name: clean-agent-drift
description: Scan a repository for repeated agent-written drift patterns such as duplicated snippets, unsafe boundary shortcuts, and one-off abstractions, then group them into small cleanup batches. Use when agent throughput is creating recurring "AI slop", when you want recurring cleanup work, or when review comments keep repeating the same structural complaints.
---

# Clean Agent Drift

## Overview

Treat drift cleanup like garbage collection: find the repeated pattern, batch the smallest safe refactor, and keep the cleanup PR narrow enough to review in under a minute when possible.

## Workflow

1. Start from mechanical patterns, not vague discomfort.
- Read [`references/drift-pattern-catalog.md`](references/drift-pattern-catalog.md) and [`references/golden-principles.md`](references/golden-principles.md).
- Prefer patterns you can name and count: duplicated helpers, unsafe casts, ignored types, repeated local utilities.

2. Scan the repo for repeated signals.
- Use [`scripts/scan_drift_patterns.py`](scripts/scan_drift_patterns.py) with a pattern file for cheap mechanical findings.
- Use [`scripts/find_duplicate_snippets.py`](scripts/find_duplicate_snippets.py) to spot copy-pasted blocks that should be centralized.

3. Batch findings into one cleanup story.
- Use [`scripts/summarize_drift_findings.py`](scripts/summarize_drift_findings.py) to group related findings by theme.
- Size the batch with [`references/refactor-pr-sizing.md`](references/refactor-pr-sizing.md).

4. Prefer targeted cleanup PRs over broad rewrites.
- Fix one repeated pattern class at a time.
- Update docs, lints, or helper abstractions when that prevents the drift from reappearing.

## Quality Bar

- Findings should be repeatable and countable.
- Cleanup batches should have one main thesis.
- Prefer centralizing an invariant over editing dozens of sites by hand with no guardrail.
- Treat every repeated review complaint as a candidate rule or shared abstraction.

## Resources

- [`scripts/scan_drift_patterns.py`](scripts/scan_drift_patterns.py): Regex-scan the repo with configurable drift patterns.
- [`scripts/find_duplicate_snippets.py`](scripts/find_duplicate_snippets.py): Find repeated normalized line blocks across files.
- [`scripts/summarize_drift_findings.py`](scripts/summarize_drift_findings.py): Group findings into markdown cleanup themes.
- [`references/drift-pattern-catalog.md`](references/drift-pattern-catalog.md): Common drift classes to look for.
- [`references/golden-principles.md`](references/golden-principles.md): Principles worth encoding back into the repo.
- [`references/cleanup-batch-rubric.md`](references/cleanup-batch-rubric.md): How to choose a cleanup batch.
- [`references/refactor-pr-sizing.md`](references/refactor-pr-sizing.md): Keep cleanup PRs short-lived and reviewable.
