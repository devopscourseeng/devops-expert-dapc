"""Tests for the simulated errors (SIMULATE_ERRORS) used to fill the logs panels."""

import logging

import pytest
from app import create_app
from features import app_version


@pytest.fixture
def client():
    return create_app().test_client()


def test_header_is_ignored_when_the_toggle_is_off(client, monkeypatch):
    monkeypatch.delenv("SIMULATE_ERRORS", raising=False)
    assert client.get("/menu", headers={"X-Simulate-Error": "1"}).status_code == 200


def test_header_gives_a_500_when_the_toggle_is_on(client, monkeypatch, caplog):
    monkeypatch.setenv("SIMULATE_ERRORS", "on")
    caplog.set_level(logging.INFO)
    response = client.get("/menu", headers={"X-Simulate-Error": "1"})
    assert response.status_code == 500
    assert response.get_json() == {"error": "simulated error"}
    failed = [r for r in caplog.records if r.getMessage() == "request failed"]
    assert len(failed) == 1
    assert failed[0].levelname == "ERROR"


def test_no_header_works_normally_when_the_toggle_is_on(client, monkeypatch):
    monkeypatch.setenv("SIMULATE_ERRORS", "on")
    assert client.get("/menu").status_code == 200


def test_simulated_error_is_counted_as_500(client, monkeypatch):
    from prometheus_client import REGISTRY

    monkeypatch.setenv("SIMULATE_ERRORS", "on")
    labels = {"endpoint": "/menu", "status": "500", "version": app_version()}
    before = REGISTRY.get_sample_value("http_requests_total", labels) or 0
    client.get("/menu", headers={"X-Simulate-Error": "1"})
    assert REGISTRY.get_sample_value("http_requests_total", labels) == before + 1
