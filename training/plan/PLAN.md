# Global Plan — DAPC Course, Sessions 5–16 (v0.2, draft for review)

Status: **draft**. Session 5 is approved. Sessions 6–16 follow the same structure and are pending review.

This plan replaces the plan for sessions 5–16 in the original global plan (v1.0). Sessions 1–4 are completed (see [CONTEXT.md](../CONTEXT.md)).

## 1. How the course works from session 5

- **Format:** 12 sessions (5–16) of 4 hours, live online, 6 participants in two teams of 3.
- **Session leads:** Patricia leads sessions 6 and 12 (quality focus: tests and peer review). The main instructor leads all the others.
- **Tools:** one shared GitHub repo (`devopscourseeng/devops-expert-dapc`), one Jira project (key **SCRUM**), and **Claude** as the only AI tool (every participant needs a Pro plan).
- **Learning by doing:** the instructor talks about 20–30 minutes per session. Participants build the theory themselves with Claude, check it against the official CertiProf material, and apply it on real tickets.
- **Everything goes through tickets and pull requests:** a `SCRUM-N` ticket, a short branch from `develop` named `feature/SCRUM-N` or `bugfix/SCRUM-N`, a PR to `develop` with CI green, a review by a classmate, and a closing comment in Jira.
- **Skills:** session 5 introduces the idea with a group discussion. From session 6 on, in every session participants turn something they learned into a Claude skill and contribute it to the repo.
- **Thread project:** *Summit Cafe API* (Flask REST API, Docker, deployed to Render) lives in `src/summit-cafe-api/`. Each session adds a capability to it.
- **Language:** all materials are in English.

## 2. Assessment: the work trail

There are **no exams or quizzes**. Assessment is entirely practical and automated, based on what each participant leaves in GitHub and Jira:

| Signal | Where it is measured |
|---|---|
| PRs linked to a `SCRUM-N` ticket, CI green, small and focused | GitHub |
| Reviews and comments on classmates' PRs | GitHub |
| Closing comments in tickets: what was done, evidence, what was learned | Jira |
| Skills contributed to the repo | GitHub |
| Attendance and participation in team activities | Session log |

At the end of the course the instructor runs a skill that measures each participant's activity in Jira and GitHub. The exact scoring (weights and thresholds) is **to be defined** and added to this plan in a separate PR. The signals above are fixed so participants know from session 5 what counts.

Optional, outside the grade: the official CertiProf DAPC exam (40 multiple-choice questions, 60 minutes, 80 % to pass). Session 16 includes a non-graded practice with the sample exam.

## 3. Session overview

| Session | Lead | Theme | DAPC slides | Syllabus unit | Project capability added |
|---|---|---|---|---|---|
| S5 | Instructor | Kickoff: Claude, GitHub and Jira as the way of working | 64–76 (recap) | 2 | First ticket closed through a PR |
| S6 | Patricia | Tests, TDD, continuous integration and trunk-based development | 99–128 | 3 | Real CI pipeline with tests that block merges |
| S7 | Instructor | Low-risk releases | 129–154 | 3 | Self-service deploy, blue-green, canary, feature toggles |
| S8 | Instructor | Low-risk architecture and the end of the First Way | 155–159 | 3 | Inventory service extracted (strangler pattern); value stream map |
| S9 | Instructor | Telemetry | 160–173 | 4 | Metrics in Prometheus and Grafana dashboards |
| S10 | Instructor | Logs, information radiators and predictive analysis | 174–182 | 4 | Structured logs, correlation id, radiator and alerts |
| S11 | Instructor | Feedback to deploy safely: LRR and HRR | 183–194 | 4 | Watched canary with automatic rollback; LRR checklist |
| S12 | Patricia | Hypotheses, A/B tests and peer review | 195–216 | 4 | A/B experiment; PR template, CODEOWNERS |
| S13 | Instructor | Learning culture and blameless postmortems | 217–225 | 5 | Postmortem template and first postmortem |
| S14 | Instructor | Resilience: fault injection and Game Day | 226–235 | 5 | Timeouts, retries, runbooks tested in a Game Day |
| S15 | Instructor | Local discoveries, global improvements | 236–252 | 5 | Reusable workflow, repo template, DORA metrics |
| S16 | Instructor | Security, change management, compliance and course close | 253–273 | 6 | DevSecOps pipeline, SBOM, automatic change record |

Slide numbers refer to the CertiProf instructor PDF (V072021A). The old plan's three assessment sessions (4, 8, 12) and the final exam session are removed; their time goes to practice.

## 4. Session plans

Every session has the same shape (the minutes add up to 240):

- **Opening:** review the work trail of the previous session.
- **Theory built by the participants** with Claude, in teams.
- **Hands-on tickets** on the Summit Cafe API.
- **Team activity.**
- **Skill creation** (from session 6).
- **Wrap-up and buffer.**

---

### Session 5 — Kickoff: Claude, GitHub and Jira as the way of working
**Session lead:** Instructor


**Goal:** by the end, each participant has Claude connected to GitHub and Jira, has closed one ticket through a PR, and understands how their work is checked.

| Block | Min | Who talks |
|---|---|---|
| **Get to know each other:** four questions for each participant (job today, tools used, AI use, expectations) | 30 | Participants |
| **Course rules:** the course in four numbers, the path every change follows, how the work trail shows progress, the branching strategy (`main` and `develop`) and best practices | 20 | Instructor |
| **Setup with Claude:** accept the repo and Jira invites, open Claude, connect GitHub and Jira, check that Claude can see the repo and the tickets (guide: `training/docs/setup-tools.md`) | 60 | Participants |
| Break | 10 | |
| **First real ticket:** take it in Jira, branch from `develop`, solve it with Claude, open the PR, tests pass, classmate review, closing comment in Jira | 60 | Participants |
| **The Three Ways with Claude** (slides 64–76, recap): each pair asks Claude to explain one Way, checks it against the official material and teaches it in 3 minutes, then the group talks about what Claude got right or missed | 30 | Pairs |
| **What is a skill?** Group discussion: what a skill is, which repeated tasks we could automate with one, and confirmation that we build the first skill in session 6 | 20 | Everyone |
| Closing: outcomes, expectations check, next session | 10 | Instructor |

**Action Items**
None.

---

### Session 6 — Tests, TDD, continuous integration and trunk-based development
**Session lead:** Patricia


**Goal:** make the pipeline a safety net: automated tests that block bad changes, built with test-first discipline and small, frequent integrations.

| Block | Min | Who talks |
|---|---|---|
| Opening: review the work trail from session 5 (two or three shared PRs) | 15 | Instructor + participants |
| **Theory with Claude** (slides 99–127): test pyramid vs ice-cream cone, fast and reliable tests, TDD, the Andon cord, long-lived branches vs trunk-based development, shift left. Each team prepares a 5-minute explanation | 40 | Teams |
| Break | 10 | |
| **Tickets:** (a) write unit and API tests with pytest and coverage for the orders logic; (b) add a TDD feature in pairs (red-green-refactor, one commit per cycle); (c) extend CI so tests and `ruff` must pass before merge | 90 | Participants |
| Break | 10 | |
| **Discussion (slide 114):** who stops the line when the build breaks? Break a test on purpose and watch the PR get blocked. Teams decide their own "build is red" rule | 35 | Teams |
| **First skill:** every participant builds their first skill (introduced in session 5), for example "write a failing test first" or "review a PR for test quality" | 20 | Participants |
| Wrap-up and buffer | 20 | Instructor |

**Action Items:** orders endpoint in the Summit Cafe API (`src/summit-cafe-api/`) with a deliberate bug and empty test folder; tickets for the three exercises.

---

### Session 7 — Low-risk releases
**Session lead:** Instructor

**Goal:** separate deployment from release and learn the patterns that make releases boring: blue-green, canary and feature toggles. Then write the steps of a release as a runbook and let a skill run it, with the trainer's rules around it (harness engineering).

| Block | Min | Who talks |
|---|---|---|
| Opening: review the work trail from session 6 | 15 | Instructor + participants |
| **Theory with Claude** (slides 129–153): risky releases and self-service deploys (Team A), environment-based patterns: blue-green, canary, cluster immune system (Team B), application-based patterns: feature toggles and dark launches (Team C) | 45 | Teams |
| Break | 10 | |
| **Tickets (run it, then extend it):** first 10 minutes to set up Docker Desktop, a bash terminal and the repo. Then four tickets under the epic "Release version 1.2 with low risk", all with the label `session-N`: (a) the deploy script checks `/menu` and `/version` after a deploy; (b) blue-green: a command moves all calls to the other side and back, and the time is measured; (c) canary: 1.2 at 10, 50 and 100, and a script counts the versions in 20 calls; (d) feature toggle: 1.2 with `SCHEDULED_ORDERS` off and on, and a test | 85 | Participants |
| Break | 10 | |
| **Team activity:** roll out a new version as a canary, see the errors, and roll back with weight 0. Each team writes the steps, the checks and the way back in a runbook PR | 35 | Teams |
| **Skill:** "deploy from the runbook". The skill reads the runbook (context first, then one step per row), deploys, sets the weights, runs the check after each step, and suggests a rollback when a check fails. A person says yes. It runs only commands that are written in the runbook | 20 | Participants |
| Wrap-up and spare time | 20 | Instructor |

**Practice environment:** `staging` (port 8100) and `prod` with `cafe-prod-stable` (8201), `cafe-prod-canary` (8202) and an nginx proxy `cafe-prod` (8200). Scripts: `deploy/deploy-to-environment.sh ENVIRONMENT VERSION`, `deploy/start-environment.sh VERSION`, `deploy/set-weight.sh PERCENT`.

**Action Items:** images 1.1 and 1.2 published to GHCR (public package) and the broken release 1.3 published from the branch `trainer/broken-release-1.3`; Jira epic and four tickets with the label `session-7`; the setup guide sent to the participants. All details are in `training/session_7/`.

---|---|---|
| Opening: review the work trail from session 6 | 15 | Instructor + participants |
| **Theory with Claude** (slides 129–153): high-risk releases (Knight Capital case), self-service deploys, environment-based patterns (blue-green, canary, cluster immune system) and application-based patterns (feature toggles, dark launches) | 45 | Teams |
| Break | 10 | |
| **Tickets:** (a) `deploy-to-environment.sh VERSION` that pulls the image from GHCR and starts it; (b) blue-green with two API instances behind nginx; (c) canary with weighted upstreams 90/10, 50/50, 100; (d) a feature toggle that ships a feature turned off and enables it via an environment variable | 85 | Participants |
| Break | 10 | |
| **Team activity:** roll out version 1.2 as a canary and perform a deliberate rollback. Each team documents the steps and times in a runbook PR | 35 | Teams |
| **Skill:** "write a deployment runbook" | 20 | Participants |
| Wrap-up and buffer | 20 | Instructor |

**Action Items:** images published to GHCR with write permission for the participants; reference nginx configuration; version 1.2 of the API with a toggle.

---

### Session 8 — Low-risk architecture and the end of the First Way
**Session lead:** Instructor


**Goal:** understand how architecture enables or blocks flow, evolve a system without rewriting it, and find the constraint in the team's own pipeline.

| Block | Min | Who talks |
|---|---|---|
| Opening: review the work trail from session 7 | 15 | Instructor + participants |
| **Theory with Claude** (slides 155–158): evolutionary architecture, monolith vs microservices, the strangler pattern | 35 | Teams |
| Break | 10 | |
| **Tickets:** (a) extract `/productos` into an `inventory` service with its own Dockerfile and tests; (b) route `/api/productos` to it through nginx; (c) add a simple contract test; (d) retire the old code once traffic no longer reaches it | 90 | Participants |
| Break | 10 | |
| **Value stream map (slide 159):** each team maps its own pipeline from commit to production in Excalidraw (process time vs wait time, % complete and accurate, total lead time), finds the constraint and proposes a Kata-style experiment | 40 | Teams |
| **Skill:** "build a value stream map from CI run data" | 20 | Participants |
| Wrap-up and buffer | 20 | Instructor |

**Action Items:** Excalidraw template for the value stream map; the inventory-service ticket split into small tickets so six people can work in parallel.

---

### Session 9 — Telemetry
**Session lead:** Instructor


**Goal:** see the system. Understand why telemetry is a precondition for solving problems, and instrument the API.

| Block | Min | Who talks |
|---|---|---|
| Opening: review the work trail from session 8 | 15 | Instructor + participants |
| **Theory with Claude** (slides 160–173): why the Second Way, telemetry to see and solve problems, high performers resolving incidents faster, modern monitoring architecture, pipeline telemetry | 40 | Teams |
| Break | 10 | |
| **Tickets:** (a) add `prometheus-client` metrics (order counter, errors per endpoint, latency histogram) at `/metrics`; (b) add Prometheus and Grafana to Compose with a provisioned datasource; (c) first PromQL queries (`rate()`, `histogram_quantile()`); (d) a Grafana panel | 90 | Participants |
| Break | 10 | |
| **Team activity:** build a dashboard with the RED signals (rate, errors, duration p95) and one business metric; generate traffic with k6 and compare dashboards across teams | 35 | Teams |
| **Skill:** "add RED metrics to a service" | 20 | Participants |
| Wrap-up and buffer | 20 | Instructor |

**Action Items:** Compose profile for the observability stack (laptops need about 8 GB RAM; Codespaces as fallback); k6 script.

---

### Session 10 — Logs, information radiators and predictive analysis
**Session lead:** Instructor


**Goal:** design useful logs, build a radiator and actionable alerts, and apply simple statistics to detect anomalies.

| Block | Min | Who talks |
|---|---|---|
| Opening: review the work trail from session 9 | 15 | Instructor + participants |
| **Theory with Claude** (slides 174–182): log levels and which events to record, logs for incident analysis, information radiators, telemetry gaps by level, mean and standard deviation, the three-sigma rule and its limits | 35 | Teams |
| Break | 10 | |
| **Tickets:** (a) structured JSON logs with a correlation id generated by nginx and propagated by the API; (b) follow one request end to end with `docker compose logs` and `jq`; (c) Grafana kiosk radiator; (d) alert on error rate above 5 % for 2 minutes; (e) three-sigma band with `avg_over_time` and `stddev_over_time` | 95 | Participants |
| Break | 10 | |
| **Team activity: hunt the gaps.** Each team fills a telemetry matrix for the Summit Cafe API by level (business, application, infrastructure, client, pipeline, security); the other team points out what is missing | 35 | Teams |
| **Skill:** "write an alert with a mini runbook" | 20 | Participants |
| Wrap-up and buffer | 20 | Instructor |

**Action Items:** nginx config with correlation id; reference alert rules; telemetry matrix template.

---

### Session 11 — Feedback to deploy safely: LRR and HRR
**Session lead:** Instructor


**Goal:** use telemetry to decide whether a deployment continues or rolls back, and review a service for readiness to launch and to hand off.

| Block | Min | Who talks |
|---|---|---|
| Opening: review the work trail from session 10 | 15 | Instructor + participants |
| **Theory with Claude** (slides 183–194): feedback for safe deployments, watching metrics after a deploy, shared on-call, developers operating their own service, handing a service back, launch guidance, Launch Readiness Review (LRR) and Hand-Off Readiness Review (HRR) | 45 | Teams |
| Break | 10 | |
| **Tickets:** (a) release version 1.3, which contains a defect that causes errors in a fraction of requests, as a 10 % canary with the version as a metrics label; (b) compare the error rate per version in Grafana; (c) write `watch_canary.sh`, which queries the Prometheus API and rolls back automatically over a threshold; (d) release the fixed 1.3.1 | 85 | Participants |
| Break | 10 | |
| **Team activity: does it pass the LRR?** Each team writes the LRR/HRR checklist for the Summit Cafe API (defects, alerts, runbooks, capacity, dependencies, security) and reviews the other team's service: would they accept it on their on-call? | 35 | Teams |
| **Skill:** "run an LRR on a service" | 20 | Participants |
| Wrap-up and buffer | 20 | Instructor |

**Action Items:** version 1.3 of the API with the planted defect; reference watcher script; LRR/HRR checklist template.

---

### Session 12 — Hypotheses, A/B tests and peer review
**Session lead:** Patricia


**Goal:** treat features as measurable hypotheses, validate them with experiments, and design review processes that raise quality without slowing flow.

| Block | Min | Who talks |
|---|---|---|
| Opening: review the work trail from session 11 | 15 | Instructor + participants |
| **Theory with Claude** (slides 195–215): hypothesis-driven development and the hypothesis format (slide 200), A/B tests in features, releases and planning, GitHub flow, what makes a good PR, the dangers of too much control, peer review guidelines, pair programming | 40 | Teams |
| Break | 10 | |
| **Tickets:** (a) write the hypothesis ("We believe that [feature] will produce [outcome]; we will know when we see [measurable signal]"); (b) a toggle that splits customers 50/50 by a hash of their id between two variants; (c) a conversion metric per variant in Prometheus; (d) simulated traffic with k6 and a data-based decision; (e) PR template, `CODEOWNERS` and a one-approval rule on `main` | 85 | Participants |
| Break | 10 | |
| **Debate (slide 216):** one team defends peer review, the other defends a change advisory board, using the data from slides 205–207 and 211. Then each participant reviews another participant's experiment PR | 40 | Teams |
| **Skill:** "review a PR using the course guidelines" | 20 | Participants |
| Wrap-up and buffer | 20 | Instructor |

**Action Items:** reference hash-based toggle; k6 script; PR template and `CODEOWNERS` draft.

---

### Session 13 — Learning culture and blameless postmortems
**Session lead:** Instructor


**Goal:** distinguish pathological, bureaucratic and generative cultures, and run a blameless incident analysis.

| Block | Min | Who talks |
|---|---|---|
| Opening: review the work trail from session 12 | 15 | Instructor + participants |
| **Theory with Claude** (slides 217–225): why the Third Way, just culture and learning culture, Westrum's organizational typology, practices that create fast, frequent, cheap learning, blameless postmortems | 40 | Teams |
| Break | 10 | |
| **Tickets:** (a) write the blameless postmortem template for the repo; (b) write a postmortem of the planted defect from session 11 using the template; (c) review a classmate's postmortem for blame language | 80 | Participants |
| Break | 10 | |
| **Team activity:** an anonymous six-statement Westrum survey (aggregate results shown), then a rewrite of a blame-style incident report: from "who made the mistake?" to "what made that decision make sense at the time?" Teams present and critique each other | 45 | Teams |
| **Skill:** "facilitate a blameless postmortem" | 20 | Participants |
| Wrap-up and buffer; assign Game Day roles for session 14 | 20 | Instructor |

**Action Items:** blame-style incident report for the rewrite exercise; Westrum survey form; list of public postmortems (GitLab.com January 2017, Amazon S3 February 2017) as references.

---

### Session 14 — Resilience: fault injection and Game Day
**Session lead:** Instructor


**Goal:** understand why injecting failures on purpose builds resilience, make the code tolerate slow or failing dependencies, and run a Game Day with its postmortem.

| Block | Min | Who talks |
|---|---|---|
| Opening: review the work trail from session 13 | 15 | Instructor + participants |
| **Theory with Claude** (slides 226–235): Netflix's Simian Army, the postmortem meeting, injecting faults in production, Game Day origin, goal and progression | 35 | Teams |
| Break | 10 | |
| **Tickets:** resilience in code. Put Toxiproxy between the API and the inventory service, add latency, watch the API hang, then add a timeout, retries with exponential backoff and a degraded response | 45 | Participants |
| Break | 10 | |
| **Game Day:** each team targets one participant's system. *Prep (20 min):* steady-state hypothesis and blast radius. *Run (50 min):* team A injects failures into team B's system and vice versa (stop a replica, add latency, drop a dependency, misconfigure the canary); the defending team detects with its telemetry and applies its runbooks; the instructor records time to detect and time to recover. *Blameless postmortem (20 min)* per team | 90 | Teams |
| **Skill:** "plan a Game Day" | 15 | Participants |
| Wrap-up and buffer | 20 | Instructor |

**Action Items:** Compose with Toxiproxy; catalogue of faults with their commands; sheet to log detection and recovery times.

---

### Session 15 — Local discoveries, global improvements
**Session lead:** Instructor


**Goal:** turn what one team learns into something the whole organization uses, reserve time to improve and pay down technical debt, and measure performance with DORA metrics.

| Block | Min | Who talks |
|---|---|---|
| Opening: review the work trail from session 14 | 15 | Instructor + participants |
| **Theory with Claude** (slides 236–251): capturing local learning, codified non-functional requirements, reusable Ops user stories, a single shared code repository, standardized processes automated in software, sharing knowledge through tests in shared libraries, aligning technology choices, improvement blitz (kaizen), technical-debt rituals, teaching and learning together | 40 | Teams |
| Break | 10 | |
| **Tickets:** (a) turn the pipeline into a reusable workflow (`workflow_call`) in the shared repo; (b) create a template for new services with Dockerfile, Compose, tests, metrics and the workflow; (c) migrate your service to the shared workflow and get it green; (d) propose an improvement to the shared workflow through a PR that all six adopt | 90 | Participants |
| Break | 10 | |
| **Team activity (slide 252): State of DevOps.** Each team computes its own DORA metrics from the repo history (deployment frequency, lead time for changes, change failure rate, time to restore, using the Game Day data) and compares them with the performance profiles in the report | 35 | Teams |
| **Skill:** "compute DORA metrics from GitHub data" | 20 | Participants |
| Wrap-up and buffer | 20 | Instructor |

**Action Items:** reference reusable workflow; summary of the latest DORA report.

---

### Session 16 — Security, change management, compliance and course close
**Session lead:** Instructor


**Goal:** build security into the pipeline, protect the pipeline itself, use it as evidence for change management and audit, and close the course with a path to the certification.

| Block | Min | Who talks |
|---|---|---|
| Opening: review the work trail from session 15 | 15 | Instructor + participants |
| **Theory with Claude** (slides 253–272): information security is everyone's job, preventive controls and secure libraries, security in the pipeline (static analysis, dependency, image and secret scanning), security telemetry, protecting the CI server, standard/normal/urgent changes, the pipeline as a control, compensating controls for segregation of duties, evidence for auditors | 40 | Teams |
| Break | 10 | |
| **Tickets:** (a) `gitleaks` blocks a planted fake secret; (b) `pip-audit` finds a vulnerable dependency and it is upgraded; (c) Trivy scans the image and the Dockerfile/Compose and fails on CRITICAL; (d) a CycloneDX SBOM as a pipeline artifact; (e) harden the workflow (minimal `permissions`, actions pinned by SHA, Dependabot); (f) a job that records every deployment (commit, PR, approver, test and scan results, proposed change class) | 70 | Participants |
| Break | 10 | |
| **Team activity (slide 273): OWASP and change classification.** Map OWASP Top 10 risks to the Summit Cafe API, then classify six proposed changes (standard, normal or urgent) and decide which automatic evidence replaces a committee approval | 35 | Teams |
| **Exam-readiness practice (non-graded):** each participant takes the official sample exam with Claude as a study partner, then discusses the questions they got wrong | 30 | Participants |
| **Skills showcase and retrospective:** each participant presents their best skill; retrospective (keep, start, stop); path to the DAPC certification | 30 | All |

**Action Items:** repo with the planted fake secret, vulnerable dependency and outdated base image (all secrets are fake test patterns, never real credentials); reference DevSecOps workflow; the official sample exam for the practice.

---

## 5. Consolidated action items before the course resumes

| Before | Item | Owner |
|---|---|---|
| S5 | Invite Patricia (leads S6 and S12) to the repo and Jira; share the plan and the sessions she leads | Instructor |
| S6 | orders endpoint in the Summit Cafe API (`src/summit-cafe-api/`) with a planted bug | Instructor (with Claude) |
| S7 | Images in GHCR with permissions; reference nginx config | Instructor (with Claude) |
| S9 | Observability Compose profile; Codespaces fallback | Instructor (with Claude) |
| S14 | Toxiproxy Compose and fault catalogue | Instructor (with Claude) |
| S16 | Security exercise repo with planted fake secret and CVE | Instructor (with Claude) |

## 6. Open decisions

- [ ] Who creates tickets from session 6 on (instructor, participants, or both). To be decided later.
- [ ] Docker capacity on participants' laptops (otherwise use GitHub Codespaces).
- [ ] How the previous plan's sessions 3–4 content (Compose environment, pytest basics) is verified as covered before session 6.

## 7. Decisions taken

- **Branching:** the course keeps `main` + `develop` with `feature/` and `bugfix/` branches. Session 6 teaches trunk-based development and compares it with this model, but `develop` stays.
- **Claude plans:** every participant needs a Pro plan, so skill creation and all exercises work for everyone.
- **Work trail scoring:** at the end of the course, a skill measures participation in Jira and GitHub. Weights and thresholds are still to be defined.
