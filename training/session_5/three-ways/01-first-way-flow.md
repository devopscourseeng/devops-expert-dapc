# The First Way: Flow

Pair 1 · Session 5 · "Teach one of the Three Ways in three minutes"

## Step 1. What Claude would say

**The idea.** The First Way looks at the whole system, not at one team. Work moves from left to right: from an idea, through Development and Operations, to the customer. The goal is to make this trip fast and smooth, so the customer gets value sooner. Making one team faster does not help if the work then waits in the next team's queue.

**How to get there.** Show the work so everyone can see it. Work in small pieces. Do not start too many things at once (this is called limiting work in progress, or WIP). Reduce the number of times work passes from one person or team to another (handoffs). Find the biggest bottleneck and fix it. Some technical practices help: a deployment pipeline, automatic tests, continuous integration (CI) and safe releases.

**Example from the Summit Cafe API.**

- A change to the café's menu page is one small pull request. We do not save a week of work for one big release.
- The ticket on the SCRUM board shows where the work is: To Do, In Progress or Done. Everyone can see it.
- CI builds and tests the change automatically, so nobody waits for a manual check.
- Docker Compose starts the full environment with one command, so nobody waits for a server.
- Only a few tickets are In Progress at a time. One finished ticket is better than five half-finished ones.

**One sentence to remember.** Flow means: small changes, visible work, no waiting.

## Step 2. Check against the official slides (64 to 76)

**Where to look.** Slides 69 to 71.

**What the slides say, in short.**

- Slide 69 presents the First Way. Its quote says the focus is the whole system, not one department, and the value for the customer.
- Slide 70 shows work moving from start to end through stages, from a need to a satisfied need, with a Kanban view and the lead time (the total time the work takes).
- Slide 71 lists the seven capabilities of the First Way. A capability is a skill or ability that a team needs.

**The seven capabilities** (the order on the slide may be different):

1. Identify the value streams (the steps that turn an idea into value for the customer)
2. Make our work visible
3. Limit work in progress (WIP)
4. Reduce the number of handoffs
5. Remove obstacles and waste
6. Always find and fix our constraints (the bottlenecks)
7. Reduce the size of the batches (work in small pieces)

**Compare with Step 1.**

- Does the explanation talk about the whole system and the left-to-right direction? It should.
- It mentions visible work, small pieces, WIP and handoffs. Does it mention **value streams** and **constraints**? These two are often forgotten.
- Does it say that Flow is more than automation? Automation helps, but the Way is about how work moves through the whole value stream.

**Watch out for.** Do not mix up the direction. Flow goes **left to right** (from idea to customer). Feedback goes right to left.

## Your turn (Steps 3, 4 and 5)

Prepare three minutes: the idea, one example, and the skills (capabilities) it needs. Present to the group. Then talk together: what was right, and what was missing?
