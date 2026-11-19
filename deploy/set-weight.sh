#!/usr/bin/env bash
# set-weight.sh PERCENT
#
# Sets the percent of calls in prod that go to the canary (cafe-prod-canary).
# The rest goes to cafe-prod-stable. Calls always come in through port 8200.
#
# Examples:
#   ./set-weight.sh 10    # canary: 10% canary, 90% stable
#   ./set-weight.sh 50    # half and half
#   ./set-weight.sh 100   # everyone on the canary
#   ./set-weight.sh 0     # roll back: everyone on stable
#   DRY_RUN=1 ./set-weight.sh 10   # only show the config
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib-nginx.sh
. "$HERE/lib-nginx.sh"

if [ "$#" -ne 1 ] || ! [[ "$1" =~ ^[0-9]+$ ]] || [ "$1" -gt 100 ]; then
  echo "Usage: $0 PERCENT   (a whole number from 0 to 100, example: $0 10)" >&2
  exit 2
fi
PERCENT=$((10#$1))

apply_config "$PERCENT"
if [ "${DRY_RUN:-0}" != "1" ]; then
  echo "[weight] OK: $PERCENT% of the calls go to the canary, $((100 - PERCENT))% to stable."
fi
