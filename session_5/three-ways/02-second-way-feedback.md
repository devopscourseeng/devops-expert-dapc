# The Second Way: Feedback

Pair 2 · Session 5 · "Explain a Way in three minutes"

## Step 1. What Claude would say

**The idea.** The Second Way creates fast, constant feedback from right to left: from the customer and from production back to the people who made the change. The goal is to shorten and amplify feedback loops, so problems are seen when they happen and fixed while they are small and cheap. Quality is built in at the source instead of being inspected at the end.

**How to get there.** See problems as they occur, using telemetry, monitoring and automated tests. Swarm on a problem: stop and fix it together, and share what you learn. Push quality closer to the source, with checks as early as possible. Think about the people who receive your work next (downstream) and make their job easier.

**Example from Café Cumbre.**

- A unit test fails on a pull request within minutes, so the author fixes it before anyone else is affected.
- A required review gives a second pair of eyes before the change is merged.
- In Session 8 we add metrics and dashboards, so we see how the café's API behaves in production.
- If an alert fires, the team stops and handles it together, then writes down what they learned.

**One sentence to remember.** Feedback means: find out fast, fix it at the source.

## Step 2. Check against the official slides (64 to 76)

**Where to look.** Slides 72 and 73.

**What the slides say, in short.**

- Slide 72 presents the Second Way. Its quote says that the goal of almost any process improvement is to shorten and amplify feedback loops so corrections can be made continually.
- Slide 73 lists the five capabilities of the Second Way.

**The five capabilities** (the order may differ from this one):

1. See problems as they occur
2. Swarm and solve problems to build new knowledge
3. Keep pushing quality closer to the source
4. Enable optimization for downstream work centers
5. Work safely within complex systems

**Compare with Step 1.**

- Did the explanation get the direction right (right to left) and the purpose (short, amplified feedback loops)?
- Did it cover **swarming**, **downstream work centers** and **working safely in complex systems**? These are easy to miss, because people usually think only of tests and monitoring.
- Is the Café Cumbre example really feedback and not flow? A test that runs on every change is feedback. Merging small changes is flow.

**Watch out for.** Feedback is not only monitoring in production. It also includes tests, reviews and any early signal that something is wrong.

## Your turn (Steps 3, 4, 5)

Prepare for three minutes: the idea, one example, the capabilities it needs. Present to the group, then join the debrief: what was right, what was missing?
