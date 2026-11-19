# Test types and the pyramid

Pair A · Session 6 · "Theory with Claude"

## Step 1. What Claude would say

**The idea.** Tests come in layers. The base is many small, fast unit tests. Above them come fewer integration and acceptance tests, which check that parts work together. At the top are few manual or UI tests, which are slow and costly. The shape should be a pyramid, not an ice-cream cone. Each layer should catch errors as early and cheaply as possible.

**How to get there.** Write most tests as unit tests. Use API or integration tests to check that the pieces work together. Keep manual and UI checks for what truly needs a person (exploratory testing). Keep the code loosely coupled, so each module can be tested alone. If a unit test is hard to write, the design is often the problem.

**Example from the Summit Cafe API.**

- Unit test: the total of an order is 2 × 3.50 + 1 × 2.80 = 9.80. No server, no HTTP.
- API test: `POST /orders` returns status 201 and the right total. Uses Flask's test client.
- Manual check: a person opens the menu in a browser and reads it. Few of these, and only when needed.
- Anti-pattern: if most of our checks were manual, every change would wait for a person.

**One sentence to remember.** Many fast tests at the bottom, few slow tests at the top.

## Step 2. Check against the official pages (99, 102, 105–107, 110)

**Where to look.**

- Page 102: the DevOps test types: unit, integration, visual, functional, performance.
- Page 105: the categories, from simplest to most complex to implement: unit, integration, acceptance.
- Page 106: if most errors are found by acceptance and integration tests, feedback is slow. Whenever such a test finds an error, write a unit test that finds it faster, earlier and more cheaply.
- Page 107: the "ice-cream cone" anti-pattern and the ideal pyramid. A sign of strong coupling is unexpected effects in other modules and unit and acceptance tests that are hard and costly to write.
- Page 110: automate as many manual tests as possible, but quality cannot be automated. A small number of reliable tests is usually better than many unreliable ones.
- Page 99: tests should be fast and reliable, and should run in parallel when needed.

**Compare with Step 1.**

- Does the answer name the layers and the direction (many unit tests at the base)? It should.
- Does it mention the rule on page 106 (write a unit test after a higher-level test finds a bug)? This is often forgotten.
- Does it connect the pyramid to coupling (page 107)? This is the design point that is easy to miss.
- Does it say automation is not everything (page 110)? People still do exploratory testing.

**Watch out for.** The pyramid is a shape to aim for, not a rule that all tests must be unit tests. Integration tests are needed too.

## Your turn (steps 3, 4 and 5)

Prepare five minutes: the idea, one example from the Summit Cafe API, and the points above. Present to the group. Then talk together: what was right, and what was missing?
