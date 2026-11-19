"""Tests for the JSON logs and the request id."""

import json
import logging

import pytest
from app import create_app
from logging_setup import JsonFormatter


@pytest.fixture
def client():
    return create_app().test_client()


def test_response_has_a_request_id(client):
    response = client.get("/health")
    assert response.headers.get("X-Request-ID")


def test_request_id_from_the_header_is_returned(client):
    response = client.get("/health", headers={"X-Request-ID": "abc123"})
    assert response.headers["X-Request-ID"] == "abc123"


def test_each_request_gets_a_new_request_id(client):
    first = client.get("/health").headers["X-Request-ID"]
    second = client.get("/health").headers["X-Request-ID"]
    assert first != second


def test_formatter_writes_one_json_object_with_the_five_keys():
    record = logging.LogRecord("app", logging.INFO, __file__, 1, "hello %s", ("world",), None)
    record.request_id = "abc123"
    entry = json.loads(JsonFormatter().format(record))
    assert {"time", "level", "service", "request_id", "msg"} <= entry.keys()
    assert entry["level"] == "INFO"
    assert entry["request_id"] == "abc123"
    assert entry["msg"] == "hello world"


def test_formatter_uses_a_dash_outside_a_request():
    record = logging.LogRecord("app", logging.WARNING, __file__, 1, "no request", None, None)
    assert json.loads(JsonFormatter().format(record))["request_id"] == "-"


def test_formatter_adds_extra_fields():
    record = logging.LogRecord("app", logging.INFO, __file__, 1, "x", None, None)
    record.order_id = 7
    assert json.loads(JsonFormatter().format(record))["order_id"] == 7


def test_service_name_comes_from_the_environment(monkeypatch):
    monkeypatch.setenv("SERVICE_NAME", "my-service")
    record = logging.LogRecord("app", logging.INFO, __file__, 1, "x", None, None)
    assert json.loads(JsonFormatter().format(record))["service"] == "my-service"


def test_create_app_twice_does_not_add_a_second_handler():
    create_app()
    app = create_app()
    json_handlers = [h for h in app.logger.handlers if getattr(h, "_json_logs", False)]
    assert len(json_handlers) == 1


def test_service_name_default_is_summit_cafe_api(monkeypatch):
    monkeypatch.delenv("SERVICE_NAME", raising=False)
    record = logging.LogRecord("app", logging.INFO, __file__, 1, "x", None, None)
    assert json.loads(JsonFormatter().format(record))["service"] == "summit-cafe-api"


def test_valid_order_logs_order_created(client, caplog):
    caplog.set_level(logging.INFO)
    response = client.post(
        "/orders",
        json={"items": [{"id": 2, "quantity": 1}]},
        headers={"X-Request-ID": "abc123"},
    )
    assert response.status_code == 201
    records = [r for r in caplog.records if r.getMessage() == "order created"]
    assert len(records) == 1
    assert records[0].levelname == "INFO"
    assert records[0].order_id == response.get_json()["id"]
    assert records[0].total == response.get_json()["total"]
    assert records[0].request_id == "abc123"


def test_server_error_logs_request_failed(caplog):
    app = create_app()

    def boom():
        raise RuntimeError("boom")

    app.add_url_rule("/boom-log", "boom_log", boom)
    caplog.set_level(logging.INFO)
    assert app.test_client().get("/boom-log").status_code == 500
    failed = [r for r in caplog.records if r.getMessage() == "request failed"]
    assert len(failed) == 1
    assert failed[0].levelname == "ERROR"
    assert failed[0].status == 500
    assert failed[0].path == "/boom-log"


def test_slow_request_logs_a_warning(monkeypatch, caplog):
    import logging_setup

    monkeypatch.setattr(logging_setup, "SLOW_REQUEST_SECONDS", -1)
    caplog.set_level(logging.INFO)
    create_app().test_client().get("/health")
    assert any(r.getMessage() == "slow request" and r.levelname == "WARNING" for r in caplog.records)
