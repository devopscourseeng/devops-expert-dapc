"""Menu data for the Summit Cafe API. The data lives in memory (no database yet)."""

MENU = [
    {"id": 1, "name": "Espresso", "category": "drinks", "price": 0},
    {"id": 2, "name": "Capuchino", "category": "drinks", "price": 3.5},
    {"id": 3, "name": "Latte", "category": "drinks", "price": 4.0},
    {"id": 4, "name": "Croissant", "category": "food", "price": 2.8},
    {"id": 5, "name": "Banana bread", "category": "food", "price": 3.2},
]

MENU_BY_ID = {item["id"]: item for item in MENU}
