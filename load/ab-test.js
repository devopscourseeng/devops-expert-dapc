// ab-test.js: simulated customers for the A/B experiment (SCRUM-50), with
// some random warnings and errors for the logs panels.
//
// Each iteration is a new customer: it opens the menu with ?customer=<id>,
// reads its variant from the X-Variant header, and sometimes places an order.
//
// THE ORDER CHANCES ARE INVENTED FOR THE CLASS, so the experiment has a result:
// 20 % of the customers in A order, 24 % of the customers in B order.
// With real customers we would not know these numbers: the experiment finds them.
//
// WARNINGS AND ERRORS, for the logs panels: in each iteration, with small random
// chances, the customer also makes one bad request. These requests are separate
// from the A/B requests (no ?customer=), so they do not change the A/B numbers.
//   WARNING_CHANCE (default 0.05): a 4xx request (bad order, unknown order or
//     menu item); the API logs a WARNING "request rejected".
//   ERROR_CHANCE (default 0.02): a request with the header X-Simulate-Error; the
//     API answers 500 and logs an ERROR "request failed". About 1.5 % of all
//     requests, below the 5 % of the alert HighErrorRate. To see the alert go to
//     Pending and then Firing (it needs 2 minutes above 5 %):
//       docker compose --profile load run --rm -e ERROR_CHANCE=0.1 k6
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
const WARNING_CHANCE = Number(__ENV.WARNING_CHANCE || 0.05);
const ERROR_CHANCE = Number(__ENV.ERROR_CHANCE || 0.02);
const JSON_HEADERS = { "Content-Type": "application/json" };

// Three kinds of bad request from a customer; each one is answered with a 4xx.
const BAD_REQUESTS = [
  () => http.post(`${BASE_URL}/orders`, JSON.stringify({ items: [] }), { headers: JSON_HEADERS }),
  () => http.get(`${BASE_URL}/orders/999999`),
  () => http.get(`${BASE_URL}/menu/99`),
];

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
      { headers: JSON_HEADERS },
    );
    check(order, { "order 201": (r) => r.status === 201 });
  }

  if (Math.random() < WARNING_CHANCE) {
    const bad = BAD_REQUESTS[Math.floor(Math.random() * BAD_REQUESTS.length)]();
    check(bad, { "warning 4xx": (r) => r.status >= 400 && r.status < 500 });
  }

  if (Math.random() < ERROR_CHANCE) {
    const failed = http.get(`${BASE_URL}/menu`, { headers: { "X-Simulate-Error": "1" } });
    check(failed, { "error 500": (r) => r.status === 500 });
  }

  sleep(0.5);
}
