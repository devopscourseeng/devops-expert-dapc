# Deploy scripts

Two environments run on your own computer with Docker:

| Environment | Container | Port | What it is |
|---|---|---|---|
| staging | `cafe-staging` | 8100 | The test place. One container, no proxy. |
| prod | `cafe-prod-stable` | 8201 | The version customers use now |
| prod | `cafe-prod-canary` | 8202 | The version being released |
| prod | `cafe-prod` | 8200 | nginx, splits the calls between stable and canary |

In prod, always call the app through port **8200**.

## deploy-to-environment.sh ENVIRONMENT VERSION

Deploys one published version.

```
./deploy/deploy-to-environment.sh staging 1.2
./deploy/deploy-to-environment.sh prod 1.2
```

- It pulls `ghcr.io/devopscourseeng/devops-expert-dapc/summit-cafe-api:1.2`.
- `staging` replaces `cafe-staging`. `prod` replaces `cafe-prod-canary`.
- It waits until `/health` answers. If it does not, it stops with an error.
- In prod it does **not** touch `cafe-prod-stable` and does **not** change the
  nginx weights. Customers do not see the new version until you change the weights.
- It refuses `latest`. Use a version number only, such as `1.2` or `1.2.3`.

To put the last good version back: `./deploy/deploy-to-environment.sh prod 1.1`.

## start-environment.sh STABLE_VERSION

Starts prod: `cafe-prod-stable` with that version and the `cafe-prod` proxy,
with 100% of the calls going to stable.

## set-weight.sh PERCENT

Sets the percent of prod calls that go to the **canary**. The rest goes to stable.
At 0 or 100 nginx marks the other side as `down`, because nginx does not accept a
weight of 0. Before reloading, the script tests the new config inside the proxy.

## check-menu.sh [CALLS]

The "watch" step. It calls `/menu` through the prod proxy (port 8200) 20 times (or CALLS times) and counts the status codes. It prints `OK` and exits with 0 if every call returned 200. Otherwise it says how many calls failed and exits with 1.

## A full release

```
./deploy/start-environment.sh 1.1               # prod: stable = 1.1, 100% of calls
./deploy/deploy-to-environment.sh staging 1.2   # test 1.2 first
curl http://localhost:8100/menu
./deploy/deploy-to-environment.sh prod 1.2      # canary = 1.2, still 0% of calls
./deploy/set-weight.sh 10                       # canary: 10% of calls
./deploy/check-menu.sh                          # watch: are all calls 200?
./deploy/set-weight.sh 50                       # half and half
./deploy/set-weight.sh 100                      # everyone on 1.2
./deploy/set-weight.sh 0                        # roll back: everyone on stable
curl http://localhost:8200/menu                 # always through the proxy
```

All scripts accept `DRY_RUN=1` to print what they would do.

Clean up: `docker rm -f cafe-prod cafe-prod-stable cafe-prod-canary cafe-staging`

You need Docker running and a published image (see `.github/workflows/README.md`).
Windows: these are bash scripts. Run them in Git Bash or WSL, not in CMD.
