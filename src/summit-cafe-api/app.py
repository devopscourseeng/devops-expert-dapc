"""Summit Cafe API: a small REST API for the cafe menu."""

from flask import Flask, jsonify, request
from menu import MENU, MENU_BY_ID
from orders import create_order, get_order


def create_app():
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify({"status": "okay"})

    @app.get("/menu")
    def list_menu():
        return jsonify(MENU)

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
        return jsonify(create_order(items)), 201

    @app.get("/orders/<int:order_id>")
    def get_one_order(order_id):
        order = get_order(order_id)
        if order is None:
            return jsonify({"error": "order not found"}), 404
        return jsonify(order)

    return app


app = create_app()
