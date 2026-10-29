#!/usr/bin/env bash
# Shared helpers for the nginx scripts. Do not run this file directly.
# Slots:  stable -> container cafe-stable on port 8001
#         new    -> container cafe-new    on port 8002  (deploy-to-environment.sh)
# Proxy:  container cafe-proxy (nginx) on port 8080 splits the traffic.

PROXY="cafe-proxy"
STABLE_PORT="${STABLE_PORT:-8001}"
NEW_PORT="${NEW_PORT:-8002}"
PROXY_PORT="${PROXY_PORT:-8080}"
NGINX_IMAGE="${NGINX_IMAGE:-nginx:1.27-alpine}"

run() {
  if [ "${DRY_RUN:-0}" = "1" ]; then
    printf '[dry-run] %s\n' "$*"
  else
    "$@"
  fi
}

# nginx_config NEW_WEIGHT  -> prints a full nginx.conf
# NEW_WEIGHT is the percent of calls that go to the new slot (0 to 100).
# nginx does not accept weight=0, so a slot with 0% is marked "down".
nginx_config() {
  local new="$1" stable
  stable=$((100 - new))
  local s_line n_line
  if [ "$stable" -eq 0 ]; then s_line="server host.docker.internal:$STABLE_PORT down;"
  else s_line="server host.docker.internal:$STABLE_PORT weight=$stable;"; fi
  if [ "$new" -eq 0 ]; then n_line="server host.docker.internal:$NEW_PORT down;"
  else n_line="server host.docker.internal:$NEW_PORT weight=$new;"; fi
  cat <<CONF
events {}
http {
  upstream cafe {
    $s_line   # stable: ${stable}%
    $n_line   # new: ${new}%
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

# apply_config NEW_WEIGHT -> checks the config inside the proxy, then reloads nginx.
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
