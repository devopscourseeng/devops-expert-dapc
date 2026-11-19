# Risky releases and self-service deploys

Team A · Session 7 · "Theory with Claude"

## Step 1. What Claude would say

**The idea.** A release is risky when it is manual, rare and different on every server. The Knight Capital case shows it: in 2012 a team copied new code to eight servers by hand, one server was missed, and the old code on that server acted wrongly on the new orders. The company lost about 440 million dollars in about 45 minutes, and nobody could go back quickly. The fix has two parts: every server gets the same automatic deploy, and there is a fast way back.

**How to get there.** Make a deploy a button, not a ritual. Build the package once, test it, and promote the same package through the environments. The pipeline should deploy in the same way in every environment, run a smoke test after each deploy, and keep the environments consistent. Record which commands ran, on which machine, when, who approved and what the output was. Give developers a self-service way to deploy, so they do not need to open a ticket and wait.

**Continuous delivery and continuous deployment.** In continuous delivery every change is ready to be deployed, and a person presses the button. In continuous deployment no person presses it: every good change goes to production by itself. Continuous integration comes first, then continuous delivery, then continuous deployment.

**Deployment is not release.** Deployment is putting a version in an environment. Release is offering a feature to all customers or to a part of them. Many people use the two words as if they were the same, but they are two actions with two purposes.

**Example from the Summit Cafe API.**

- The CI job "Unit tests" runs on every pull request.
- The workflow "Publish image" builds the image once, runs a smoke test (the container starts and `/health` answers) and publishes it to GHCR with the tag `1.2`.
- `./deploy/deploy-to-environment.sh staging 1.2` and `./deploy/deploy-to-environment.sh prod 1.2` run the same image in two environments.
- Deploying to prod puts 1.2 in the canary container with 0% of the calls. Release happens later, with `./deploy/set-weight.sh`.

**One sentence to remember.** Make deploys boring: one button, the same everywhere, and a fast way back.

## Step 2. Check against the official pages (129–134, 138–141)

**Where to look.**

- Pages 129–130: what matters is the results, not the form. Deploys should be low-risk, push-button events that we can run on demand. Continuous delivery is the base for continuous deployment, as continuous integration is the base for continuous delivery.
- Page 131: pipeline requirements: deploy in the same way in all environments, smoke test the deploys, keep environments consistent.
- Page 132: a CI/CD pipeline for services, with promotion between environments.
- Pages 133–134: automated self-service deploys: build, test and deploy, without manual steps or hand-offs. Developers can deploy and fix problems without opening a ticket for Operations.
- Page 138: what the deploy pipeline should do: check that packages are fit for production, show that production environments are ready, offer a one-button self-service method, record commands, machines, time, who approved and the output, run a smoke test, and give fast feedback.
- Page 139: the picture that compares continuous integration, continuous delivery and continuous deployment (which steps are manual and which are automatic).
- Pages 140–141: deployment (installing a version in an environment) is different from release (offering a feature to customers).

**Compare with Step 1.**

- Does the answer say that the same package goes to every environment? It should.
- Does it list what the pipeline records (who, what, where, when, output)? This is often forgotten.
- Does it separate continuous delivery (a person presses the button) from continuous deployment (no person)? This is easy to mix up.
- Does it explain that deployment and release are different actions?

**Watch out for.** The case of Knight Capital is not in the official pages for these numbers. It is the example we use to make the idea clear.

## Your turn (steps 3, 4 and 5)

Prepare one example from the Summit Cafe API, teach the others for about 5 minutes, and then talk together: where in our own work is a deploy still manual or different from one computer to another?
