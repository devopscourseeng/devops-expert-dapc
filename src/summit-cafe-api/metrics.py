"""Prometheus metrics for the Summit Cafe API: RED signals plus orders created.

The metrics live at module level because the registry is global: tests call
create_app() many times, and registering the same metric twice raises an error.
"""

import time

from flask import Response, g, request
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest

REQUESTS = Counter(
    "http_requests_total",
    "HTTP requests, by route template and status code.",
    ["endpoint", "status"],
)
DURATION = Histogram(
    "http_request_duration_seconds",
    "HTTP request duration in seconds, by route template.",
    ["endpoint"],
)
ORDERS = Counter("orders_total", "Orders created.")

METRICS_PATH = "/metrics"
UNMATCHED = "unmatched"


def _endpoint():
    """The route template (/menu/<int:item_id>), never the raw path, so ids
    do not create new series. Requests with no route (404, 405) are "unmatched"."""
    rule = request.url_rule
    return rule.rule if rule is not None else UNMATCHED


def init_app(app):
    """Register the request hooks and the /metrics route on the app."""

    @app.before_request
    def start_timer():
        g.metrics_start = time.perf_counter()

    # Flask also runs after_request for unhandled exceptions (as a 500 response)
    # when the app is not in testing or debug mode.
    @app.after_request
    def record(response):
        endpoint = _endpoint()
        if endpoint == METRICS_PATH:
            return response
        start = g.pop("metrics_start", None)
        if start is not None:
            DURATION.labels(endpoint=endpoint).observe(time.perf_counter() - start)
        REQUESTS.labels(endpoint=endpoint, status=str(response.status_code)).inc()
        return response

    @app.get(METRICS_PATH)
    def metrics():
        return Response(generate_latest(), content_type=CONTENT_TYPE_LATEST)
