#!/usr/bin/env bash
set -euo pipefail

if [[ "$#" -ne 1 || "${1:-}" == "--help" ]]; then
  cat <<'EOF'
Usage: stop_background_processes.sh <pid-file>

Read newline-separated PIDs from the file and stop any process that is still running.
EOF
  exit 0
fi

pid_file="$1"
if [[ ! -f "$pid_file" ]]; then
  echo "PID file not found: $pid_file" >&2
  exit 1
fi

while IFS= read -r pid; do
  [[ -z "$pid" ]] && continue
  if kill -0 "$pid" >/dev/null 2>&1; then
    kill "$pid"
  fi
done < "$pid_file"
