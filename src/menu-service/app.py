"""Menu service: the cafe menu, split out of the Summit Cafe API monolith."""

import os

from flask import Flask, jsonify
from menu import MENU, MENU_BY_ID

VERSION_DEFAULT = "dev"


def app_version():
    """The version of the image. The publish workflow sets it from the tag."""
    return os.environ.get("APP_VERSION", VERSION_DEFAULT)


def create_app():
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify({"status": "okay"})

    @app.get("/version")
    def version():
        return jsonify({"version": app_version()})

    @app.get("/menu")
    def list_menu():
        return jsonify(MENU)

    @app.get("/menu/<int:item_id>")
    def get_item(item_id):
        item = MENU_BY_ID.get(item_id)
        if item is None:
            return jsonify({"error": "item not found"}), 404
        return jsonify(item)

    return app


app = create_app()
