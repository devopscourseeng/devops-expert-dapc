"""Menu data for the Summit Cafe API. The data lives in memory (no database yet)."""

MENU = [
    {"id": 1, "name": "Espresso", "category": "drinks", "price": 0, "available": True},
    {"id": 2, "name": "Capuchino", "category": "drinks", "price": 3.5, "available": True},
    {"id": 3, "name": "Latte", "category": "drinks", "price": 4.0, "available": True},
    {"id": 4, "name": "Croissant", "category": "food", "price": 2.8, "available": True},
    {"id": 5, "name": "Banana bread", "category": "food", "price": 3.2, "available": True},
]

MENU_BY_ID = {item["id"]: item for item in MENU}
