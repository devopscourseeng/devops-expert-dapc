# Summit Cafe API

A small REST API for the cafe menu. It is the project we build and improve during the course.

## Endpoints

| Method | Path | What it returns |
|---|---|---|
| GET | `/health` | The status of the service |
| GET | `/version` | The image version and the state of the toggles |
| GET | `/menu` | The list of menu items |
| GET | `/menu/{id}` | One menu item |

| POST | `/orders` | Creates an order. With `SCHEDULED_ORDERS=on` it also accepts `pickup_time` (like `14:30`) |
| GET | `/orders/{id}` | One order |

## Settings

| Variable | Values | What it does |
|---|---|---|
| `SCHEDULED_ORDERS` | `off` (default), `on` | Feature toggle: lets a customer choose a pickup time. With `off` the field is ignored and the API works as in 1.1. |
| `APP_VERSION` | text | The version shown by `/version` and in the `version` label of the request metrics. The publish workflow sets it from the image tag. Default: `dev`. |

## Metrics

`GET /metrics` shows the metrics for Prometheus:

| Metric | Labels | What it counts |
|---|---|---|
| `http_requests_total` | `endpoint`, `status`, `version` | HTTP requests |
| `http_request_duration_seconds` | `endpoint`, `version` | Request time (histogram) |
| `orders_total` | none | Orders created |

`endpoint` is the route template (`/menu/<int:item_id>`), `version` is `APP_VERSION`. The `version` label lets Prometheus tell the stable and the canary containers apart.

## Project files

| File | What it does |
|---|---|
| `app.py` | The routes |
| `menu.py` | The menu data (kept in memory, no database) |
| `tests/` | The tests (pytest) |
| `Dockerfile` | Builds the container image |
| `requirements.txt` | Python packages |

## Run it

_To be written: this is a starter ticket._

## Deploy

The service can be deployed to Render from this repository with the Dockerfile. Set the root directory to `src/summit-cafe-api`.
