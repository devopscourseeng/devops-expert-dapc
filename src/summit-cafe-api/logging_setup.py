"""JSON logs with a request id for the summit-cafe-api.

Every log line is one JSON object with the keys time, level, service, request_id
and msg, plus any extra fields passed with extra= (for example order_id).
The request id comes from the X-Request-ID header, or a new one is created, and
it is sent back in the X-Request-ID response header. Search the logs for that
value to follow one request.

Only the standard library is used. Never log request bodies, passwords, tokens
or personal data.
"""

import json
import logging
import os
import sys
import time
import uuid
from datetime import datetime, timezone

from flask import g, has_request_context, request

SERVICE_DEFAULT = "summit-cafe-api"
REQUEST_ID_HEADER = "X-Request-ID"
SLOW_REQUEST_SECONDS = 1.0

# The attributes every LogRecord has. Anything else on a record came from extra=.
_STANDARD_ATTRS = set(vars(logging.LogRecord("", 0, "", 0, "", None, None))) | {
    "message",
    "asctime",
    "request_id",
    "service",
}


def service_name():
    return os.environ.get("SERVICE_NAME", SERVICE_DEFAULT)


class JsonFormatter(logging.Formatter):
    """One JSON object per line: time, level, service, request_id, msg and extras."""

    def format(self, record):
        entry = {
            "time": datetime.fromtimestamp(record.created, tz=timezone.utc).isoformat(),
            "level": record.levelname,
            "service": service_name(),
            "request_id": getattr(record, "request_id", "-"),
            "msg": record.getMessage(),
        }
        for key, value in vars(record).items():
            if key not in _STANDARD_ATTRS and not key.startswith("_"):
                entry[key] = value
        if record.exc_info:
            entry["error"] = self.formatException(record.exc_info)
        return json.dumps(entry, default=str)


class RequestIdFilter(logging.Filter):
    """Adds request_id to every record: the id of the current request, or "-"."""

    def filter(self, record):
        record.request_id = g.get("request_id", "-") if has_request_context() else "-"
        return True


def _configure_logger(logger):
    """One stdout handler and one filter, even when create_app() runs many times."""
    from flask.logging import default_handler

    logger.removeHandler(default_handler)
    if not any(getattr(h, "_json_logs", False) for h in logger.handlers):
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(JsonFormatter())
        handler._json_logs = True
        logger.addHandler(handler)
    if not any(isinstance(f, RequestIdFilter) for f in logger.filters):
        logger.addFilter(RequestIdFilter())
    logger.setLevel(logging.INFO)


def init_app(app):
    """Configure JSON logging on the app logger and register the request id hooks."""
    # Configure the logger before Flask creates it, so Flask does not add its
    # own plain-text handler next to ours.
    _configure_logger(logging.getLogger(app.name))
    _configure_logger(app.logger)

    @app.before_request
    def set_request_id():
        g.request_id = request.headers.get(REQUEST_ID_HEADER) or uuid.uuid4().hex
        g.log_start = time.perf_counter()

    @app.after_request
    def log_and_return_request_id(response):
        start = g.pop("log_start", None)
        if start is not None:
            duration = time.perf_counter() - start
            if duration > SLOW_REQUEST_SECONDS:
                app.logger.warning(
                    "slow request",
                    extra={"path": request.path, "duration_seconds": round(duration, 3)},
                )
        if response.status_code >= 500:
            app.logger.error(
                "request failed",
                extra={"path": request.path, "status": response.status_code},
            )
        response.headers[REQUEST_ID_HEADER] = g.get("request_id", "-")
        return response
