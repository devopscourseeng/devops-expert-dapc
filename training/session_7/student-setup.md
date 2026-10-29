# Session 7: set up your computer

Do this **before the class**. It takes about 15 minutes. Everything runs on your own computer; no real server and no password are needed.

## 1. Install Docker Desktop

1. Install Docker Desktop for your system.
2. Open it and wait until it says **Engine running**.
3. Check in a terminal:

```
docker ps
```

You should see a table with a header line, even if it is empty. If you see "cannot connect to the Docker API", Docker Desktop is not running yet.

## 2. Use a bash terminal

The scripts are bash scripts.

- **Windows:** use **Git Bash**. It comes with Git for Windows. Do **not** use CMD or PowerShell: CMD says `'.' is not recognized`.
- **Mac and Linux:** use the normal Terminal.

## 3. Get the code

```
git clone https://github.com/devopscourseeng/devops-expert-dapc.git
cd devops-expert-dapc
git checkout develop
```

## 4. Check that it works

```
./deploy/start-environment.sh 1.1
curl http://localhost:8200/menu
```

You should see the menu in JSON. The image is public: you do not need a login for GHCR.

Clean up when you are done:

```
docker rm -f cafe-prod cafe-prod-stable cafe-prod-canary cafe-staging
```

## Your environments

| Environment | Container | Port |
|---|---|---|
| staging | `cafe-staging` | 8100 |
| prod, stable | `cafe-prod-stable` | 8201 |
| prod, canary | `cafe-prod-canary` | 8202 |
| prod, proxy (nginx) | `cafe-prod` | 8200 |

In prod, always call port **8200**. The proxy splits the calls between stable and canary.

## Commands

```
./deploy/start-environment.sh 1.1               # prod: stable = 1.1, 100% of the calls
./deploy/deploy-to-environment.sh staging 1.2   # deploy 1.2 to staging
./deploy/deploy-to-environment.sh prod 1.2      # put 1.2 in the canary, 0% of the calls
./deploy/set-weight.sh 10                       # 10% of the calls go to the canary
./deploy/set-weight.sh 0                        # rollback: all calls go to stable
curl http://localhost:8200/version              # which version answered?
```

Add `DRY_RUN=1` before a command to see what it would do without doing it.

Version 1.1 has no `/version` route. A call that reaches 1.1 answers "Not Found": read it as "this is the old version".

## If something goes wrong

| What you see | What it means | What to do |
|---|---|---|
| `failed to connect to the docker API` | Docker Desktop is not running | Open Docker Desktop and wait for "Engine running" |
| `'.' is not recognized` | You are in CMD | Open Git Bash |
| `port is already allocated` | Another program or container uses the port | `docker ps`, then `docker rm -f` the old container |
| `denied` or `unauthorized` when pulling | The package is not public yet | Tell the trainer |
| The first pull is slow | The image is downloading | Wait; the next pulls are fast |

Any token in the exercises is fake. Never use a real password or key in this course.

## Claude

For the tickets you use Claude on your computer (or in the chat) to write and explain code. You need a Claude Pro plan. Read what Claude writes before you run it. If you cannot use Claude, tell the trainer: you can pair with a classmate and still write the code and the pull request.
