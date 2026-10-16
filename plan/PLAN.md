# Global Plan — DAPC Course, Sessions 5–16 (v0.2, draft for review)

Status: **draft**. Session 5 is approved. Sessions 6–16 follow the same structure and are pending review.

This plan replaces the plan for sessions 5–16 in the original global plan (v1.0). Sessions 1–4 are completed (see [CONTEXT.md](../CONTEXT.md)).

## 1. How the course works from session 5

- **Format:** 12 sessions (5–16) of 4 hours, live online, 6 participants in two teams of 3.
- **Session leads:** Patricia leads sessions 6 and 12 (quality focus: tests and peer review). Alex leads all the others.
- **Tools:** one shared GitHub repo (`devopscourseeng/devops-expert-dapc`), one Jira project (key **SCRUM**), and **Claude** as the only AI tool (Pro preferred, free allowed).
- **Learning by doing:** the instructor talks about 20–30 minutes per session. Participants build the theory themselves with Claude, check it against the official CertiProf material, and apply it on real tickets.
- **Everything goes through tickets and pull requests:** a `SCRUM-N` ticket, a short branch from `develop` named `feature/SCRUM-N` or `bugfix/SCRUM-N`, a PR to `develop` with CI green, a review by a classmate, and a closing comment in Jira.
- **Skills:** session 5 introduces the idea with a group discussion. From session 6 on, in every session participants turn something they learned into a Claude skill and contribute it to the repo.
- **Thread project:** *Café Cumbre en línea* (Flask API + nginx, Docker Compose) lives in `cafe-cumbre-en-linea/`. Each session adds a capability to it.
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

The exact scoring (weights and thresholds) is **to be defined** and added to this plan in a separate PR. The signals above are fixed so participants know from session 5 what counts.

Optional, outside the grade: the official CertiProf DAPC exam (40 multiple-choice questions, 60 minutes, 80 % to pass). Session 16 includes a non-graded practice with the sample exam.

## 3. Session overview

| Session | Lead | Theme | DAPC slides | Syllabus unit | Project capability added |
|---|---|---|---|---|---|
| S5 | Alex | Kickoff: Claude, GitHub and Jira as the way of working | 64–76 (recap) | 2 | First ticket closed through a PR |
| S6 | Patricia | Tests, TDD, continuous integration and trunk-based development | 99–128 | 3 | Real CI pipeline with tests that block merges |
| S7 | Alex | Low-risk releases | 129–154 | 3 | Self-service deploy, blue-green, canary, feature toggles |
| S8 | Alex | Low-risk architecture and the end of the First Way | 155–159 | 3 | Inventory service extracted (strangler pattern); value stream map |
| S9 | Alex | Telemetry | 160–173 | 4 | Metrics in Prometheus and Grafana dashboards |
| S10 | Alex | Logs, information radiators and predictive analysis | 174–182 | 4 | Structured logs, correlation id, radiator and alerts |
| S11 | Alex | Feedback to deploy safely: LRR and HRR | 183–194 | 4 | Watched canary with automatic rollback; LRR checklist |
| S12 | Patricia | Hypotheses, A/B tests and peer review | 195–216 | 4 | A/B experiment; PR template, CODEOWNERS |
| S13 | Alex | Learning culture and blameless postmortems | 217–225 | 5 | Postmortem template and first postmortem |
| S14 | Alex | Resilience: fault injection and Game Day | 226–235 | 5 | Timeouts, retries, runbooks tested in a Game Day |
| S15 | Alex | Local discoveries, global improvements | 236–252 | 5 | Reusable workflow, repo template, DORA metrics |
| S16 | Alex | Security, change management, compliance and course close | 253–273 | 6 | DevSecOps pipeline, SBOM, automatic change record |

Slide numbers refer to the CertiProf instructor PDF (V072021A). The old plan's three assessment sessions (4, 8, 12) and the final exam session are removed; their time goes to practice.

## 4. Session plans

Every session has the same shape (the minutes add up to 240):

- **Opening:** review the work trail of the previous session.
- **Theory built by the participants** with Claude, in teams.
- **Hands-on tickets** on Café Cumbre.
- **Team activity.**
- **Skill creation** (from session 6).
- **Wrap-up and buffer.**

---

### Session 5 — Kickoff: Claude, GitHub and Jira as the way of working
**Session lead:** Alex


**Goal:** by the end, each participant has Claude connected to GitHub and Jira, has closed one ticket through a PR, and understands how their work is checked.

| Block | Min | Who talks |
|---|---|---|
| **Get to know each other:** four questions for each participant (job today, tools used, AI use, expectations) | 30 | Participants |
| **Course rules:** the course in four numbers, the path every change follows, how the work trail shows progress, the branching strategy (`main` and `develop`) and best practices | 20 | Instructor |
| **Setup with Claude:** accept the repo and Jira invites, open Claude, connect GitHub and Jira, check that Claude can see the repo and the tickets (guide: `docs/setup-tools.md`) | 60 | Participants |
| Break | 10 | |
| **First real ticket:** take it in Jira, branch from `develop`, solve it with Claude, open the PR, tests pass, classmate review, closing comment in Jira | 60 | Participants |
| **The Three Ways with Claude** (slides 64–76, recap): each pair asks Claude to explain one Way, checks it against the official material and teaches it in 3 minutes, then the group talks about what Claude got right or missed | 30 | Pairs |
| **What is a skill?** Group discussion: what a skill is, which repeated tasks we could automate with one, and confirmation that we build the first skill in session 6 | 20 | Everyone |
| Closing: outcomes, expectations check, next session | 10 | Instructor |

**Action Items**
1. Starter tickets in SCRUM: 8–10 small, easy tickets (for example "fix the site title"), one per participant plus spares, each assigned to a participant. Replace `SCRUM-12` on the branching and best-practices slides with a real ticket number.
2. Collaborator invites to the repo and to Jira for the 6 participants, sent several days earlier (guide: `docs/send-invites.md`).
3. Check live where the GitHub and Jira connections are in Claude's settings (the menu names change), and replace the "plan blocks a step" row on the troubleshooting slide with what really happens on a free account.

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

**Action Items:** Café Cumbre orders API in `cafe-cumbre-en-linea/` with a deliberate bug and empty test folder; tickets for the three exercises.

---

### Session 7 — Low-risk releases
**Session lead:** Alex


**Goal:** separate deployment from release and learn the patterns that make releases boring: blue-green, canary and feature toggles.

| Block | Min | Who talks |
|---|---|---|
| Opening: review the work trail from session 6 | 15 | Instructor + participants |
| **Theory with Claude** (slides 129–153): high-risk releases (Knight Capital case), self-service deploys, environment-based patterns (blue-green, canary, cluster immune system) and application-based patterns (feature toggles, dark launches) | 45 | Teams |
| Break | 10 | |
| **Tickets:** (a) `deploy.sh VERSION` that pulls the image from GHCR and starts it; (b) blue-green with two API instances behind nginx; (c) canary with weighted upstreams 90/10, 50/50, 100; (d) a feature toggle that ships a feature turned off and enables it via an environment variable | 85 | Participants |
| Break | 10 | |
| **Team activity:** roll out version 1.2 as a canary and perform a deliberate rollback. Each team documents the steps and times in a runbook PR | 35 | Teams |
| **Skill:** "write a deployment runbook" | 20 | Participants |
| Wrap-up and buffer | 20 | Instructor |

**Action Items:** images published to GHCR with write permission for the participants; reference nginx configuration; version 1.2 of the API with a toggle.

---

### Session 8 — Low-risk architecture and the end of the First Way
**Session lead:** Alex


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
**Session lead:** Alex


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
**Session lead:** Alex


**Goal:** design useful logs, build a radiator and actionable alerts, and apply simple statistics to detect anomalies.

| Block | Min | Who talks |
|---|---|---|
| Opening: review the work trail from session 9 | 15 | Instructor + participants |
| **Theory with Claude** (slides 174–182): log levels and which events to record, logs for incident analysis, information radiators, telemetry gaps by level, mean and standard deviation, the three-sigma rule and its limits | 35 | Teams |
| Break | 10 | |
| **Tickets:** (a) structured JSON logs with a correlation id generated by nginx and propagated by the API; (b) follow one request end to end with `docker compose logs` and `jq`; (c) Grafana kiosk radiator; (d) alert on error rate above 5 % for 2 minutes; (e) three-sigma band with `avg_over_time` and `stddev_over_time` | 95 | Participants |
| Break | 10 | |
| **Team activity: hunt the gaps.** Each team fills a telemetry matrix for Café Cumbre by level (business, application, infrastructure, client, pipeline, security); the other team points out what is missing | 35 | Teams |
| **Skill:** "write an alert with a mini runbook" | 20 | Participants |
| Wrap-up and buffer | 20 | Instructor |

**Action Items:** nginx config with correlation id; reference alert rules; telemetry matrix template.

---

### Session 11 — Feedback to deploy safely: LRR and HRR
**Session lead:** Alex


**Goal:** use telemetry to decide whether a deployment continues or rolls back, and review a service for readiness to launch and to hand off.

| Block | Min | Who talks |
|---|---|---|
| Opening: review the work trail from session 10 | 15 | Instructor + participants |
| **Theory with Claude** (slides 183–194): feedback for safe deployments, watching metrics after a deploy, shared on-call, developers operating their own service, handing a service back, launch guidance, Launch Readiness Review (LRR) and Hand-Off Readiness Review (HRR) | 45 | Teams |
| Break | 10 | |
| **Tickets:** (a) release version 1.3, which contains a defect that causes errors in a fraction of requests, as a 10 % canary with the version as a metrics label; (b) compare the error rate per version in Grafana; (c) write `watch_canary.sh`, which queries the Prometheus API and rolls back automatically over a threshold; (d) release the fixed 1.3.1 | 85 | Participants |
| Break | 10 | |
| **Team activity: does it pass the LRR?** Each team writes the LRR/HRR checklist for Café Cumbre (defects, alerts, runbooks, capacity, dependencies, security) and reviews the other team's service: would they accept it on their on-call? | 35 | Teams |
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
**Session lead:** Alex


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
**Session lead:** Alex


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
**Session lead:** Alex


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
**Session lead:** Alex


**Goal:** build security into the pipeline, protect the pipeline itself, use it as evidence for change management and audit, and close the course with a path to the certification.

| Block | Min | Who talks |
|---|---|---|
| Opening: review the work trail from session 15 | 15 | Instructor + participants |
| **Theory with Claude** (slides 253–272): information security is everyone's job, preventive controls and secure libraries, security in the pipeline (static analysis, dependency, image and secret scanning), security telemetry, protecting the CI server, standard/normal/urgent changes, the pipeline as a control, compensating controls for segregation of duties, evidence for auditors | 40 | Teams |
| Break | 10 | |
| **Tickets:** (a) `gitleaks` blocks a planted fake secret; (b) `pip-audit` finds a vulnerable dependency and it is upgraded; (c) Trivy scans the image and the Dockerfile/Compose and fails on CRITICAL; (d) a CycloneDX SBOM as a pipeline artifact; (e) harden the workflow (minimal `permissions`, actions pinned by SHA, Dependabot); (f) a job that records every deployment (commit, PR, approver, test and scan results, proposed change class) | 70 | Participants |
| Break | 10 | |
| **Team activity (slide 273): OWASP and change classification.** Map OWASP Top 10 risks to Café Cumbre, then classify six proposed changes (standard, normal or urgent) and decide which automatic evidence replaces a committee approval | 35 | Teams |
| **Exam-readiness practice (non-graded):** each participant takes the official sample exam with Claude as a study partner, then discusses the questions they got wrong | 30 | Participants |
| **Skills showcase and retrospective:** each participant presents their best skill; retrospective (keep, start, stop); path to the DAPC certification | 30 | All |

**Action Items:** repo with the planted fake secret, vulnerable dependency and outdated base image (all secrets are fake test patterns, never real credentials); reference DevSecOps workflow; the official sample exam for the practice.

---

## 5. Consolidated action items before the course resumes

| Before | Item | Owner |
|---|---|---|
| S5 | Starter tickets in SCRUM (8–10) | Instructor (with Claude) |
| S5 | Collaborator invites (repo and Jira) for the 6 participants | Instructor |
| S5 | Invite Patricia (leads S6 and S12) to the repo and Jira; share the plan and the sessions she leads | Alex |
| S6 | Café Cumbre orders API in `cafe-cumbre-en-linea/` with a planted bug | Instructor (with Claude) |
| S7 | Images in GHCR with permissions; reference nginx config | Instructor (with Claude) |
| S9 | Observability Compose profile; Codespaces fallback | Instructor (with Claude) |
| S14 | Toxiproxy Compose and fault catalogue | Instructor (with Claude) |
| S16 | Security exercise repo with planted fake secret and CVE | Instructor (with Claude) |

## 6. Open decisions

- [ ] Exact scoring for the work trail (weights, thresholds, pass mark).
- [ ] Who creates tickets from session 6 on (instructor, participants, or both).
- [ ] Branching model: session 5 teaches `main` + `develop` with `feature/` and `bugfix/` branches. Session 6 teaches trunk-based development (slides 121–123). Decide how session 6 compares the two, and whether the course keeps `develop` afterwards.
- [ ] Whether free Claude accounts can complete every exercise, or Pro is required from a given session.
- [ ] Skill creation on free accounts: skills require code execution to be enabled, and the "record a skill" shortcut is not available on free plans. Decide whether participants without Pro write the skill file by hand, pair up, or upgrade.
- [ ] Docker capacity on participants' laptops (otherwise use GitHub Codespaces).
- [ ] How the previous plan's sessions 3–4 content (Compose environment, pytest basics) is verified as covered before session 6.
