---
name: run-pr-review-loop
description: Drive a pull request through an agent-first review loop by self-reviewing diffs, gathering additional review feedback, applying fixes, responding to comments, rerunning validations, and repeating until the PR is ready or human judgment is required. Use when Codex should finish the review-feedback loop rather than stopping after the first patch.
---

# Run Pr Review Loop

## Overview

Treat the first patch as the start of the work, not the finish line. Keep tightening the branch until the remaining issues are judgment-heavy or the PR clearly meets the repo’s ready bar.

## Workflow

1. Self-review before asking for more feedback.
- Inspect the diff locally.
- Use [`scripts/summarize_pr_risks.py`](scripts/summarize_pr_risks.py) to surface risky areas fast.
- Check the changed paths against [`references/review-checklist.md`](references/review-checklist.md).

2. Gather external review context.
- Pull comments and review state with [`scripts/collect_review_feedback.sh`](scripts/collect_review_feedback.sh) when GitHub CLI is available.
- Separate correctness issues from taste or preference.

3. Fix, validate, and loop.
- Batch related fixes together.
- Rerun the relevant validation commands, not just the smallest local check.
- Use [`scripts/rerun_validation_suite.sh`](scripts/rerun_validation_suite.sh) for repeatable command sets.

4. Respond with evidence.
- Summarize what changed.
- Point to validation or repro evidence.
- Leave open questions only when they are real product or architecture judgments.

## Escalation Rule

Escalate when the remaining blocker is not mechanical:
- ambiguous product intent
- risky rollback tradeoffs
- incomplete external context
- disagreement about the correct behavior

## Resources

- [`scripts/summarize_pr_risks.py`](scripts/summarize_pr_risks.py): Summarize file-level risk signals in the current diff.
- [`scripts/collect_review_feedback.sh`](scripts/collect_review_feedback.sh): Pull PR comments through `gh`.
- [`scripts/rerun_validation_suite.sh`](scripts/rerun_validation_suite.sh): Re-run a sequence of validation commands.
- [`references/review-checklist.md`](references/review-checklist.md): Core review pass.
- [`references/pr-ready-criteria.md`](references/pr-ready-criteria.md): Ready-to-merge bar.
- [`references/common-regression-patterns.md`](references/common-regression-patterns.md): Typical misses to re-check.
- [`references/response-style-guide.md`](references/response-style-guide.md): How to answer review comments with signal.
