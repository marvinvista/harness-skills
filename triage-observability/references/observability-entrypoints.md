# Observability Entrypoints

Choose the first signal by the symptom:

- Errors, crashes, unexpected branches:
  Start with logs.
- Slow requests, degraded startup, SLO regressions:
  Start with metrics.
- One bad journey, one slow endpoint, or one broken request path:
  Start with traces.

Then correlate across the other signals only after you have one concrete lead.
