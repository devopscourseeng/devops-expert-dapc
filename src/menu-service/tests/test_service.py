import pytest
from app import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_health_returns_okay(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "okay"}


def test_version_defaults_to_dev(client, monkeypatch):
    monkeypatch.delenv("APP_VERSION", raising=False)
    assert client.get("/version").get_json() == {"version": "dev"}


def test_version_uses_app_version(client, monkeypatch):
    monkeypatch.setenv("APP_VERSION", "1.4")
    assert client.get("/version").get_json() == {"version": "1.4"}
