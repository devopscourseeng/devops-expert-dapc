"""Summit Cafe API: a small REST API for the cafe menu."""

import re

import logging_setup
import metrics
from features import (
    ab_combo_test_enabled,
    app_version,
    scheduled_orders_enabled,
    variant_for,
)
from flask import Flask, current_app, jsonify, request
from menu import COMBO, MENU, MENU_BY_ID
from orders import create_order, get_order

PICKUP_TIME = re.compile(r"([01]\d|2[0-3]):[0-5]\d")


def ab_variant():
    """The A/B variant for this request, or None when the test is off or there is
    no ?customer= (then everything behaves exactly as without the experiment)."""
    customer = request.args.get("customer")
    if not customer or not ab_combo_test_enabled():
        return None
    return variant_for(customer)


def create_app():
    app = Flask(__name__)
    metrics.init_app(app)
    logging_setup.init_app(app)

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.get("/version")
    def version():
        return jsonify(
            {
                "version": app_version(),
                "scheduled_orders": "on" if scheduled_orders_enabled() else "off",
            }
        )

    @app.get("/menu")
    def list_menu():
        variant = ab_variant()
        if variant is None:
            return jsonify(MENU)
        metrics.AB_MENU_VIEWS.labels(variant=variant).inc()
        response = jsonify(MENU + [COMBO] if variant == "B" else MENU)
        response.headers["X-Variant"] = variant
        return response

    @app.get("/menu/<int:item_id>")
    def get_item(item_id):
        return jsonify(MENU_BY_ID[item_id])

    @app.post("/orders")
    def post_order():
        body = request.get_json(silent=True) or {}
        items = body.get("items")
        if not isinstance(items, list) or not items:
            return jsonify({"error": "items must be a non-empty list"}), 400
        for line in items:
            if (
                not isinstance(line, dict)
                or not isinstance(line.get("id"), int)
                or line.get("id") not in MENU_BY_ID
                or not isinstance(line.get("quantity"), int)
                or line["quantity"] < 1
            ):
                return jsonify({"error": "each item needs a menu id and a quantity of at least 1"}), 400
        pickup_time = None
        if scheduled_orders_enabled() and "pickup_time" in body:
            pickup_time = body["pickup_time"]
            if not isinstance(pickup_time, str) or not PICKUP_TIME.fullmatch(pickup_time):
                return jsonify({"error": "pickup_time must look like 14:30"}), 400
        order = create_order(items, pickup_time)
        metrics.ORDERS.inc()
        variant = ab_variant()
        log_fields = {"order_id": order["id"], "total": order["total"]}
        if variant is not None:
            metrics.AB_ORDERS.labels(variant=variant).inc()
            log_fields["variant"] = variant
        current_app.logger.info("order created", extra=log_fields)
        response = jsonify(order)
        if variant is not None:
            response.headers["X-Variant"] = variant
        return response, 201

    @app.get("/orders/<int:order_id>")
    def get_one_order(order_id):
        order = get_order(order_id)
        if order is None:
            return jsonify({"error": "order not found"}), 404
        return jsonify(order)

    return app


app = create_app()
