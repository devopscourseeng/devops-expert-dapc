# Example runbook: release 1.2 as a canary

This is the trainer's example for the team activity. Teams write their own. The skill in the last block reads a runbook like this one and runs it.

## Part 1. Context

| Item | Value |
|---|---|
| Goal | Release version 1.2 of the Summit Cafe API to prod as a canary: 10%, then 50%, then 100% of the calls. |
| Versions | Live now: 1.1 (`cafe-prod-stable`). New: 1.2 (`cafe-prod-canary`). Last good version to go back to: 1.1. |
| Where | staging: port 8100. prod: nginx on port 8200, stable on 8201, canary on 8202. Weights are set with `./deploy/set-weight.sh`. |
| Ready to start | Image 1.2 is in GHCR. The CI job "Unit tests" is green. `curl http://localhost:8200/menu` answers. |
| When it is bad | Any call to `/menu` that does not return 200 from the new version. One error is enough to go back. |
| Who decides | A person says yes before the weights change and before a rollback. The skill only suggests. |

## Part 2. Steps

| # | Step | Command | How we know it is OK | How we go back |
|---|---|---|---|---|
| 1 | Check ready | `curl http://localhost:8200/menu` | The menu answers | Stop here |
| 2 | Test in staging | `./deploy/deploy-to-environment.sh staging 1.2` | The script prints OK and `curl http://localhost:8100/version` shows 1.2 | Stop here |
| 3 | Deploy to prod | `./deploy/deploy-to-environment.sh prod 1.2` | The script prints OK and `curl http://localhost:8202/version` shows 1.2 | `./deploy/deploy-to-environment.sh prod 1.1` |
| 4 | Weight 10 | `./deploy/set-weight.sh 10` | The script prints OK. In 20 calls to `/version`, about 2 show 1.2 | `./deploy/set-weight.sh 0` |
| 5 | Watch | `./deploy/check-menu.sh` | The script prints OK: every call returned 200 | `./deploy/set-weight.sh 0` |
| 6 | Weight 50 | `./deploy/set-weight.sh 50` | In 20 calls to `/version`, about 10 show 1.2 | `./deploy/set-weight.sh 0` |
| 7 | Watch | Same as step 5 | Every call returns 200 | `./deploy/set-weight.sh 0` |
| 8 | Weight 100 | `./deploy/set-weight.sh 100` | All calls to `/version` show 1.2 | `./deploy/set-weight.sh 0` |

Time to roll back (measure it and write it here): ___ seconds.

## Notes

- Version 1.1 has no `/version` route. A call that reaches 1.1 answers "Not Found". Read it as "this is the old version".
- In the activity, the new version is 1.4, which is broken on purpose: the watch step (5) finds `500` answers from `/menu`, and the way back is `./deploy/set-weight.sh 0`.
- Each team writes its own runbook, with the commands and the times it measured, and opens a pull request.
