"""Feature toggles for the Summit Cafe API.

A toggle is an environment variable. It is read on every call, so a test can
change it and a restart with a new value is the only thing needed in production.
"""

import os

VERSION_DEFAULT = "dev"


def _is_on(name):
    return os.environ.get(name, "off").strip().lower() in ("on", "true", "1")


def scheduled_orders_enabled():
    """SCHEDULED_ORDERS=on lets a customer choose a pickup time. Default: off."""
    return _is_on("SCHEDULED_ORDERS")


def app_version():
    """The version of the image. The publish workflow sets it from the tag."""
    return os.environ.get("APP_VERSION", VERSION_DEFAULT)
