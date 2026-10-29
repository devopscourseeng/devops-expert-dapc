#!/usr/bin/env bash
# deploy-to-environment.sh ENVIRONMENT VERSION [--scheduled-orders on|off]
#
# Deploys one published version of the Summit Cafe API.
#
#   staging  replaces the container cafe-staging (port 8100). Test here first.
#   prod     replaces the container cafe-prod-canary (port 8202).
#            It never touches cafe-prod-stable and never changes the nginx
#            weights, so customers are not affected until you run set-weight.sh.
#
# What it does, in order:
#   1. Checks that VERSION looks like 1.2 or 1.2.3 (never "latest").
#   2. Pulls the image from GHCR.
#   3. Replaces the container and waits until /health answers.
#      If it does not answer, it stops with an error.
#
# Examples:
#   ./deploy-to-environment.sh staging 1.2
#   ./deploy-to-environment.sh prod 1.2
#   ./deploy-to-environment.sh prod 1.1          # put the last good version back
#   DRY_RUN=1 ./deploy-to-environment.sh prod 1.2   # only print the commands
#
# Feature toggle (API 1.2 and later): add --scheduled-orders on or off.
#   ./deploy-to-environment.sh staging 1.2 --scheduled-orders on    # feature on
#   ./deploy-to-environment.sh staging 1.2 --scheduled-orders off   # feature off (default)
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib-nginx.sh
. "$HERE/lib-nginx.sh"

IMAGE="${IMAGE:-ghcr.io/devopscourseeng/devops-expert-dapc/summit-cafe-api}"
TRIES=20

say() { printf '[deploy] %s\n' "$*"; }

usage() {
  echo "Usage: $0 ENVIRONMENT VERSION [--scheduled-orders on|off]" >&2
  echo "Example: $0 staging 1.2" >&2
  echo "ENVIRONMENT is staging or prod. The toggle is off unless you say on." >&2
  exit 2
}

if [ "$#" -ne 2 ] && [ "$#" -ne 4 ]; then usage; fi

ENVIRONMENT="$1"
VERSION="$2"
SCHEDULED_ORDERS="off"
if [ "$#" -eq 4 ]; then
  [ "$3" = "--scheduled-orders" ] || usage
  case "$4" in
    on|off) SCHEDULED_ORDERS="$4" ;;
    *) echo "Error: --scheduled-orders must be on or off (got: $4)." >&2; exit 2 ;;
  esac
fi

case "$ENVIRONMENT" in
  staging) CONTAINER="$STAGING"; PORT="$STAGING_PORT" ;;
  prod)    CONTAINER="$CANARY";  PORT="$CANARY_PORT" ;;
  *)
    echo "Error: ENVIRONMENT must be staging or prod (got: $ENVIRONMENT)." >&2
    exit 2
    ;;
esac

if ! [[ "$VERSION" =~ ^[0-9]+\.[0-9]+(\.[0-9]+)?$ ]]; then
  echo "Error: VERSION must be a number like 1.2 or 1.2.3 (got: $VERSION)." >&2
  echo "We do not deploy 'latest' because it changes without warning." >&2
  exit 2
fi

say "Pulling $IMAGE:$VERSION"
run docker pull "$IMAGE:$VERSION"

say "Replacing $CONTAINER with version $VERSION on port $PORT"
run docker rm -f "$CONTAINER" >/dev/null 2>&1 || true
run docker run -d --name "$CONTAINER" \
  --label "cafe.version=$VERSION" \
  --label "cafe.environment=$ENVIRONMENT" \
  -p "$PORT:8000" \
  -e "SCHEDULED_ORDERS=$SCHEDULED_ORDERS" \
  "$IMAGE:$VERSION"

if [ "${DRY_RUN:-0}" = "1" ]; then
  say "Dry run finished. Nothing was changed."
  exit 0
fi

say "Waiting for http://localhost:$PORT/health"
for i in $(seq 1 "$TRIES"); do
  if curl -fsS "http://localhost:$PORT/health" >/dev/null 2>&1; then
    say "OK: version $VERSION answers on port $PORT ($ENVIRONMENT)."
    if [ "$ENVIRONMENT" = "prod" ]; then
      say "Customers are not affected. Change the weights when you are ready."
    fi
    exit 0
  fi
  sleep 1
done

echo "Error: version $VERSION did not answer /health after $TRIES seconds." >&2
echo "Logs: docker logs $CONTAINER" >&2
echo "Go back with: ./deploy-to-environment.sh $ENVIRONMENT <last good version>" >&2
exit 1
