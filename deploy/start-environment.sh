#!/usr/bin/env bash
# start-environment.sh STABLE_VERSION
#
# Starts the practice environment:
#   cafe-stable  runs STABLE_VERSION on port 8001
#   cafe-proxy   nginx on port 8080, sends 100% of calls to cafe-stable
# The "new" slot is empty until you run deploy-to-environment.sh.
#
# Example:  ./start-environment.sh 1.1     then   curl localhost:8080/menu
# Dry run:  DRY_RUN=1 ./start-environment.sh 1.1
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib-nginx.sh
. "$HERE/lib-nginx.sh"

IMAGE="${IMAGE:-ghcr.io/devopscourseeng/devops-expert-dapc/summit-cafe-api}"
say() { printf '[start] %s\n' "$*"; }

if [ "$#" -ne 1 ] || ! [[ "$1" =~ ^[0-9]+\.[0-9]+(\.[0-9]+)?$ ]]; then
  echo "Usage: $0 STABLE_VERSION   (example: $0 1.1)" >&2
  exit 2
fi
VERSION="$1"

say "Starting cafe-stable with version $VERSION on port $STABLE_PORT"
run docker pull "$IMAGE:$VERSION"
run docker rm -f cafe-stable >/dev/null 2>&1 || true
run docker run -d --name cafe-stable --label "cafe.version=$VERSION" \
  -p "$STABLE_PORT:8000" "$IMAGE:$VERSION"

say "Starting $PROXY (nginx) on port $PROXY_PORT"
run docker rm -f "$PROXY" >/dev/null 2>&1 || true
# The proxy reaches the two slots through the host, so it works on Windows, Mac and Linux.
run docker run -d --name "$PROXY" --add-host host.docker.internal:host-gateway \
  -p "$PROXY_PORT:80" "$NGINX_IMAGE"

if [ "${DRY_RUN:-0}" != "1" ]; then sleep 2; fi
say "Sending 100% of the calls to cafe-stable"
apply_config 0

if [ "${DRY_RUN:-0}" = "1" ]; then
  say "Dry run finished. Nothing was changed."
  exit 0
fi

for i in $(seq 1 20); do
  if curl -fsS "http://localhost:$PROXY_PORT/health" >/dev/null 2>&1; then
    say "OK: http://localhost:$PROXY_PORT answers (100% stable, version $VERSION)."
    exit 0
  fi
  sleep 1
done
echo "Error: the proxy did not answer. Logs: docker logs $PROXY" >&2
exit 1
