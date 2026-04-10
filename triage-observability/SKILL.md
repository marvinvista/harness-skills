---
name: triage-observability
description: Query logs, metrics, and traces for a local or worktree-specific app instance, check performance budgets, correlate failures, and summarize the likely cause. Use when a task depends on runtime behavior, slow paths, startup regressions, or user journeys that need observability evidence instead of code inspection alone.
---

# Triage Observability

## Overview

Use runtime evidence to narrow the problem before editing code. Prefer the observability surface closest to the symptom: logs for failures, metrics for budgets and rates, traces for slow or broken request paths.

## Workflow

1. Start from the symptom.
- Read [`references/observability-entrypoints.md`](references/observability-entrypoints.md) to choose logs, metrics, or traces first.
- Scope the investigation to one worktree, service, route, or user journey when possible.

2. Query the closest signal.
- Use [`scripts/scan_json_logs.py`](scripts/scan_json_logs.py) for structured log files.
- Use [`scripts/evaluate_metrics_budget.py`](scripts/evaluate_metrics_budget.py) to compare metrics snapshots against thresholds.
- Use [`scripts/summarize_trace_spans.py`](scripts/summarize_trace_spans.py) to flag spans that exceed a latency budget.

3. Correlate the evidence.
- Match timestamps, request IDs, trace IDs, user journeys, or service names across sources.
- Prefer one concrete failure path over broad speculation.

4. Summarize the likely cause and next action.
- State what the evidence shows.
- State what remains uncertain.
- Point to the smallest verification or fix that should come next.

## Quality Bar

- Keep the investigation narrow enough to act on.
- Distinguish "no evidence found" from "system looks healthy".
- Prefer budget violations tied to a route or operation, not just a global average.
- Preserve the exact query, file path, or threshold that led to the conclusion.

## Resources

- [`scripts/scan_json_logs.py`](scripts/scan_json_logs.py): Filter newline-delimited JSON logs by level, service, and text.
- [`scripts/evaluate_metrics_budget.py`](scripts/evaluate_metrics_budget.py): Compare metric snapshots to budget rules.
- [`scripts/summarize_trace_spans.py`](scripts/summarize_trace_spans.py): Summarize slow spans from JSON trace exports.
- [`references/observability-entrypoints.md`](references/observability-entrypoints.md): Decide which signal to inspect first.
- [`references/performance-budget-rubric.md`](references/performance-budget-rubric.md): Suggested latency and startup budget framing.
- [`references/log-query-playbook.md`](references/log-query-playbook.md): Common ways to narrow noisy logs.
- [`references/trace-triage-checklist.md`](references/trace-triage-checklist.md): Checklist for trace-led debugging.
