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

## How we work

- Every change starts from a Jira ticket (project SCRUM) and goes through a pull request to `develop`.
- Branches: `feature/SCRUM-N` or `bugfix/SCRUM-N`, created from `develop`.
- `main` and `develop` are protected: a pull request, one approval and a green **Checks** job are required.
