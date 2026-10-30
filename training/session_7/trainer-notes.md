# Session 7: trainer notes

Everything the trainer must prepare, and what to expect in class.

## Before the class

| # | What | How to check |
|---|---|---|
| 1 | Images in GHCR: `1.1`, `1.2` and the broken `1.4` | See "Publish the images" below |
| 2 | The package is public | An anonymous `docker pull` works (no `docker login`) |
| 3 | Jira: no code tickets for session 7. SCRUM-24 to SCRUM-27 were closed, because the hands-on uses the scripts only | Filter the board by the label `session-7` |
| 4 | The setup guide is sent to the participants | [student-setup.md](student-setup.md) |
| 5 | A full dry run on your computer | See "Dry run" below |
| 6 | Teams A, B and C are decided (two people each) | Not stored in this repository |

### Publish the images

Use the workflow **Publish image** (Actions tab, "Run workflow"). A published tag never changes, so you cannot publish the same version twice.

| Version | Branch to run the workflow from | Notes |
|---|---|---|
| 1.1 | `develop` | The first image. It has no `/version` route. |
| 1.2 | `develop` | Has `/version` and the toggle `SCHEDULED_ORDERS`. |
| 1.4 | `trainer/broken-release-1.3` | **Broken on purpose.** Do not merge this branch. (The branch name still says 1.3: the first try at 1.3 was published by mistake from another branch. 1.3 is a healthy image and is not used.) |

Check the tags from any terminal:

```
curl -s "https://ghcr.io/token?scope=repository:devopscourseeng/devops-expert-dapc/summit-cafe-api:pull"
curl -s -H "Authorization: Bearer TOKEN" https://ghcr.io/v2/devopscourseeng/devops-expert-dapc/summit-cafe-api/tags/list
```

You should see `1.1`, `1.2`, `1.3`, `1.4` and the `sha-...` tags.

### What is broken in 1.4

The menu is cached by app version, and the cache only has the key `dev`. In any published image `APP_VERSION` is set (`1.3`), so `GET /menu` raises an error and returns **500**.

It passes everything the pipeline checks: the unit tests run with `APP_VERSION` not set, and the smoke test only calls `/health`. That is a good story for the class: our checks were too weak. `GET /menu/1`, `/health` and `/version` still work.

### Dry run (about 10 minutes)

```
./deploy/start-environment.sh 1.2
./deploy/deploy-to-environment.sh staging 1.2
./deploy/deploy-to-environment.sh staging 1.4
URL=http://localhost:8100/menu ./deploy/check-menu.sh
./deploy/deploy-to-environment.sh prod 1.4
./deploy/set-weight.sh 10
./deploy/check-menu.sh
./deploy/set-weight.sh 0
./deploy/check-menu.sh
```

In staging, 1.4 returns 500 from `/menu`. In prod at 10%, about 2 of 20 calls return 500. After `set-weight.sh 0`, all return 200. Clean up with `docker rm -f cafe-prod cafe-prod-stable cafe-prod-canary cafe-staging`.

## In the class

| Block | Min | Slides | Notes |
|---|---|---|---|
| Opening: work trail | 15 | 1–3 | Look at session 6 pull requests and tickets. |
| Theory with Claude | 45 | 4–14 | Teams A, B, C. Backup answers: [theory/](theory/) |
| Break | 10 | 15 | |
| Hands-on: deploy, canary and rollback | 85 | 16–20 | First 10 minutes: everyone runs the four setup steps (slide 16). Slide 19 is the picture of the flow. Slide 20 has the five steps, and its speaker notes have the answers. |
| Break | 10 | 21 | |
| Skill: deploy from the runbook | 20 | 22–24 | Runbook, harness engineering, and the skill. Students create the skill in the Claude Code CLI, so it can reach Docker on their computer. |
| Closing | 20 | 25 | |

### The hands-on (no code, no tickets)

Students use only the scripts in `deploy/` and find the commands themselves (cheat sheet on slide 17, `deploy/README.md`). Nobody writes code, so there are no pull requests in this block.

1. Start with 1.2 as the base, in prod (stable) and in staging.
2. Try the broken 1.4 in staging. `/health` is OK, but `/menu` returns 500: do not release.
3. Deploy 1.4 to prod. It goes to the canary with 0% of the calls, so prod still works.
4. Send 10% of the calls to 1.4. `check-menu.sh` shows errors that come and go.
5. Roll back with `set-weight.sh 0`, and time it. All calls return 200 again.

Students who finish early do the feature toggle on slide 18.

### Common problems

See the table in [student-setup.md](student-setup.md). The two most common are Docker Desktop not running and typing the commands in CMD instead of Git Bash.

## Things in the starter code that are not bugs of today

The API has a few mistakes left on purpose for the earlier session 5 and 6 tickets: `/health` answers `okay` (SCRUM-8), Espresso costs 0 (SCRUM-7), and an order total ignores the quantity (SCRUM-18). Do not fix them in session 7.

## After the class

Clean up on your computer: `docker rm -f cafe-prod cafe-prod-stable cafe-prod-canary cafe-staging`.
