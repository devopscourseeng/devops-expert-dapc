#!/usr/bin/env bash
# send-traffic.sh
#
# Sends traffic to the Summit Cafe API so the Grafana panels show data.
# In a loop until Ctrl+C it calls GET /menu, GET /menu/1 and POST /orders,
# and prints one line per call with the status code. A failed call does not
# stop the loop (it shows as 000 when the API does not answer).
#
# Settings (environment variables):
#   BASE_URL  where the API is   (default: http://localhost:8000)
#   DELAY     seconds between calls (default: 0.2)
#
# Examples:
#   ./observability/send-traffic.sh
#   DELAY=1 ./observability/send-traffic.sh
#   BASE_URL=http://localhost:8200 ./observability/send-traffic.sh   # through the prod proxy
#
# Example output:
#   [traffic] GET  /menu    200
#   [traffic] GET  /menu/1  200
#   [traffic] POST /orders  201
set -euo pipefail

BASE_URL="${BASE_URL:-http://localhost:8000}"
DELAY="${DELAY:-0.2}"
ORDER='{"items":[{"id":2,"quantity":1}]}'

# call METHOD PATH [BODY] -> prints the status code, or 000 if the call failed.
call() {
  local method="$1" path="$2" body="${3:-}" code
  if [ -n "$body" ]; then
    code=$(curl -s -o /dev/null --max-time 5 -w '%{http_code}' -X "$method" \
      -H 'Content-Type: application/json' -d "$body" "$BASE_URL$path" || true)
  else
    code=$(curl -s -o /dev/null --max-time 5 -w '%{http_code}' -X "$method" "$BASE_URL$path" || true)
  fi
  printf '[traffic] %-4s %-8s %s\n' "$method" "$path" "${code:-000}"
  sleep "$DELAY"
}

echo "[traffic] Sending traffic to $BASE_URL every ${DELAY}s. Stop with Ctrl+C."
trap 'echo; echo "[traffic] Stopped."; exit 0' INT TERM

while true; do
  call GET /menu
  call GET /menu/1
  call POST /orders "$ORDER"
done
