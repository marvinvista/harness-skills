#!/usr/bin/env bash
set -euo pipefail

if [[ "${1:-}" == "--help" ]]; then
  cat <<'EOF'
Usage: collect_review_feedback.sh [pr-selector]

Fetch PR comments for the current branch or for the provided PR selector using gh.
Examples:
  collect_review_feedback.sh
  collect_review_feedback.sh 123
  collect_review_feedback.sh https://github.com/org/repo/pull/123
EOF
  exit 0
fi

if ! command -v gh >/dev/null 2>&1; then
  echo "gh CLI is required to collect PR feedback" >&2
  exit 1
fi

selector="${1:-}"
if [[ -n "$selector" ]]; then
  gh pr view "$selector" --comments
else
  gh pr view --comments
fi
