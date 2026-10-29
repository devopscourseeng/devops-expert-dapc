# Deploy scripts

## deploy-to-environment.sh VERSION

Puts one published version of the Summit Cafe API in the **new** slot.

```
./deploy/deploy-to-environment.sh 1.2
```

- It pulls `ghcr.io/devopscourseeng/devops-expert-dapc/summit-cafe-api:1.2`.
- It replaces the container `cafe-new` and publishes it on port 8002.
- It waits until `/health` answers. If it does not, it stops with an error.
- It does **not** touch the stable slot and does **not** change the nginx
  weights. Customers do not see the new version until the weights change.
- It refuses `latest`. Use a version number only, such as `1.2` or `1.2.3`.

To put the last good version back in the new slot: `./deploy/deploy-to-environment.sh 1.1`.

To see what it would do without changing anything: `DRY_RUN=1 ./deploy/deploy-to-environment.sh 1.2`.

You need Docker running and a published image (see `.github/workflows/README.md`).

## Practice environment with nginx

Two slots behind one nginx proxy:

| Container | Port | What it is |
|---|---|---|
| `cafe-stable` | 8001 | the version customers use now |
| `cafe-new` | 8002 | the version you are releasing |
| `cafe-proxy` | 8080 | nginx, splits the calls between the two slots |

Always call the app through port 8080.

```
./deploy/start-environment.sh 1.1        # stable = 1.1, 100% of calls
./deploy/deploy-to-environment.sh 1.2    # new slot = 1.2, still 0% of calls
./deploy/set-weight.sh 10                # canary: 10% new, 90% stable
./deploy/set-weight.sh 50                # half and half
./deploy/set-weight.sh 100               # everyone on 1.2
./deploy/set-weight.sh 0                 # roll back: everyone on stable
```

The weight is the percent of calls that go to the **new** slot. At 0 or 100 nginx
marks the other slot as `down`, because nginx does not accept a weight of 0.

All scripts accept `DRY_RUN=1` to print what they would do.

Clean up: `docker rm -f cafe-proxy cafe-stable cafe-new`

Windows: these are bash scripts. Run them in Git Bash or WSL, not in CMD.
