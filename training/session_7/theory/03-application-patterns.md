# Application-based patterns

Team C · Session 7 · "Theory with Claude"

## Step 1. What Claude would say

**The idea.** Application-based patterns lower risk by changing who sees a feature. The code of the feature is in the version that is deployed, but the app has a switch that decides if the feature is on. You release by turning the switch on, without a new deploy. You go back by turning it off.

**Feature toggles.** A feature toggle is a way to turn a feature on or off without deploying production code. It makes rollback easy, lets the system lose a feature in a controlled way instead of failing completely, and helps a service-oriented architecture to be more resilient. It also asks for more discipline from developers: old toggles must be removed, or they become clutter.

**Dark launches.** With a toggle you can deploy a feature to production without customers seeing it. This is a dark launch. The feature is fully deployed and can be tested in production, but it is invisible to customers. For big or risky changes, teams do this for weeks before the release, so they can test the expected production load in a safe way.

**Example from the Summit Cafe API.**

- Version 1.2 has the toggle `SCHEDULED_ORDERS`. It is `off` by default.
- With `off`, `POST /orders` ignores `pickup_time`, so the API acts as in 1.1. The code is deployed but the feature is hidden: that is the dark launch.
- With `on`, an order can have a `pickup_time` such as `14:30`. A bad time returns a 400 error.
- `GET /version` shows the version and the state of the toggle.
- The toggle changes with an environment variable: restart the container with `-e SCHEDULED_ORDERS=on`. The image is the same.

**One sentence to remember.** Ship the code first, turn the feature on later, and remove the toggle when it is no longer needed.

## Step 2. Check against the official pages (151–153)

**Where to look.**

- Page 151: application-based release patterns give more flexibility to release new features safely, usually one feature at a time. They ask for more discipline and more involvement from Development.
- Page 152: feature toggles are a mechanism to turn features on and off selectively without a production code deploy. They also allow us to go back easily, to degrade performance gracefully, and to be more resilient through a service-oriented architecture.
- Page 153: dark launches. Toggles let us deploy features to production without users being able to reach them. The full feature is in production, we test it, and customers still do not see it. For big or risky changes, this is often done for weeks before the release.

**Compare with Step 1.**

- Does the answer say that a toggle works without deploying new production code? It should.
- Does it list the three benefits (easy rollback, graceful degradation, resilience)?
- Does it explain that a dark launch means the feature is in production but invisible?
- Does it mention the cost: more discipline from Development?

**Watch out for.** A toggle that stays forever becomes clutter and a source of mistakes. Remove old toggles when the feature is released for everyone. This point is our advice and is not on the official pages.

## Your turn (steps 3, 4 and 5)

Prepare one example from the Summit Cafe API, teach the others for about 5 minutes, and then talk together: which feature in our own product would you ship dark first?
