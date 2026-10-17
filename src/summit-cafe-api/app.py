"""Summit Cafe API: a small REST API for the cafe menu."""

from flask import Flask, jsonify
from menu import MENU, MENU_BY_ID


def create_app():
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.get("/menu")
    def list_menu():
        return jsonify(MENU)

    @app.get("/menu/<int:item_id>")
    def get_item(item_id):
        return jsonify(MENU_BY_ID[item_id])

    return app


app = create_app()
