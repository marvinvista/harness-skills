# Drift Pattern Catalog

Common cleanup targets:

- repeated local helpers that should be shared
- unsafe casts or ignored types at internal boundaries
- copy-pasted validation or fetch code
- one-off utilities that duplicate a repo-standard abstraction
- TODOs or FIXME clusters in newly changed areas

Prefer patterns that can be found mechanically and fixed in one focused pass.
