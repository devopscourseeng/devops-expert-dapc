# Example runbook: release 1.4 as a canary

This is the trainer's example. It is the same runbook as the runbook slide. The skill in the last block reads a runbook like this one and runs it.

## Part 1. Context

| Item | Value |
|---|---|
| Goal | Release version 1.4 of the Summit Cafe API to prod as a canary: 10%, then 50%, then 100% of the calls. |
| Versions | Live now: 1.2 (`cafe-prod-stable`). New: 1.4 (`cafe-prod-canary`). Last good version to go back to: 1.2. |
| Where | staging: port 8100. prod: nginx on port 8200, stable on 8201, canary on 8202. Weights are set with `./deploy/set-weight.sh`. |
| Ready to start | Image 1.4 is in GHCR. The CI job "Unit tests" is green. `curl http://localhost:8200/menu` answers. |
| When it is bad | Any call to `/menu` that does not return 200. One error is enough to go back. |
| Who decides | A person says yes before the weights change and before a rollback. The skill only suggests. |

## Part 2. Steps

| # | Step | Command | How we know it is OK | How we go back |
|---|---|---|---|---|
| 1 | Check ready | `curl http://localhost:8200/menu` | The menu answers | Stop here |
| 2 | Test in staging | `./deploy/deploy-to-environment.sh staging 1.4` | The script prints OK and staging answers on 8100 | Stop here |
| 3 | Deploy to prod | `./deploy/deploy-to-environment.sh prod 1.4` | The script prints OK and the canary answers on 8202 | `./deploy/set-weight.sh 0` |
| 4 | Weight 10 | `./deploy/set-weight.sh 10` | The script prints OK | `./deploy/set-weight.sh 0` |
| 5 | Watch | `./deploy/check-menu.sh` | The script prints OK: every call returned 200 | `./deploy/set-weight.sh 0` |
| 6 | Weight 50 | `./deploy/set-weight.sh 50` | The script prints OK | `./deploy/set-weight.sh 0` |
| 7 | Weight 100 | `./deploy/set-weight.sh 100` | The script prints OK | `./deploy/set-weight.sh 0` |

Time to roll back (measure it and write it here): ___ seconds.

## Notes

- Version 1.4 is broken on purpose. The watch step (5) finds `500` answers from `/menu`, so the way back is `./deploy/set-weight.sh 0`. Steps 6 and 7 are never reached in class.
- With a good version, the same runbook goes all the way to step 7.
