# Menu service

The cafe menu as its own service, split out of the Summit Cafe API monolith (`src/summit-cafe-api`) with the strangler pattern. For now the monolith still serves `/menu` too; nothing routes traffic here yet.

## Endpoints

| Method | Path | What it returns |
|---|---|---|
| GET | `/health` | The status of the service |
| GET | `/version` | The image version |
| GET | `/menu` | The list of menu items |
| GET | `/menu/{id}` | One menu item, or 404 with `{"error": "item not found"}` |

Each item has `id` (int), `name` (text), `category` (`drinks` or `food`) and `price` (number).

## Settings

| Variable | Values | What it does |
|---|---|---|
| `APP_VERSION` | text | The version shown by `/version`. The publish workflow sets it from the image tag. |
| `PORT` | number | The port gunicorn listens on inside the container. Default: `8000`. |

## Run the tests

From this folder (it has its own `pytest.ini`):

```
cd src/menu-service
pip install -r requirements.txt pytest
pytest -q
```

## Run it with Docker

```
docker build -t menu-service:local --build-arg APP_VERSION=local src/menu-service
docker run -d --name menu-service -p 8300:8000 menu-service:local

curl http://localhost:8300/health      # {"status": "okay"}
curl http://localhost:8300/version     # {"version": "local"}
curl http://localhost:8300/menu        # the list
curl -i http://localhost:8300/menu/99  # 404

docker rm -f menu-service
```

## Published image

Pushing a `v*` tag publishes it next to the monolith, with the same version:

```
ghcr.io/devopscourseeng/devops-expert-dapc/menu-service:<version>
```
