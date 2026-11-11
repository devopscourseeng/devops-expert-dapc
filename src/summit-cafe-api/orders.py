"""Orders for the Summit Cafe API. The data lives in memory (no database yet)."""

from menu import MENU_BY_ID

ORDERS = {}
_last_id = 0


def create_order(items, pickup_time=None):
    """Create an order from [{"id": menu_id, "quantity": n}, ...] and store it.

    pickup_time (like "14:30") is only used when the scheduled orders toggle is on.
    """
    global _last_id
    lines = []
    for line in items:
        item = MENU_BY_ID[line["id"]]
        lines.append(
            {
                "id": item["id"],
                "name": item["name"],
                "quantity": line["quantity"],
                "price": item["price"],
            }
        )
    total = round(sum(line["price"] * line["quantity"] for line in lines), 2)
    _last_id += 1
    order = {"id": _last_id, "items": lines, "total": total}
    if pickup_time is not None:
        order["pickup_time"] = pickup_time
    ORDERS[_last_id] = order
    return order


def get_order(order_id):
    return ORDERS.get(order_id)
