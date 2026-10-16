# The Second Way: Feedback

Pair 2 · Session 5 · "Teach one of the Three Ways in three minutes"

## Step 1. What Claude would say

**The idea.** The Second Way creates fast and constant feedback from right to left: from the customer and from production back to the people who made the change. The goal is to make feedback loops short and strong, so problems are seen when they happen and fixed while they are still small and cheap. Quality is built in from the start, not checked only at the end.

**How to get there.** See problems as they happen, with monitoring (telemetry) and automatic tests. When a problem appears, the team stops and fixes it together (this is called swarming), and shares what it learned. Put quality checks as early as possible. Think about the people who receive your work next (downstream) and make their job easier.

**Example from the Summit Cafe API.**

- A unit test fails on a pull request after a few minutes, so the author fixes it before it affects anyone else.
- A required review gives a second pair of eyes before the change is merged.
- In Session 8 we add metrics and dashboards, so we can see how the café's API behaves in production.
- If an alert starts, the team stops and works on it together, then writes down what they learned.

**One sentence to remember.** Feedback means: find out fast, fix it at the source.

## Step 2. Check against the official slides (64 to 76)

**Where to look.** Slides 72 and 73.

**What the slides say, in short.**

- Slide 72 presents the Second Way. Its quote says that the goal of almost any process improvement is to make feedback loops shorter and stronger, so corrections can be made all the time.
- Slide 73 lists the five capabilities of the Second Way. A capability is a skill or ability that a team needs.

**The five capabilities** (the order on the slide may be different):

1. See problems as they happen
2. Swarm (work together) to solve problems and build new knowledge
3. Keep pushing quality closer to the source
4. Make things better for the next teams in the chain (downstream)
5. Work safely in complex systems

**Compare with Step 1.**

- Is the direction right (right to left)? Is the purpose clear (short and strong feedback loops)?
- Does it cover **swarming**, **downstream teams** and **working safely in complex systems**? These are easy to forget, because most people think only of tests and monitoring.
- Is the Summit Cafe API example really feedback, and not flow? A test that runs on every change is feedback. Merging small changes is flow.

**Watch out for.** Feedback is not only monitoring in production. It also includes tests, reviews and any early signal that something is wrong.

## Your turn (Steps 3, 4 and 5)

Prepare three minutes: the idea, one example, and the skills (capabilities) it needs. Present to the group. Then talk together: what was right, and what was missing?
