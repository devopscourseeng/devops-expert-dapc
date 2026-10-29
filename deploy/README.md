# Deploy scripts

## deploy.sh VERSION

Puts one published version of the Summit Cafe API in the **new** slot.

```
./deploy/deploy.sh 1.2
```

- It pulls `ghcr.io/devopscourseeng/devops-expert-dapc/summit-cafe-api:1.2`.
- It replaces the container `cafe-new` and publishes it on port 8002.
- It waits until `/health` answers. If it does not, it stops with an error.
- It does **not** touch the stable slot and does **not** change the nginx
  weights. Customers do not see the new version until the weights change.
- It refuses `latest`. Use a version number only, such as `1.2` or `1.2.3`.

To go back to the last good version in the new slot: `./deploy/deploy.sh 1.1`.

To see what it would do without changing anything: `DRY_RUN=1 ./deploy/deploy.sh 1.2`.

You need Docker running and a published image (see `.github/workflows/README.md`).
