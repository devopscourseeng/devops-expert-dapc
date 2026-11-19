import pytest
from app import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_menu_returns_a_list(client):
    response = client.get("/menu")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
    assert len(response.get_json()) > 0


def test_get_one_item(client):
    response = client.get("/menu/3")
    assert response.status_code == 200
    assert response.get_json()["name"] == "Latte"


def test_get_unknown_item_returns_404(client):
    response = client.get("/menu/99")
    assert response.status_code == 404
    assert response.get_json() == {"error": "item not found"}


def test_every_item_has_the_expected_fields(client):
    for item in client.get("/menu").get_json():
        assert set(item) == {"id", "name", "category", "price"}
        assert isinstance(item["id"], int)
        assert isinstance(item["name"], str) and item["name"].strip()
        assert item["category"] in ("drinks", "food")
        assert isinstance(item["price"], (int, float)) and not isinstance(item["price"], bool)


def test_item_ids_are_unique(client):
    ids = [item["id"] for item in client.get("/menu").get_json()]
    assert len(ids) == len(set(ids))


def test_get_item_matches_the_list(client):
    for item in client.get("/menu").get_json():
        response = client.get(f"/menu/{item['id']}")
        assert response.status_code == 200
        assert response.get_json() == item


@pytest.mark.xfail(reason="Known bug: Espresso has price 0 in the menu data", strict=True)
def test_every_price_is_positive(client):
    assert all(item["price"] > 0 for item in client.get("/menu").get_json())
