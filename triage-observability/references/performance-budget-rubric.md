# Performance Budget Rubric

Frame budgets in user-visible terms:

- startup time
- one critical route load
- one background task
- one trace span in a critical journey

Prefer:
- explicit thresholds
- route or operation names
- one worktree or one test run worth of evidence

Avoid:
- global averages with no reproduction path
- "feels slow" conclusions without measurements
