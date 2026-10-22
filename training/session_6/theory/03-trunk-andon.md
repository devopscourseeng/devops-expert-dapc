# Trunk-based development (official) vs our develop flow, and the Andon cord

Pair C · Session 6 · "Theory with Claude"

## Step 1. What Claude would say

**The idea.** Integrate often. Long-lived branches make merging slow and painful: the longer a branch lives, the harder it is to combine with everyone else's changes, and the next merge gets worse. The official model, trunk-based development, has developers commit to the trunk at least once a day. A change reaches the trunk only if all automated tests pass ("blocked commits"). The Andon cord fits here: when the build breaks, no new work enters until it is fixed.

**How this course works.** We use the same goal, with a different trunk: `develop`. Each ticket gets a short branch from `develop`. It returns through a pull request, with CI green and a classmate's review. The required checks block a merge that fails. The model is not the official trunk-based one, because we have a `develop` branch and we do not commit to it directly.

**Example from the Summit Cafe API.**

- Long-lived branch: a branch for "orders" that lives for two weeks. When it is merged, it conflicts with three other changes.
- Our flow: a branch `feature/SCRUM-N` that lives for one day. Its PR is merged into `develop` once `Checks` is green.
- Andon cord: a PR breaks `pytest`. Nobody opens another PR until the test is fixed, and anyone who needs help brings it in.

**One sentence to remember.** Integrate often, with automated checks, and stop the line when it breaks.

## Step 2. Check against the official pages (113, 115–117, 121–123)

**Where to look.**

- Page 113: the Andon cord. A virtual Andon cord: when a change breaks the build or the tests, no new work enters until the problem is fixed. If someone needs help, bring in the help they need.
- Page 115: small batches; infrequent commits to the trunk cause problems.
- Page 116: long-lived branches. Integration gets exponentially harder, integration problems mean much rework, and a painful merge is done less often, which makes the next one worse.
- Page 117: continuous integration makes integration part of daily work. Quote: "without automated tests, continuous integration is the fastest way to get a large pile of electronic junk."
- Pages 121–122: two strategies. Optimize for individual productivity (private branches): merging becomes a nightmare. Optimize for team productivity (one trunk): verify often, and blocked commits, where a change reaches the trunk only if all automated tests pass first.
- Page 123: developers commit to the trunk at least once a day. Definition of "done": integrated, tested, working, potentially usable, built from the trunk with one click, validated by automated tests.

**Compare with Step 1.**

- Does the answer name the official model as "trunk-based development" and our model as the develop flow? It should, so the two are not confused.
- Does it explain blocked commits (page 122), which apply to both models? This is often missing.
- Does it say why `develop` stays in this course (plan decision) and what we keep from the official model: short branches, frequent integration, automated checks?
- Does it tie the Andon cord to the red build? It should, with the rule from page 113.

**Watch out for.** Do not say the official model is wrong, and do not say our model is the official one. The official material recommends a daily commit to the trunk. Our course uses short branches from `develop` with pull requests. Both aim at the same thing: small, frequent, tested integration.

## Your turn (steps 3, 4 and 5)

Prepare five minutes: the idea, one example from the Summit Cafe API, and the points above. Present to the group. Then talk together: what was right, and what was missing?
