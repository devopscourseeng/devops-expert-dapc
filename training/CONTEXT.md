# CONTEXT.md — DAPC Course (DevOps Advanced Professional Certification)

Shared context file. Its purpose is that anyone (or any Claude session) opening this repository can understand the course, its status and the working rules without depending on a chat history.

> Maintenance: update this file through a PR when the course status or a decision changes. If something here contradicts another document in the repo, this file describes the **current state** and the other document should be fixed or this file corrected.

## 1. The course

| Item | Value |
|---|---|
| Course | DevOps Advanced Professional Certification (DAPC) · "DevOps Expert" |
| Certifying body | CertiProf (base material V072021A) |
| Format | Live online (video call, breakout rooms, Excalidraw whiteboard) |
| Workload | 16 sessions of 4 h = 64 h, one session per week, plus 2–3 h per week of independent work |
| Participants | 6, in two teams of 3 for group activities |
| Certification exam | 40 multiple-choice questions, 60 min, pass mark 80 % (32/40) |
| Course grade | 0–100; pass with 70 or more and 80 % attendance (13 of 16 sessions) |

## 2. Current status

- **Sessions 1–4:** already prepared by the previous instructor (scripts, labs and practices). Summary in section 4.
- **From session 5:** a new instructor (the owner of this repo) takes over the course. Everything that is still missing is prepared here.
- **Original global plan (v1.0, Oct 2026)** by the previous instructor: covers all 16 sessions. It is the starting reference, not necessarily the final plan.
- **New global plan (v0.1, sessions 5–16):** draft with titles and short descriptions only. The instructor will keep improving it over the coming days. Until it is published here, plan v1.0 is the reference.
- **Session 5:** will be the new instructor's kickoff: get to know the audience, set up AI tools, Jira and GitHub, and start working through the DAPC material.

## 3. New instructor's goals and approach

- Cover the CertiProf content using **AI as the students' main tool** for learning by doing.
- Reduce instructor talk time (the instructor dislikes master classes) and increase student practice time.
- Work with **GitLab or GitHub** (whichever is easier for MCPs and DevOps tools) plus **Jira**: students get tickets assigned, push changes and have CI/CD integrated.
- Have students **create skills**.
- One complete project as the thread of the course, hosted in this repo (see section 5).

## 4. What was covered in sessions 1–4

Summary of plan v1.0. Slide numbers refer to pages of the CertiProf instructor PDF.

| Session | Topic | Slides | Main practice |
|---|---|---|---|
| S1 | Origin of DevOps, base concepts (CD, IaC, Kata, WIP, lead time, technical debt, bimodal), CALMS, organization | 1–47 | Lab 1 GitHub (repo, branches, PR, conflict, Actions, `main` protection, tag) · Lab 2 Docker (images, layers, Dockerfile, registry). Homework T1 "Cafetería Yungas" |
| S2 | Team Topologies, self-managed teams, Ops in Dev, DevOps Topologies | 48–63 | Cafetería Yungas solved three ways; in-class exercise "Chocolatería Alto Beni"; group activity Ruta Salar / Cooperativa Illimani. T2 optional |
| S3 | The Three Ways and pipeline foundations | 64–98 | Flowban simulation; full environment with Compose in one command (workshop 98). T3 |
| S4 | **Assessment 1** and automated testing | 99–109 | Assessment practice "Heladería Sajama"; pytest + coverage + CI that blocks `main`. T4 |

> Note: plan v1.0 states that only S1 and S2 had been delivered when it was written; the new instructor resumes from S5. Check with the instructor how much of S3–S4 was actually delivered before planning any review.

## 5. Thread project: Summit Cafe API

The project that participants build and operate from session 5: a small Flask REST API in `src/summit-cafe-api/`, packaged with Docker and deployed to Render. (Sessions 1–4 used the earlier project "Café Cumbre en línea": a Flask API plus an nginx site with Docker Compose.) Each session adds a capability (per plan v1.0):

| Sessions | Capability added | Way |
|---|---|---|
| S1–S2 | Repo with CI and publishing; versioned site image (1.0 → 1.1) | Flow |
| S3 | Orders API and Compose: full environment in one command | Flow |
| S4 | Unit and API tests; test job that blocks integration | Flow |
| S5 | Feature built with TDD; pipeline for analysis, tests, build and publishing to GHCR | Flow |
| S6 | Self-service deployment, blue-green, canary and feature toggles | Flow |
| S7 | Inventory service extracted with the strangler pattern; value stream map | Flow |
| S8 | Metrics in Prometheus and Grafana dashboards | Feedback |
| S9 | Structured logs with correlation id, information radiator and alerts | Feedback |
| S10 | Watched canary with automatic rollback; LRR checklist | Feedback |
| S11 | A/B experiment; PR template, CODEOWNERS and cross review | Feedback |
| S12 | Blameless postmortem template | Learning |
| S13 | Timeouts, retries and runbooks tested in a Game Day (Toxiproxy) | Learning |
| S14 | Reusable workflow and shared repository template | Learning |
| S15 | Security controls (gitleaks, pip-audit, Trivy), SBOM and automatic change record | Security and change |

With the new approach (AI + Jira + tickets) this distribution may change. The new plan v0.1 redefines it for S5–S16.

## 6. Official syllabus (6 units)

1. Introduction (slides 18–63)
2. Principles: the Three Ways (64–76)
3. The First Way: flow (77–159)
4. The Second Way: feedback (160–216)
5. The Third Way: learning (217–252)
6. Security, change and compliance (253–273)

Assessments: A1 in S4, A2 in S8, A3 in S12, final assessment with exam simulation in S16. Weights: A1–A3 15 % each, final 25 %, homework 20 %, participation 10 %.

## 7. Tools and stack

Git and GitHub (Actions, GHCR), Docker and Compose, Flask, pytest, ruff, nginx, Prometheus, Grafana, k6, Toxiproxy, gitleaks, pip-audit, Trivy (CycloneDX SBOM), Dependabot. New: Jira and AI assistants for students. Whiteboard: Excalidraw.

## 8. Repository conventions

- Language of all materials: **English**. Original names of exercises from the CertiProf material are kept as they are.
- Structure: `training/` holds the course material (`CONTEXT.md`, `plan/`, `docs/` guides, `session_N/` per session with slides and handouts). `src/` holds the source code (`src/summit-cafe-api/`). `.github/` holds the CI workflow.
- Changes enter **through pull requests**, one topic per PR, with a short description of what changes and why.
- Secrets that appear in practices are always **fake** (test patterns); never real credentials.
- The original CertiProf PDFs (instructor and student material, brochure, sample exam) are **not uploaded** to this repo because they are copyrighted material. They are cited by slide number.

## 9. Open decisions

- [ ] Choose GitHub or GitLab as the students' platform and how to integrate Jira.
- [ ] Publish the new global plan (v0.1) in `training/plan/` when it is ready.
- [x] The thread project (Summit Cafe API) lives in this repo, in `src/summit-cafe-api/`.
- [ ] Define how students' use of AI will be assessed (plan v1.0 forbids it in practical assessments and allows it, if declared, in homework; this is a proposal to review).
