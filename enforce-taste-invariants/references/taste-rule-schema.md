# Taste Rule Schema

The rules JSON may contain:

- `file_size_limits`: list of `{ glob, max_lines, message }`
- `filename_patterns`: list of `{ glob, regex, message }`
- `forbidden_patterns`: list of `{ glob, regex, message }`

Keep every rule:
- mechanical
- scoped by file glob
- explained by a short remediation message
