---
name: update-quality-grades
description: Score repository domains or architectural layers against a defined quality rubric, render a quality report, and highlight the weakest areas for follow-up work. Use when the repo maintains a QUALITY_SCORE-style document, when cleanup work needs prioritization, or when you want a repeatable grading pass instead of ad hoc quality opinions.
---

# Update Quality Grades

## Overview

Grade the repo with a repeatable rubric, not with a vibe. Keep the scoring transparent enough that future runs can explain why a domain or layer moved up or down and what should happen next.

## Workflow

1. Choose the grading surface.
- Grade by product domain, architectural layer, or another stable partition.
- Use [`references/quality-dimensions.md`](references/quality-dimensions.md) and [`references/scoring-guidelines.md`](references/scoring-guidelines.md) to keep the rubric consistent.

2. Scaffold or load the rubric.
- Use [`scripts/init_quality_rubric.py`](scripts/init_quality_rubric.py) to create a starter rubric JSON.
- Keep criteria names and weights explicit.

3. Record evidence-based scores.
- Build a JSON evidence file with section, criterion, score, and optional note.
- Keep evidence sources grounded in repo artifacts using [`references/evidence-sources.md`](references/evidence-sources.md).

4. Render the report and extract priorities.
- Use [`scripts/score_quality_matrix.py`](scripts/score_quality_matrix.py) to produce a markdown report.
- Use [`scripts/highlight_low_scores.py`](scripts/highlight_low_scores.py) to surface the weakest sections.
- Feed those weak spots into cleanup, plan, or refactor work.

## Quality Bar

- Scores should be justified by visible evidence.
- Criteria should be stable enough to compare across runs.
- Grade changes should be explainable.
- Follow-up priorities should come from the weakest weighted areas, not the loudest recent anecdote.

## Resources

- [`scripts/init_quality_rubric.py`](scripts/init_quality_rubric.py): Create a starter rubric JSON.
- [`scripts/score_quality_matrix.py`](scripts/score_quality_matrix.py): Compute weighted scores and render a markdown report.
- [`scripts/highlight_low_scores.py`](scripts/highlight_low_scores.py): List the weakest scored sections from an evidence file.
- [`references/quality-dimensions.md`](references/quality-dimensions.md): Suggested quality dimensions.
- [`references/scoring-guidelines.md`](references/scoring-guidelines.md): How to apply the score scale consistently.
- [`references/evidence-sources.md`](references/evidence-sources.md): What kinds of repo evidence should support scores.
- [`references/follow-up-prioritization.md`](references/follow-up-prioritization.md): Turn weak grades into next actions.
