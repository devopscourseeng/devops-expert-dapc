import pytest
from app import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_create_order_returns_201_with_the_order(client):
    response = client.post(
        "/orders",
        json={"items": [{"id": 2, "quantity": 2}, {"id": 4, "quantity": 1}]},
    )
    assert response.status_code == 201
    body = response.get_json()
    assert body["id"] >= 1
    assert [line["id"] for line in body["items"]] == [2, 4]


def test_get_created_order_returns_it(client):
    created = client.post("/orders", json={"items": [{"id": 3, "quantity": 1}]}).get_json()
    response = client.get(f"/orders/{created['id']}")
    assert response.status_code == 200
    assert response.get_json()["id"] == created["id"]


def test_get_unknown_order_returns_404(client):
    assert client.get("/orders/999999").status_code == 404


def test_create_order_rejects_empty_items(client):
    assert client.post("/orders", json={"items": []}).status_code == 400
