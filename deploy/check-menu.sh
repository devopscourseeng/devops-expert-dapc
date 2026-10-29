#!/usr/bin/env bash
# check-menu.sh [CALLS]
#
# The "watch" step of a release. It calls GET /menu through the prod proxy
# (port 8200) CALLS times (default 20) and counts the status codes.
#
# Exit code 0: every call returned 200.   Exit code 1: at least one call did not.
#
# Examples:
#   ./check-menu.sh        # 20 calls
#   ./check-menu.sh 50     # 50 calls
#
# Example output (the new version is broken and gets half of the calls):
#      10 200
#      10 500
#   [check] 10 of 20 calls failed. Go back: ./deploy/set-weight.sh 0
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib-nginx.sh
. "$HERE/lib-nginx.sh"

CALLS="${1:-20}"
if ! [[ "$CALLS" =~ ^[0-9]+$ ]] || [ "$CALLS" -lt 1 ]; then
  echo "Usage: $0 [CALLS]   (a whole number, example: $0 20)" >&2
  exit 2
fi

URL="${URL:-http://localhost:$PROXY_PORT/menu}"
codes=$(for _ in $(seq 1 "$CALLS"); do
  curl -s -o /dev/null --max-time 5 -w "%{http_code}\n" "$URL" || true
done)

echo "$codes" | sort | uniq -c
failed=$(echo "$codes" | grep -vc '^200$' || true)

if [ "$failed" -eq 0 ]; then
  echo "[check] OK: all $CALLS calls returned 200."
  exit 0
fi
echo "[check] $failed of $CALLS calls failed. Go back: ./deploy/set-weight.sh 0"
exit 1
