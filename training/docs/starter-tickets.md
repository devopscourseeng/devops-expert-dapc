# Starter tickets for Session 5

Ten small tickets for the first real ticket exercise (6 participants plus 4 spares). Each one changes a different part of the Summit Cafe API in `src/summit-cafe-api/`. The goal is to practice the process (ticket, branch, pull request, tests, review, closing comment), not to write hard code.

The bug fixes are planted on purpose: the code in the repository really has these problems.

## How to create them in Jira

1. Go to **Jira settings → System → External system import → CSV**.
2. Upload [starter-tickets.csv](starter-tickets.csv) and map the columns: Summary → Summary, Issue Type → Issue Type, Description → Description, Labels → Labels.
3. Import into the **SCRUM** project.
4. Assign one ticket to each participant. Keep the other four unassigned as spares.
5. Note the real ticket numbers (SCRUM-N). Replace `SCRUM-12` in the slides with one of them.

If the import does not work, create the tickets by hand: copy the summary and the description from the tables below.

## The tickets

| # | Summary | Type | Branch | File | Done when |
|---|---|---|---|---|---|
| 1 | Fix the typo "Capuchino" in the menu | Bug | `bugfix/SCRUM-N` | `menu.py` | GET /menu/2 returns the name "Cappuccino". |
| 2 | Return 404 for an unknown menu item | Bug | `bugfix/SCRUM-N` | `app.py` | GET /menu/99 returns 404 with a JSON error message. |
| 3 | Set the correct price for the Espresso | Bug | `bugfix/SCRUM-N` | `menu.py` | GET /menu/1 returns the price 2.5. |
| 4 | Make /health return "ok" | Bug | `bugfix/SCRUM-N` | `app.py` | GET /health returns {"status": "ok"}. |
| 5 | Add an "available" field to menu items | Story | `feature/SCRUM-N` | `menu.py` | Every item returned by GET /menu has "available": true. |
| 6 | Filter the menu by category | Story | `feature/SCRUM-N` | `app.py` | GET /menu?category=food returns only food items, and GET /menu still returns everything. |
| 7 | Add an opening hours endpoint | Story | `feature/SCRUM-N` | `app.py` | GET /hours returns 200 and the opening and closing times. |
| 8 | Add a root endpoint with the API name and version | Story | `feature/SCRUM-N` | `app.py` | GET / returns 200 with the name and the version. |
| 9 | Write the "Run it" section of the README | Task | `feature/SCRUM-N` | `README.md` | A new person can follow the README and start the API. |
| 10 | Add a test that every menu item has the required fields | Task | `feature/SCRUM-N` | `tests/test_menu.py` | The new test passes in CI. |

## Descriptions

### 1. Fix the typo "Capuchino" in the menu

The menu item 2 is called "Capuchino". The correct name is "Cappuccino".

- **Type:** Bug
- **Branch:** `bugfix/SCRUM-N`
- **File:** `src/summit-cafe-api/menu.py`
- **Done when:** GET /menu/2 returns the name "Cappuccino".

### 2. Return 404 for an unknown menu item

GET /menu/99 returns an error 500 because the id does not exist. It should return status 404 and a JSON message such as {"error": "Item not found"}.

- **Type:** Bug
- **Branch:** `bugfix/SCRUM-N`
- **File:** `src/summit-cafe-api/app.py`
- **Done when:** GET /menu/99 returns 404 with a JSON error message.

### 3. Set the correct price for the Espresso

The Espresso (item 1) has the price 0. Set it to 2.5.

- **Type:** Bug
- **Branch:** `bugfix/SCRUM-N`
- **File:** `src/summit-cafe-api/menu.py`
- **Done when:** GET /menu/1 returns the price 2.5.

### 4. Make /health return "ok"

GET /health returns {"status": "okay"}. The agreed value is "ok".

- **Type:** Bug
- **Branch:** `bugfix/SCRUM-N`
- **File:** `src/summit-cafe-api/app.py`
- **Done when:** GET /health returns {"status": "ok"}.

### 5. Add an "available" field to menu items

Add the field "available" (true or false) to every menu item. Set it to true for all items.

- **Type:** Story
- **Branch:** `feature/SCRUM-N`
- **File:** `src/summit-cafe-api/menu.py`
- **Done when:** Every item returned by GET /menu has "available": true.

### 6. Filter the menu by category

Add the query option category to GET /menu. Example: GET /menu?category=drinks returns only the drinks. Without the option, it returns all items.

- **Type:** Story
- **Branch:** `feature/SCRUM-N`
- **File:** `src/summit-cafe-api/app.py`
- **Done when:** GET /menu?category=food returns only food items, and GET /menu still returns everything.

### 7. Add an opening hours endpoint

Add GET /hours. It returns the opening hours as JSON, for example {"open": "08:00", "close": "18:00"}.

- **Type:** Story
- **Branch:** `feature/SCRUM-N`
- **File:** `src/summit-cafe-api/app.py`
- **Done when:** GET /hours returns 200 and the opening and closing times.

### 8. Add a root endpoint with the API name and version

Add GET /. It returns the name of the API and its version, for example {"name": "Summit Cafe API", "version": "0.1.0"}.

- **Type:** Story
- **Branch:** `feature/SCRUM-N`
- **File:** `src/summit-cafe-api/app.py`
- **Done when:** GET / returns 200 with the name and the version.

### 9. Write the "Run it" section of the README

The README says "To be written" under Run it. Explain how to run the API on your computer (with Python, and with Docker) and how to run the tests.

- **Type:** Task
- **Branch:** `feature/SCRUM-N`
- **File:** `src/summit-cafe-api/README.md`
- **Done when:** A new person can follow the README and start the API.

### 10. Add a test that every menu item has the required fields

Add a test in src/summit-cafe-api/tests that checks every item returned by GET /menu has the fields id, name, category and price.

- **Type:** Task
- **Branch:** `feature/SCRUM-N`
- **File:** `src/summit-cafe-api/tests/test_menu.py`
- **Done when:** The new test passes in CI.

## Notes for the instructor

- Tickets 1, 3 and 5 all change `menu.py`, and tickets 2, 4, 6, 7 and 8 all change `app.py`. Merge conflicts are possible and are a good thing to solve together. Resolve them in class, not by avoiding them.
- Ticket 10 is a good one for anyone who finishes early. Tickets 9 and 10 do not touch the API code.
- Hand out the tickets so that neighbours do not have the same file when possible.
