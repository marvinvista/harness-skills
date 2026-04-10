# Structured Logging Guidance

Good mechanical logging rules include:

- avoid `console.log` or ad hoc `print` in application code
- prefer structured fields over interpolated prose
- keep severity explicit
- log at system boundaries and error paths

If a logging preference cannot be checked mechanically, keep it out of the invariant set.
