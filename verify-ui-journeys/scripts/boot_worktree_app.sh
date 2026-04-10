#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: boot_worktree_app.sh --cwd <dir> --command <start-command> [--url <http-url>] [--timeout <seconds>] [--log-file <path>] [--pid-file <path>]

Start an app command in the background, write logs, and optionally wait for a URL to respond.
EOF
}

cwd=""
command=""
url=""
timeout="60"
log_file="worktree-app.log"
pid_file="worktree-app.pid"

while [[ "$#" -gt 0 ]]; do
  case "$1" in
    --cwd)
      cwd="$2"
      shift 2
      ;;
    --command)
      command="$2"
      shift 2
      ;;
    --url)
      url="$2"
      shift 2
      ;;
    --timeout)
      timeout="$2"
      shift 2
      ;;
    --log-file)
      log_file="$2"
      shift 2
      ;;
    --pid-file)
      pid_file="$2"
      shift 2
      ;;
    --help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

if [[ -z "$cwd" || -z "$command" ]]; then
  usage >&2
  exit 1
fi

mkdir -p "$(dirname "$log_file")" "$(dirname "$pid_file")"

(
  cd "$cwd"
  nohup /bin/sh -lc "$command" >"$log_file" 2>&1 &
  echo $! >"$pid_file"
)

if [[ -z "$url" ]]; then
  cat "$pid_file"
  exit 0
fi

end=$((SECONDS + timeout))
while (( SECONDS < end )); do
  if curl -fsS "$url" >/dev/null 2>&1; then
    echo "ready:$url"
    exit 0
  fi
  sleep 1
done

echo "Timed out waiting for $url" >&2
exit 1
