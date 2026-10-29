import pytest
from app import create_app

ITEMS = [{"id": 2, "quantity": 1}]


@pytest.fixture
def client():
    return create_app().test_client()


def test_version_defaults_to_dev_with_the_toggle_off(client, monkeypatch):
    monkeypatch.delenv("APP_VERSION", raising=False)
    monkeypatch.delenv("SCHEDULED_ORDERS", raising=False)
    assert client.get("/version").get_json() == {"version": "dev", "scheduled_orders": "off"}


def test_version_shows_the_image_version_and_the_toggle(client, monkeypatch):
    monkeypatch.setenv("APP_VERSION", "1.2")
    monkeypatch.setenv("SCHEDULED_ORDERS", "on")
    assert client.get("/version").get_json() == {"version": "1.2", "scheduled_orders": "on"}


def test_toggle_off_ignores_pickup_time(client, monkeypatch):
    monkeypatch.setenv("SCHEDULED_ORDERS", "off")
    response = client.post("/orders", json={"items": ITEMS, "pickup_time": "14:30"})
    assert response.status_code == 201
    assert "pickup_time" not in response.get_json()


def test_toggle_off_does_not_validate_pickup_time(client, monkeypatch):
    monkeypatch.delenv("SCHEDULED_ORDERS", raising=False)
    response = client.post("/orders", json={"items": ITEMS, "pickup_time": "soon"})
    assert response.status_code == 201


def test_toggle_on_saves_pickup_time(client, monkeypatch):
    monkeypatch.setenv("SCHEDULED_ORDERS", "on")
    created = client.post("/orders", json={"items": ITEMS, "pickup_time": "14:30"})
    assert created.status_code == 201
    assert created.get_json()["pickup_time"] == "14:30"
    stored = client.get(f"/orders/{created.get_json()['id']}")
    assert stored.get_json()["pickup_time"] == "14:30"


def test_toggle_on_pickup_time_is_optional(client, monkeypatch):
    monkeypatch.setenv("SCHEDULED_ORDERS", "on")
    response = client.post("/orders", json={"items": ITEMS})
    assert response.status_code == 201
    assert "pickup_time" not in response.get_json()


@pytest.mark.parametrize("bad", ["soon", "25:00", "14:60", "9:30", "14:30\n", 1430, None])
def test_toggle_on_rejects_a_bad_pickup_time(client, monkeypatch, bad):
    monkeypatch.setenv("SCHEDULED_ORDERS", "on")
    response = client.post("/orders", json={"items": ITEMS, "pickup_time": bad})
    assert response.status_code == 400
