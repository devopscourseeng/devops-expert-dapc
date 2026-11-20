"""Feature toggles for the Summit Cafe API.

A toggle is an environment variable. It is read on every call, so a test can
change it and a restart with a new value is the only thing needed in production.
"""

import hashlib
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


def ab_combo_test_enabled():
    """AB_COMBO_TEST=on starts the A/B experiment with the combo (SCRUM-50). Default: off."""
    return _is_on("AB_COMBO_TEST")


def variant_for(customer_id):
    """The A/B variant of a customer: "A" (menu as today) or "B" (menu with the combo).

    SHA-256 gives the same answer on every machine and after every restart, so a
    customer always stays in the same group. Python's hash() would not: it changes
    each time the process starts.
    """
    digest = hashlib.sha256(customer_id.encode()).hexdigest()
    return "A" if int(digest, 16) % 2 == 0 else "B"
