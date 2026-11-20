// ab-test.js: simulated customers for the A/B experiment (SCRUM-50).
//
// Each iteration is a new customer: it opens the menu with ?customer=<id>,
// reads its variant from the X-Variant header, and sometimes places an order.
//
// THE ORDER CHANCES ARE INVENTED FOR THE CLASS, so the experiment has a result:
// 20 % of the customers in A order, 24 % of the customers in B order.
// With real customers we would not know these numbers: the experiment finds them.
//
// Run (from the repo root, with the stack up and AB_COMBO_TEST=on):
//   docker compose --profile load run --rm k6

import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  vus: 20,
  duration: "3m",
};

const BASE_URL = __ENV.BASE_URL || "http://localhost:8000";
const ORDER_CHANCE = { A: 0.2, B: 0.24 };
const COMBO_ID = 6;
const CAPPUCCINO_ID = 2;

export default function () {
  const customer = `c-${__VU}-${__ITER}`;

  const menu = http.get(`${BASE_URL}/menu?customer=${customer}`);
  check(menu, { "menu 200": (r) => r.status === 200 });
  const variant = menu.headers["X-Variant"];

  if (variant && Math.random() < ORDER_CHANCE[variant]) {
    // Customers in B who order take the combo half of the time.
    const item = variant === "B" && Math.random() < 0.5 ? COMBO_ID : CAPPUCCINO_ID;
    const order = http.post(
      `${BASE_URL}/orders?customer=${customer}`,
      JSON.stringify({ items: [{ id: item, quantity: 1 }] }),
      { headers: { "Content-Type": "application/json" } },
    );
    check(order, { "order 201": (r) => r.status === 201 });
  }

  sleep(0.5);
}
