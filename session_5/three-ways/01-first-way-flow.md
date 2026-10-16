# The First Way: Flow

Pair 1 · Session 5 · "Explain a Way in three minutes"

## Step 1. What Claude would say

**The idea.** The First Way looks at the whole system, not at one team or department. Work moves from left to right: from an idea in the business, through Development and Operations, to the customer. The goal is to make that journey fast and smooth, so value reaches the customer sooner. Making one silo faster does not help if the work then waits in the next queue.

**How to get there.** Make the work visible, work in small batches, limit how much work is in progress, reduce handoffs between people and teams, and keep removing the biggest bottleneck. Technical practices that support this: a deployment pipeline, automated tests, continuous integration and low-risk releases.

**Example from Café Cumbre.**

- A change to the café's menu page is one small pull request, not a week of work saved up for a big release.
- The ticket on the SCRUM board shows where the work is: To Do, In Progress or Done. Everyone can see it.
- Continuous integration builds and tests the change automatically, so nobody waits for a manual check.
- Docker Compose starts the full environment with one command, so there is no waiting for someone to prepare a server.
- Only a few tickets are In Progress at a time. A finished ticket is better than five half-finished ones.

**One sentence to remember.** Flow means: small changes, visible work, no waiting.

## Step 2. Check against the official slides (64 to 76)

**Where to look.** Slides 69 to 71.

**What the slides say, in short.**

- Slide 69 presents the First Way as flow, with a quote that stresses the performance of the whole system instead of a single silo, and the value for the customer.
- Slide 70 shows work moving end to end through stages (from a suspected need to a need satisfied), with a Kanban-style view of the system and its lead time.
- Slide 71 lists the seven capabilities of the First Way.

**The seven capabilities** (the slide shows them as a numbered list; the order may differ from this one):

1. Identify the value streams
2. Make our work visible
3. Limit work in progress (WIP)
4. Reduce the number of handoffs
5. Remove obstacles and waste in the value stream
6. Continually identify and elevate our constraints
7. Reduce batch size

**Compare with Step 1.**

- Did the explanation cover the idea of the whole system and the left-to-right direction? It should.
- It mentions visible work, small batches, WIP and handoffs. Did it mention **value streams** and **constraints**? These two are often missed.
- Did it say that Flow is more than automation? Automation helps, but the Way is about how work flows across the whole value stream.

**Watch out for.** Mixing up the direction: Flow goes **left to right** (idea to customer). Feedback goes right to left.

## Your turn (Steps 3, 4, 5)

Prepare for three minutes: the idea, one example, the capabilities it needs. Present to the group, then join the debrief: what was right, what was missing?
