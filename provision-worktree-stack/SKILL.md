---
name: provision-worktree-stack
description: Prepare, health-check, and tear down an isolated app stack for a git worktree, including deterministic port allocation, env-file rendering, and local process cleanup. Use when a branch or worktree needs its own runnable environment so agents can test, debug, and validate changes without colliding with shared dev servers.
---

# Provision Worktree Stack

## Overview

Give each worktree a predictable local environment so agents can run and validate changes without stomping on each other. Prefer deterministic ports, explicit env files, health checks, and deliberate teardown over ad-hoc shell history.

## Workflow

1. Start from repo-local conventions.
- Read [`references/stack-layout.md`](references/stack-layout.md) and [`references/env-file-conventions.md`](references/env-file-conventions.md).
- Reuse repo-native scripts if they already solve the problem.

2. Allocate deterministic local resources.
- Use [`scripts/derive_worktree_ports.py`](scripts/derive_worktree_ports.py) to assign ports from a worktree path.
- Keep all derived values explicit in env files or command output.

3. Render worktree-local configuration.
- Use [`scripts/render_env_file.py`](scripts/render_env_file.py) to generate an env file from defaults plus worktree-specific overrides.
- Keep secrets out of checked-in files.

4. Confirm the stack is actually healthy.
- Use [`scripts/wait_for_http_health.py`](scripts/wait_for_http_health.py) to wait for HTTP endpoints.
- Apply the checks in [`references/healthcheck-rubric.md`](references/healthcheck-rubric.md) before claiming the stack is ready.

5. Tear down cleanly.
- Use [`scripts/stop_background_processes.sh`](scripts/stop_background_processes.sh) to stop tracked background processes.
- Follow [`references/teardown-checklist.md`](references/teardown-checklist.md) so worktree cleanup does not leave orphaned services behind.

## Quality Bar

- Every worktree should have stable ports and env paths.
- Readiness should mean more than "process started".
- Cleanup should be idempotent.
- Prefer one obvious setup path over many almost-equivalent scripts.

## Resources

- [`scripts/derive_worktree_ports.py`](scripts/derive_worktree_ports.py): Derive deterministic ports from a worktree path.
- [`scripts/render_env_file.py`](scripts/render_env_file.py): Render `.env`-style files from templates and overrides.
- [`scripts/wait_for_http_health.py`](scripts/wait_for_http_health.py): Wait for a local HTTP endpoint to become healthy.
- [`scripts/stop_background_processes.sh`](scripts/stop_background_processes.sh): Stop background processes from a PID manifest.
- [`references/stack-layout.md`](references/stack-layout.md): Suggested worktree stack shape.
- [`references/env-file-conventions.md`](references/env-file-conventions.md): Env-file rules for isolated stacks.
- [`references/healthcheck-rubric.md`](references/healthcheck-rubric.md): What a meaningful health check should cover.
- [`references/teardown-checklist.md`](references/teardown-checklist.md): Cleanup expectations.
