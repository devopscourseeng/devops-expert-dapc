"""Summit Cafe API: a small REST API for the cafe menu."""

import re

from features import app_version, scheduled_orders_enabled
from flask import Flask, jsonify, request
from menu import MENU, MENU_BY_ID
from orders import create_order, get_order

# Keep the menu in a cache, one entry for each version of the app.
MENU_CACHE = {"dev": MENU}


PICKUP_TIME = re.compile(r"([01]\d|2[0-3]):[0-5]\d")


def create_app():
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify({"status": "okay"})

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
        return jsonify(MENU_CACHE[app_version()])

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
        return jsonify(create_order(items, pickup_time)), 201

    @app.get("/orders/<int:order_id>")
    def get_one_order(order_id):
        order = get_order(order_id)
        if order is None:
            return jsonify({"error": "order not found"}), 404
        return jsonify(order)

    return app


app = create_app()
