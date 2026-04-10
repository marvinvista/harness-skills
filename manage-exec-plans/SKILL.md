---
name: manage-exec-plans
description: Create, update, and close repository-local execution plans for complex work, including scope, milestones, progress logs, decision logs, and next actions. Use when a task is too large for ephemeral chat planning, when work must continue across runs, or when Codex needs a durable plan artifact checked into the repo.
---

# Manage Exec Plans

## Overview

Create a checked-in execution plan when the work will outlive one prompt or one run. Keep the plan short, current, and grounded in repository state instead of speculative project-management filler.

## Workflow

1. Decide whether the task needs a durable plan.
- Stay in chat for small, local edits.
- Create a checked-in plan when the work has multiple phases, decision points, or handoffs.

2. Find the right plan location.
- Prefer updating an existing active plan before creating a new one.
- Store active plans under `docs/exec-plans/active/`.
- Store finished plans under `docs/exec-plans/completed/`.

3. Create or refresh the plan.
- Use [`scripts/init_exec_plan.py`](scripts/init_exec_plan.py) for a new file.
- Use [`references/plan-template.md`](references/plan-template.md) when writing by hand.
- Keep scope, acceptance criteria, milestones, risks, and next actions explicit.

4. Keep the plan operational during work.
- Append dated entries to the progress log.
- Append decisions instead of rewriting history.
- Update next actions before stopping so another run can resume cleanly.

5. Close the plan deliberately.
- Move completed plans with [`scripts/move_exec_plan.py`](scripts/move_exec_plan.py).
- Leave enough context in the decision log that future runs do not need to rediscover the tradeoffs.

## Quality Bar

- Prefer 3-7 milestones over exhaustive micro-tasks.
- Tie claims to code, docs, tests, or artifacts that exist in the repo.
- Log uncertainty explicitly instead of hiding it in vague wording.
- Separate "out of scope" from "not started yet".

## Resources

- [`scripts/init_exec_plan.py`](scripts/init_exec_plan.py): Create a new plan from the shared template.
- [`scripts/append_decision_log.py`](scripts/append_decision_log.py): Append a dated decision entry to an existing plan.
- [`scripts/move_exec_plan.py`](scripts/move_exec_plan.py): Move a finished plan from active to completed.
- [`references/plan-template.md`](references/plan-template.md): Default plan shape.
- [`references/plan-examples.md`](references/plan-examples.md): Example requests and plan outcomes.
- [`references/decision-log-rubric.md`](references/decision-log-rubric.md): What belongs in the decision log.
- [`references/active-vs-completed.md`](references/active-vs-completed.md): Plan lifecycle rules.
