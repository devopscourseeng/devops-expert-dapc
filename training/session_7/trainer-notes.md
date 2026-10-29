# Session 7: trainer notes

Everything the trainer must prepare, and what to expect in class.

## Before the class

| # | What | How to check |
|---|---|---|
| 1 | Images in GHCR: `1.1`, `1.2` and the broken `1.3` | See "Publish the images" below |
| 2 | The package is public | An anonymous `docker pull` works (no `docker login`) |
| 3 | Jira: epic **SCRUM-23** with tickets **SCRUM-24 to SCRUM-27**, all with the label `session-7` | Open the board and filter by the label |
| 4 | The setup guide is sent to the participants | [student-setup.md](student-setup.md) |
| 5 | A full dry run on your computer | See "Dry run" below |
| 6 | Teams A, B and C are decided (two people each) | Not stored in this repository |

### Publish the images

Use the workflow **Publish image** (Actions tab, "Run workflow"). A published tag never changes, so you cannot publish the same version twice.

| Version | Branch to run the workflow from | Notes |
|---|---|---|
| 1.1 | `develop` | The first image. It has no `/version` route. |
| 1.2 | `develop` | Has `/version` and the toggle `SCHEDULED_ORDERS`. |
| 1.3 | `trainer/broken-release-1.3` | **Broken on purpose.** Do not merge this branch. |

Check the tags from any terminal:

```
curl -s "https://ghcr.io/token?scope=repository:devopscourseeng/devops-expert-dapc/summit-cafe-api:pull"
curl -s -H "Authorization: Bearer TOKEN" https://ghcr.io/v2/devopscourseeng/devops-expert-dapc/summit-cafe-api/tags/list
```

You should see `1.1`, `1.2`, `1.3` and the `sha-...` tags.

### What is broken in 1.3

The menu is cached by app version, and the cache only has the key `dev`. In any published image `APP_VERSION` is set (`1.3`), so `GET /menu` raises an error and returns **500**.

It passes everything the pipeline checks: the unit tests run with `APP_VERSION` not set, and the smoke test only calls `/health`. That is a good story for the class: our checks were too weak. `GET /menu/1`, `/health` and `/version` still work.

### Dry run (about 10 minutes)

```
./deploy/start-environment.sh 1.1
./deploy/deploy-to-environment.sh staging 1.2
./deploy/deploy-to-environment.sh prod 1.3
./deploy/set-weight.sh 50
for i in $(seq 1 20); do curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8200/menu; done | sort | uniq -c
./deploy/set-weight.sh 0
```

At 50%, about half of the calls return 500. After `set-weight.sh 0`, all return 200. Clean up with `docker rm -f cafe-prod cafe-prod-stable cafe-prod-canary cafe-staging`.

## In the class

| Block | Min | Notes |
|---|---|---|
| Opening: work trail | 15 | Slides 1–3. Look at session 6 pull requests and tickets. |
| Theory with Claude | 45 | Slides 4–15. Teams A, B, C. Backup answers: [theory/](theory/) |
| Break | 10 | |
| Setup check and tickets | 85 | Slides 17–19. First 10 minutes: everyone runs the four setup steps. |
| Break | 10 | |
| Team activity | 35 | Slides 20 and 22. Canary of 1.3, find the errors, roll back, write the runbook. |
| Skill | 20 | Slides 24–26. The skill reads the runbook and runs the steps. |
| Wrap-up | 20 | Slide 27. |

### The tickets (option "run it, then extend it")

Everyone starts from the scripts in the repo. Jira: SCRUM-24 to SCRUM-27.

| Ticket | Done when | Hint for the trainer |
|---|---|---|
| a. Deploy script | After a deploy, the script also checks `/menu` and that `/version` shows the deployed version | Add the checks after the `/health` loop in `deploy-to-environment.sh`. Note that 1.1 has no `/version`. |
| b. Blue-green | One command moves all calls to the other side, and one moves them back. The time is measured | `set-weight.sh 100` and `0` already do it. The ticket is a small `switch` script that reads the current side. A simple way to keep the state: a file or a container label. |
| c. Canary | 1.2 at 10, 50, 100. A script makes 20 calls and counts the versions | `for i in $(seq 1 20); do curl -s http://localhost:8200/version; echo; done \| sort \| uniq -c` |
| d. Feature toggle | 1.2 runs with the toggle off and on. A test shows `pickup_time` is saved only when it is on | The tests are in `src/summit-cafe-api/tests/test_features.py`. Run a container with `-e SCHEDULED_ORDERS=on`. |

Review every pull request: it must target `develop`, have a green "Unit tests", and a classmate's review.

### Common problems

See the table in [student-setup.md](student-setup.md). The two most common are Docker Desktop not running and typing the commands in CMD instead of Git Bash.

## Things in the starter code that are not bugs of today

The API has a few mistakes left on purpose for the earlier session 5 and 6 tickets: `/health` answers `okay` (SCRUM-8), Espresso costs 0 (SCRUM-7), and an order total ignores the quantity (SCRUM-18). Do not fix them in session 7 pull requests.

## After the class

Clean up on your computer: `docker rm -f cafe-prod cafe-prod-stable cafe-prod-canary cafe-staging`.
