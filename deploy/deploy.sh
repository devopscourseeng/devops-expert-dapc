#!/usr/bin/env bash
# deploy.sh VERSION
#
# Deploys one published version of the Summit Cafe API to the "new" slot.
# It never touches the "stable" slot and never changes the nginx weights,
# so running it does not send customers to the new version.
#
# What it does, in order:
#   1. Checks that VERSION looks like 1.2 or 1.2.3 (never "latest").
#   2. Pulls the image from GHCR.
#   3. Replaces the container "cafe-new" with the new version (port 8002).
#   4. Waits until /health answers. If it does not, it stops with an error.
#
# Examples:
#   ./deploy.sh 1.2      # put version 1.2 in the new slot
#   ./deploy.sh 1.1      # put version 1.1 back in the new slot
#   DRY_RUN=1 ./deploy.sh 1.2   # only print the commands
#
# Settings (all optional):
#   IMAGE      image name without the tag
#   NEW_PORT   host port of the new slot (default 8002)
set -euo pipefail

IMAGE="${IMAGE:-ghcr.io/devopscourseeng/devops-expert-dapc/summit-cafe-api}"
NEW_PORT="${NEW_PORT:-8002}"
CONTAINER="cafe-new"
TRIES=20

say() { printf '[deploy] %s\n' "$*"; }
run() {
  if [ "${DRY_RUN:-0}" = "1" ]; then
    printf '[dry-run] %s\n' "$*"
  else
    "$@"
  fi
}

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 VERSION   (example: $0 1.2)" >&2
  exit 2
fi

VERSION="$1"
if ! [[ "$VERSION" =~ ^[0-9]+\.[0-9]+(\.[0-9]+)?$ ]]; then
  echo "Error: VERSION must be a number like 1.2 or 1.2.3 (got: $VERSION)." >&2
  echo "We do not deploy 'latest' because it changes without warning." >&2
  exit 2
fi

say "Pulling $IMAGE:$VERSION"
run docker pull "$IMAGE:$VERSION"

say "Replacing $CONTAINER with version $VERSION on port $NEW_PORT"
run docker rm -f "$CONTAINER" >/dev/null 2>&1 || true
run docker run -d --name "$CONTAINER" \
  --label "cafe.version=$VERSION" \
  -p "$NEW_PORT:8000" \
  "$IMAGE:$VERSION"

if [ "${DRY_RUN:-0}" = "1" ]; then
  say "Dry run finished. Nothing was changed."
  exit 0
fi

say "Waiting for http://localhost:$NEW_PORT/health"
for i in $(seq 1 "$TRIES"); do
  if curl -fsS "http://localhost:$NEW_PORT/health" >/dev/null 2>&1; then
    say "OK: version $VERSION answers on port $NEW_PORT."
    say "Customers are not affected. Change the weights when you are ready."
    exit 0
  fi
  sleep 1
done

echo "Error: version $VERSION did not answer /health after $TRIES seconds." >&2
echo "Logs: docker logs $CONTAINER" >&2
echo "Go back with: ./deploy.sh <last good version>" >&2
exit 1
