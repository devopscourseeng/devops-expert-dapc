# Environment-based patterns

Team B · Session 7 · "Theory with Claude"

## Step 1. What Claude would say

**The idea.** Environment-based patterns lower risk by changing where the new code runs. You have two or more environments, but only one receives customer traffic. You deploy the new version to an environment that has no customers, check it, and then release by moving traffic to it. Because traffic is moved by a router or a load balancer, going back is moving the traffic back.

**Blue-green.** There are two production environments, blue and green. Only one serves customers at a time. You deploy to the idle one, test it, and switch the router. If something is wrong, you switch back.

**The database problem.** Two versions of the app that share one database can break each other. There are two general answers: use two databases, or separate database changes from application changes. The second answer is called expand and contract. First you expand: you add new columns or tables and keep the old ones. Later you contract: you remove the old ones when no version uses them.

**Canary.** You release to a small group first, watch the result, and only then move to a bigger group. If something looks wrong, you go back. The name comes from canaries that miners took into mines: the bird showed the danger first. Facebook used groups like this: a small set of users, then its own employees, then most of the users.

**Cluster immune system.** It extends the canary pattern by connecting production monitoring to the release process and by rolling back the code automatically. Two benefits: it protects against defects that are hard to find, and it shortens the time to notice and react to bad performance.

**Example from the Summit Cafe API.**

- Environments: staging (port 8100) and prod, with `cafe-prod-stable` (8201), `cafe-prod-canary` (8202) and the nginx proxy `cafe-prod` (8200).
- Blue-green: all calls go to one side (`set-weight.sh 0` or `100`), and a switch moves them to the other side.
- Canary: `./deploy/set-weight.sh 10`, then `50`, then `100`. `curl http://localhost:8200/version` shows which version answered.
- Rollback: `./deploy/set-weight.sh 0`.
- Immune system: a skill that reads the runbook, watches the errors and suggests the rollback. In our practice a person approves the rollback.

**One sentence to remember.** Deploy where no customer is, then move the customers a little at a time.

## Step 2. Check against the official pages (142–150)

**Where to look.**

- Pages 142–144: two big families of release patterns: environment-based (only one environment gets live traffic; the release is moving the traffic) and application-based (the app is changed so features can be exposed selectively).
- Page 145: the effect of decoupling deploys from releases: no deploys in the middle of the night or on weekends, deploys in normal working hours, lower release risk and a shorter lead time.
- Page 146: blue-green is the simplest of the three patterns: two production environments, only one serves customers at a time.
- Page 147: dealing with database changes: two databases, or separate database changes from application changes (expand and contract: do not mutate objects; first add new ones, then remove the old ones).
- Page 148: the canary pattern: automate promotion to bigger and more critical environments, with planned confirmations, watch the performance in each environment, go back if something looks wrong, otherwise go to the next one. The origin of the name is the canary in the coal mine.
- Page 149: Facebook's groups: a small set of users, the company's employees, and then most of the users, with a router or load balancer.
- Page 150: the cluster immune system: canary plus production monitoring plus automatic rollback. Two benefits (hard-to-find defects, faster response).

**Compare with Step 1.**

- Does the answer say that only one environment receives customer traffic? It should.
- Does it mention the database problem and expand and contract? This is often forgotten.
- Does it describe canary as a series of bigger groups with a check between them?
- Does it say what is new in the immune system (monitoring connected to release, automatic rollback)?

**Watch out for.** In our practice we use weights on one proxy, which gives a percent of calls. The official canary talks about groups of users or environments. Both are canary: what matters is a small group first, a check, and a way back.

## Your turn (steps 3, 4 and 5)

Prepare one example from the Summit Cafe API, teach the others for about 5 minutes, and then talk together: which pattern would you choose for a database change, and why?
