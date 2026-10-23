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


def test_every_menu_item_is_available(client):
    response = client.get("/menu")
    assert response.status_code == 200
    for item in response.get_json():
        assert item["available"] is True


def test_single_menu_item_is_available(client):
    response = client.get("/menu/3")
    assert response.status_code == 200
    assert response.get_json()["available"] is True
