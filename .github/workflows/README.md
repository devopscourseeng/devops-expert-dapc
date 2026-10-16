# CI

`ci.yml` runs one job, **Checks**, on every pull request and on pushes to `main` and `develop`:

1. `ruff check .` (lint)
2. `pytest -q` (tests)

Branch protection on `main` and `develop` should require the **Checks** status check to pass before a PR can be merged.

The tests live in `src/summit-cafe-api/tests`.
