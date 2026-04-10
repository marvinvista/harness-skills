#!/usr/bin/env bash
set -euo pipefail

if [[ "$#" -eq 0 || "${1:-}" == "--help" ]]; then
  cat <<'EOF'
Usage: rerun_validation_suite.sh "command 1" "command 2" ...

Run a sequence of validation commands in order and stop on the first failure.
Example:
  rerun_validation_suite.sh "npm run lint" "npm test"
EOF
  exit 0
fi

for command in "$@"; do
  echo "==> $command"
  /bin/sh -lc "$command"
done
