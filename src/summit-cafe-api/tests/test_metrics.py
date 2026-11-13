"""Tests for the Prometheus metrics. The registry is global, so each test
compares a value before and after the call instead of an absolute value."""

import pytest
from app import create_app
from prometheus_client import REGISTRY


def value(name, **labels):
    return REGISTRY.get_sample_value(name, labels) or 0.0


@pytest.fixture
def client():
    return create_app().test_client()


def test_metrics_endpoint_returns_the_metrics(client):
    response = client.get("/metrics")
    assert response.status_code == 200
    assert response.content_type.startswith("text/plain")
    assert "http_requests_total" in response.get_data(as_text=True)


def test_valid_order_increases_orders_total_by_one(client):
    before = value("orders_total")
    response = client.post("/orders", json={"items": [{"id": 2, "quantity": 1}]})
    assert response.status_code == 201
    assert value("orders_total") == before + 1


def test_invalid_order_does_not_increase_orders_total(client):
    before = value("orders_total")
    response = client.post("/orders", json={"items": []})
    assert response.status_code == 400
    assert value("orders_total") == before


def test_request_is_counted_by_route_template(client):
    labels = {"endpoint": "/menu/<int:item_id>", "status": "200"}
    before = value("http_requests_total", **labels)
    assert client.get("/menu/1").status_code == 200
    assert value("http_requests_total", **labels) == before + 1


def test_request_duration_is_observed(client):
    before = value("http_request_duration_seconds_count", endpoint="/menu")
    client.get("/menu")
    assert value("http_request_duration_seconds_count", endpoint="/menu") == before + 1


def test_unhandled_exception_is_counted_as_500():
    app = create_app()

    def boom():
        raise RuntimeError("boom")

    app.add_url_rule("/boom", "boom", boom)
    labels = {"endpoint": "/boom", "status": "500"}
    before = value("http_requests_total", **labels)
    assert app.test_client().get("/boom").status_code == 500
    assert value("http_requests_total", **labels) == before + 1


def test_unknown_path_is_counted_as_unmatched(client):
    labels = {"endpoint": "unmatched", "status": "404"}
    before = value("http_requests_total", **labels)
    assert client.get("/no-such-page/123").status_code == 404
    assert value("http_requests_total", **labels) == before + 1


def test_wrong_method_is_counted_as_unmatched(client):
    labels = {"endpoint": "unmatched", "status": "405"}
    before = value("http_requests_total", **labels)
    assert client.delete("/menu").status_code == 405
    assert value("http_requests_total", **labels) == before + 1


def test_metrics_endpoint_is_not_measured(client):
    before_count = value("http_requests_total", endpoint="/metrics", status="200")
    before_duration = value("http_request_duration_seconds_count", endpoint="/metrics")
    client.get("/metrics")
    assert value("http_requests_total", endpoint="/metrics", status="200") == before_count
    assert value("http_request_duration_seconds_count", endpoint="/metrics") == before_duration
