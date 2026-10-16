# Summit Cafe API

A small REST API for the cafe menu. It is the project we build and improve during the course.

## Endpoints

| Method | Path | What it returns |
|---|---|---|
| GET | `/health` | The status of the service |
| GET | `/menu` | The list of menu items |
| GET | `/menu/{id}` | One menu item |

More endpoints come in later sessions.

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
