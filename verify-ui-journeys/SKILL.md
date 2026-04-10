---
name: verify-ui-journeys
description: Boot an app in an isolated worktree, drive key UI journeys with browser tooling, capture snapshots or recordings, reproduce bugs, validate fixes, and summarize before-and-after evidence. Use when a task involves user-visible behavior, browser-based repro steps, or regression verification.
---

# Verify Ui Journeys

## Overview

Start from a reproducible app instance, collect evidence before changing code, and then rerun the same journey after the fix. Optimize for clear repro steps and artifact-backed verification, not just “looks good on my machine.”

## Workflow

1. Start the right app instance.
- Prefer a worktree-local or branch-local environment over a shared dev server.
- Use [`scripts/boot_worktree_app.sh`](scripts/boot_worktree_app.sh) to launch and wait for readiness when the repo does not already provide a better harness.

2. Reproduce the issue before editing.
- Identify the target route or flow from [`references/route-map.md`](references/route-map.md).
- Use known credentials from [`references/test-accounts.md`](references/test-accounts.md).
- Check [`references/known-flaky-flows.md`](references/known-flaky-flows.md) before treating instability as a product bug.

3. Capture before-and-after evidence.
- Save screenshots, DOM snapshots, or recordings for the failure state.
- Re-run the exact same journey after the fix.
- Summarize what changed and what stayed the same.

4. Validate broadly enough to trust the fix.
- Check adjacent states, not just the happy path.
- Use [`references/ui-verification-checklist.md`](references/ui-verification-checklist.md) to cover loading, errors, empty states, and navigation edges.

## Quality Bar

- Repro steps should be executable by another run.
- Evidence should show both failure and resolution when practical.
- Verification should mention the user-visible outcome, not only the DOM detail.
- Keep repo-specific routes, accounts, and flaky-flow notes current.

## Resources

- [`scripts/boot_worktree_app.sh`](scripts/boot_worktree_app.sh): Launch an app command and optionally wait for a URL to become ready.
- [`references/route-map.md`](references/route-map.md): Map routes or flows worth testing.
- [`references/test-accounts.md`](references/test-accounts.md): Store non-secret local test personas and setup notes.
- [`references/known-flaky-flows.md`](references/known-flaky-flows.md): Track flows that can fail for harness reasons.
- [`references/ui-verification-checklist.md`](references/ui-verification-checklist.md): Reusable UI verification pass.
- [`assets/journey-template.spec.ts`](assets/journey-template.spec.ts): Starter browser-journey template to copy into repo tests.
