"""Tests for the A/B experiment with the Latte + Croissant combo (SCRUM-50)."""

import pytest
from app import create_app
from features import variant_for
from menu import MENU
from prometheus_client import REGISTRY

COMBO_ID = 6


@pytest.fixture
def client():
    return create_app().test_client()


@pytest.fixture
def ab_on(monkeypatch):
    monkeypatch.setenv("AB_COMBO_TEST", "on")


def value(name, **labels):
    return REGISTRY.get_sample_value(name, labels) or 0.0


def customer_with(variant):
    """The first customer id c-0, c-1, ... that lands in the given variant."""
    return next(f"c-{n}" for n in range(1000) if variant_for(f"c-{n}") == variant)


def ids(menu):
    return [item["id"] for item in menu]


def test_same_customer_always_gets_the_same_variant():
    assert len({variant_for("c-42") for _ in range(10)}) == 1


def test_split_is_close_to_50_50():
    b_count = sum(variant_for(f"c-{n}") == "B" for n in range(1000))
    assert 450 <= b_count <= 550


def test_toggle_off_menu_is_unchanged(client):
    response = client.get(f"/menu?customer={customer_with('B')}")
    assert response.status_code == 200
    assert COMBO_ID not in ids(response.get_json())
    assert "X-Variant" not in response.headers


def test_toggle_on_variant_b_sees_the_combo(client, ab_on):
    response = client.get(f"/menu?customer={customer_with('B')}")
    assert response.headers["X-Variant"] == "B"
    assert COMBO_ID in ids(response.get_json())


def test_toggle_on_variant_a_does_not_see_the_combo(client, ab_on):
    response = client.get(f"/menu?customer={customer_with('A')}")
    assert response.headers["X-Variant"] == "A"
    assert COMBO_ID not in ids(response.get_json())


def test_toggle_on_without_customer_menu_is_unchanged(client, ab_on):
    response = client.get("/menu")
    assert response.get_json() == MENU
    assert "X-Variant" not in response.headers


def test_menu_view_is_counted_by_variant(client, ab_on):
    before = value("ab_menu_views_total", variant="B")
    client.get(f"/menu?customer={customer_with('B')}")
    assert value("ab_menu_views_total", variant="B") == before + 1


def test_order_is_counted_by_variant(client, ab_on):
    before = value("ab_orders_total", variant="B")
    response = client.post(
        f"/orders?customer={customer_with('B')}",
        json={"items": [{"id": 2, "quantity": 1}]},
    )
    assert response.status_code == 201
    assert response.headers["X-Variant"] == "B"
    assert value("ab_orders_total", variant="B") == before + 1


def test_rejected_order_is_not_counted(client, ab_on):
    before = value("ab_orders_total", variant="B")
    response = client.post(f"/orders?customer={customer_with('B')}", json={"items": []})
    assert response.status_code == 400
    assert value("ab_orders_total", variant="B") == before


def test_toggle_off_order_is_not_counted(client):
    before = value("ab_orders_total", variant="B")
    client.post(f"/orders?customer={customer_with('B')}", json={"items": [{"id": 2, "quantity": 1}]})
    assert value("ab_orders_total", variant="B") == before


def test_combo_can_be_ordered(client):
    response = client.post("/orders", json={"items": [{"id": COMBO_ID, "quantity": 1}]})
    assert response.status_code == 201
    assert response.get_json()["total"] == 6.0


def test_combo_can_be_read_by_id(client):
    assert client.get(f"/menu/{COMBO_ID}").get_json()["name"] == "Latte + Croissant combo"
