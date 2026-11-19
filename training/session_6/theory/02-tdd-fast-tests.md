# TDD and fast, reliable tests

Pair B · Session 6 · "Theory with Claude"

## Step 1. What Claude would say

**The idea.** Test-driven development (TDD) means writing the automated test first. The test describes the behaviour we expect. We run it and watch it fail (red). Then we write the smallest code that makes it pass (green). Then we clean up the code without changing what it does (refactor), and the tests stay green. Fast, reliable tests make this loop practical, because a slow or flaky test gets ignored.

**How to get there.** Pick the next small behaviour. Write its test and run it. Write only enough code to pass. Commit each step. Keep tests fast: no real network, no waiting. Keep them reliable: the same input gives the same result every time. If a test sometimes fails for no reason, fix it or remove it, because people stop trusting the suite.

**Example from the Summit Cafe API.**

- Behaviour: `DELETE /orders/{id}` returns 204 for an existing order.
- Red: write the test. It fails, because the route does not exist yet.
- Green: add the smallest route that deletes the order and returns 204.
- Refactor: move the storage code into a small helper, and the test still passes.

**One sentence to remember.** Write the failing test first, make it pass, then clean up.

## Step 2. Check against the official pages (99, 100, 108, 110, 113)

**Where to look.**

- Page 99: fast and reliable tests; find errors as early as possible; run tests fast, in parallel if needed; write tests before code (TDD).
- Page 100: automate as many manual tests as possible; pull the Andon cord when the pipeline breaks.
- Page 108: TDD and ATDD (acceptance test-driven development). Kent Beck (1990, Extreme Programming) describes three steps. The official slide numbers them 2, 3 and 4; the usual numbering is 1 to 3: make the test fail, make it pass, refactor new and old code.
- Page 110: a small number of reliable automated tests is usually preferable to many unreliable ones. Start small and add over time.
- Page 113: the Andon cord. When a change breaks the build or the tests, no new work enters until it is fixed.

**Compare with Step 1.**

- Does the answer describe the cycle in the right order: test first, fail, pass, refactor? It should.
- Does it mention that the test must fail for the right reason? This is often forgotten.
- Does it say reliable and fast, not only "automated"? Page 110 is the source for that point.
- Does it link flaky tests to the Andon cord (page 113)? This is the connection participants usually miss.

**Watch out for.** Our course rule "one commit per cycle" is our rule, not the official one. Say so if asked.

## Your turn (steps 3, 4 and 5)

Prepare five minutes: the idea, one example from the Summit Cafe API, and the points above. Present to the group. Then talk together: what was right, and what was missing?
