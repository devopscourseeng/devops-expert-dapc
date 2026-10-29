# Workflows

## CI (`ci.yml`)

Runs one job, **Unit tests**, on every pull request and on pushes to `main` and `develop`:

1. `ruff check .` (lint)
2. `pytest -q` (tests)

Branch protection on `main` and `develop` requires the **Unit tests** status check to pass before a PR can be merged.

The tests live in `src/summit-cafe-api/tests`.

## Publish image (`publish.yml`)

Builds the Summit Cafe API image and publishes it to GitHub Container Registry (GHCR):

```
ghcr.io/devopscourseeng/devops-expert-dapc/summit-cafe-api:<version>
```

Steps: check the version, build the image, run a smoke test (the container starts and `/health` answers), then publish for Intel and Apple Silicon computers. Each image gets two tags: the version (for example `1.2`) and the commit (`sha-<full commit>`).

A published version never changes. If the version already exists, the workflow stops.

### Publish a version

Tag the commit you want to release:

```
git tag v1.2
git push origin v1.2
```

Or open **Actions > Publish image > Run workflow** and type the version (for example `1.2`).

### One-time setup: make the package public

The first publish creates a private package. Open the repository page, then **Packages > summit-cafe-api > Package settings > Change visibility > Public**. After that, anyone can pull the image without a login or token:

```
docker pull ghcr.io/devopscourseeng/devops-expert-dapc/summit-cafe-api:1.2
```
