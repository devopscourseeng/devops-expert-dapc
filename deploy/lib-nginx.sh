#!/usr/bin/env bash
# Shared helpers for the nginx scripts. Do not run this file directly.
# Environments:
#   staging -> container cafe-staging      port 8100  (one container, no proxy)
#   prod    -> container cafe-prod         port 8200  (nginx proxy, splits the calls)
#              container cafe-prod-stable  port 8201  (the version customers use now)
#              container cafe-prod-canary  port 8202  (the version being released)

STAGING="cafe-staging"
STAGING_PORT="${STAGING_PORT:-8100}"
PROXY="cafe-prod"
PROXY_PORT="${PROXY_PORT:-8200}"
STABLE="cafe-prod-stable"
STABLE_PORT="${STABLE_PORT:-8201}"
CANARY="cafe-prod-canary"
CANARY_PORT="${CANARY_PORT:-8202}"
NGINX_IMAGE="${NGINX_IMAGE:-nginx:1.27-alpine}"

run() {
  if [ "${DRY_RUN:-0}" = "1" ]; then
    printf '[dry-run] %s\n' "$*"
  else
    "$@"
  fi
}

# nginx_config CANARY_WEIGHT  -> prints a full nginx.conf
# CANARY_WEIGHT is the percent of calls that go to the canary (0 to 100).
# nginx does not accept weight=0, so a slot with 0% is marked "down".
nginx_config() {
  local new="$1" stable
  stable=$((100 - new))
  local s_line n_line
  if [ "$stable" -eq 0 ]; then s_line="server host.docker.internal:$STABLE_PORT down;"
  else s_line="server host.docker.internal:$STABLE_PORT weight=$stable;"; fi
  if [ "$new" -eq 0 ]; then n_line="server host.docker.internal:$CANARY_PORT down;"
  else n_line="server host.docker.internal:$CANARY_PORT weight=$new;"; fi
  cat <<CONF
events {}
http {
  upstream cafe {
    $s_line   # stable: ${stable}%
    $n_line   # canary: ${new}%
  }
  server {
    listen 80;
    location / {
      proxy_pass http://cafe;
      proxy_next_upstream error timeout http_502 http_503;
    }
  }
}
CONF
}

# apply_config CANARY_WEIGHT -> checks the config inside the proxy, then reloads nginx.
# The config goes in through stdin, so there are no file paths to get wrong on Windows.
apply_config() {
  local new="$1"
  if [ "${DRY_RUN:-0}" = "1" ]; then
    printf '[dry-run] send this config to %s, test it and reload nginx:\n' "$PROXY"
    nginx_config "$new"
    return 0
  fi
  nginx_config "$new" | docker exec -i "$PROXY" sh -c \
    'cat > /tmp/cafe.conf && nginx -t -c /tmp/cafe.conf && cp /tmp/cafe.conf /etc/nginx/nginx.conf && nginx -s reload'
}
