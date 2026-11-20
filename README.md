# DevOps Expert (DAPC) course

Material and code for the CertiProf DAPC course (DevOps Advanced Professional Certification), sessions 5 to 16.

| Folder | What is in it |
|---|---|
| [`training/`](training/) | The course material: context, global plan, guides and the files for each session |
| [`src/`](src/) | The source code we work on during the course |
| [`.github/`](.github/) | The CI workflow (runs ruff and the tests on every pull request) |

## Training material

| File or folder | What it is |
|---|---|
| [`training/CONTEXT.md`](training/CONTEXT.md) | Course context, goals and conventions |
| [`training/plan/PLAN.md`](training/plan/PLAN.md) | The global plan for sessions 5 to 16 |
| [`training/docs/`](training/docs/) | Guides: setup, invitations, starter tickets |
| [`training/session_5/`](training/session_5/) | Session 5: trainer slides and backup answers for the Three Ways activity |

## Source code

| Folder | What it is |
|---|---|
| [`src/summit-cafe-api/`](src/summit-cafe-api/) | The Summit Cafe API: a small Flask REST API with a Dockerfile and tests |

## Monitoring

Run the API, the menu service, Prometheus, Loki, Alloy and Grafana together. Everything is configured from files in [`observability/`](observability/).

```
docker compose up -d --build
```

| Service | Address |
|---|---|
| Summit Cafe API | http://localhost:8000 (metrics at `/metrics`) |
| Menu service | http://localhost:8001 |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 (no login, for local training only) |
| Loki (logs) | http://localhost:3100 (read it from Grafana) |
| Alloy (sends the logs to Loki) | http://localhost:12345 |

Open the **Summit Cafe** dashboard: http://localhost:3000/d/summit-cafe

**Radiator:** open http://localhost:3000/d/summit-cafe?kiosk on a shared screen so the whole team sees the dashboard, without menus.

To see data in the panels, send traffic to the API (stop with Ctrl+C):

```
./observability/send-traffic.sh
DELAY=1 BASE_URL=http://localhost:8000 ./observability/send-traffic.sh   # slower, explicit URL
```

What each panel query means: [`observability/queries.md`](observability/queries.md).

**Logs:** both services write one JSON object per line, with `time`, `level`, `service`, `request_id` and `msg`. Every response has an `X-Request-ID` header; send your own value to follow one request:

```
curl -s -H 'X-Request-ID: abc123' -H 'Content-Type: application/json' \
  -d '{"items":[{"id":2,"quantity":1}]}' localhost:8000/orders
docker compose logs --no-log-prefix summit-cafe-api | jq -cR 'fromjson? | select(.request_id=="abc123")'
```

`fromjson?` skips gunicorn's own plain-text lines.

**Logs in Grafana:** Alloy reads the logs of both services and sends them to Loki, with the labels `service` and `level`. The dashboard shows the number of errors and warnings, errors and warnings per minute, and the latest lines. In **Explore** (data source Loki) you can search any line, for example `{service="summit-cafe-api"} |= "abc123"`. Levels: ERROR for a 5xx response, WARNING for a 4xx response or a request slower than 1 second.

## A/B experiment

An A/B test of a **Latte + Croissant combo** on the menu (SCRUM-50). It is off by default.

* With `AB_COMBO_TEST=on`, `GET /menu?customer=<id>` puts each customer in variant **A** (the menu as today) or **B** (the menu with the combo), always the same one for the same id, and answers with the header `X-Variant`.
* `POST /orders?customer=<id>` counts the order for that variant.
* The panel **A/B: orders per menu view** shows the conversion of A and B.

```
AB_COMBO_TEST=on docker compose up -d --build     # start with the experiment on
curl -i "localhost:8000/menu?customer=c-1"        # see X-Variant, and the combo for B
docker compose --profile load run --rm k6         # 3 minutes of simulated customers
docker compose up -d                              # stop the experiment (toggle off)
```

The simulated customers in [`load/ab-test.js`](load/ab-test.js) order with invented chances (20 % in A, 24 % in B), so the class sees a result. They also make some random bad requests (about 5 % warnings, 2 % errors) for the logs panels; these do not change the A/B numbers. The errors use the training toggle `SIMULATE_ERRORS`, which `docker-compose.yml` turns on: a request with the header `X-Simulate-Error` gets a 500.

Stop everything: `docker compose down`

The stack needs about 8 GB of RAM (Loki and Alloy add about 300 MB). If your computer has less, use GitHub Codespaces.

## How we work

- Every change starts from a Jira ticket (project SCRUM) and goes through a pull request to `develop`.
- Branches: `feature/SCRUM-N` or `bugfix/SCRUM-N`, created from `develop`.
- `main` and `develop` are protected: a pull request, one approval and a green **Checks** job are required.
