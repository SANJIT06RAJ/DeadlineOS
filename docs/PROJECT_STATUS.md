# PROJECT_STATUS — DeadlineOS

_Last updated: Sunday, 8 November 2026_

**Latest application commit:** 06492bc — chore: add Python linting and formatting checks.

**Latest verified progress:** Week 7 Day 48 — Clean-install and failed-startup recovery testing — IMPLEMENTATION AND TESTING COMPLETED; APPLICATION COMMIT PENDING.

**Day 48 verified progress:**
- Built and recreated the frontend Docker image successfully after the Nginx configuration change.
- Verified the production frontend returned HTTP 200.
- Stopped the Compose backend and confirmed the frontend remained running and serving the application.
- Confirmed API requests returned HTTP 502 while the backend was unavailable, without an Nginx startup crash.
- Fixed Nginx backend DNS/startup handling using Docker's embedded DNS resolver and dynamic hostname resolution.
- Corrected API path forwarding with an explicit rewrite before proxying to FastAPI.
- Restarted the backend without restarting the frontend; API health recovered successfully.
- Verified the assignment summary returned the expected **27 assignments**: 24 pending, 2 in progress, 1 completed, 6 overdue, 0 due today, 19 upcoming, and 1 without a due date.
- Confirmed the persistent Compose volume remained mounted at `/data`.
- Created and integrity-checked a local SQLite snapshot, backed up the original empty Docker database, and restored the 27-record snapshot into the Compose volume. Temporary backups were retained.
- `git diff --check` passed and the Nginx diff was reviewed.
- The application change in `frontend/nginx.conf` remains local and uncommitted.

**Day 47 verified progress:**
- Added root-level `pyproject.toml` with Ruff configuration for Python 3.13 and an 88-character line length.
- Excluded the pre-existing local-only `backend/oop_practice.py` from Ruff and scoped the FastAPI `B008` exception to `backend/app/main.py`.
- Ruff lint passed; all 20 backend Python files passed the formatting check.
- Backend pytest suite: **132 passed**.
- `pip check` passed; `pip-audit` reported no known vulnerabilities.
- Frontend ESLint passed; Vitest reported **13 passed across 2 test files**; production build passed.
- Frontend production dependency audit reported **0 vulnerabilities**.
- Committed as `06492bc` and pushed successfully to `origin/master`.

**Day 46 verified progress:**
- Created `.github/workflows/ci.yml` for automated backend and frontend checks.
- Configured Python 3.13 and Node.js 24 environments.
- Backend CI installs `backend/requirements.txt` and runs pytest.
- Frontend CI uses `npm ci`, runs Vitest, ESLint, and the Vite production build.
- Added `argon2-cffi==25.1.0` to backend requirements after CI exposed the missing dependency.
- GitHub Actions Run #3 succeeded: backend **132 passed**, frontend **13 passed across 2 test files**.
- Both GitHub Actions jobs reported success.

**Week 6 status:** Days 36–42 completed. Day 42 final regression verification passed. Week 6 is complete.

**Week 7 status:** Days 43–48 technically completed and verified. Day 48 status documentation is pushed; the Day 48 application change remains local and uncommitted.

**Current roadmap progress:** Week 7 — Day 48 implementation and recovery testing completed and verified; application commit pending.

**Next task:** Day 49 — Release tagging, Git history review, and final bug fixes.

**Git state:** The Day 48 status documentation updates have been committed to `origin/master`. The local working copy must be fast-forwarded to include the documentation commits and then retain the local `frontend/nginx.conf` change. That application change has not yet been committed. `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.

**Scope reminder:** DeadlineOS remains a single-student MVP. Authentication and multiple-user accounts remain outside the initial application scope.

Day 28 verification:
- Backend baseline: **71 passed**.
- Added parametrized API tests for yesterday, today, and tomorrow deadlines.
- Assignment API tests: **56 passed**.
- Full backend pytest suite: **74 passed**.
- Verified deadline calculations and overdue classification for all three boundary cases.
- Browser-tested Calendar date display and navigation.
- Browser-tested overdue styling and Notification Center classifications.
- Confirmed completed assignments are excluded from overdue notifications.
- User confirmed all Calendar and Notification Center checks behaved correctly.
- `git diff --check`: PASSED.
- Reviewed the test diff: 31 insertions, no deletions, in `backend/tests/test_assignment_api.py`.
- Committed as `8f70737` — `test: cover assignment deadline boundaries` — and pushed to `origin/master`.
- Final Git verification confirmed local `master` and `origin/master` synchronized at `8f70737`.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.

**Current roadmap progress:** Week 5 Day 32 — human confirmation before saving AI-extracted assignment details — implemented, verified, committed, and pushed (`d2f5b56`).

**Next roadmap task:** Day 33 — Test missing dates, ambiguous instructions, and incorrect AI suggestions.

## 1. Environment

- OS: Windows

- Project directory: `C:\Users\kefztv\Desktop\DeadlineOS`

- Git: `2.55.0.windows.2`

- Python: `3.13.0`

- Node.js: `v24.18.0`

- npm: `11.16.0`

- VS Code: `1.141.2`

- Python virtual environment: `backend\.venv`

- Backend: FastAPI + Uvicorn

- Database: SQLite

- Automated testing: pytest

- Linux environment: Ubuntu on WSL 2

- Remote repository: https://github.com/SANJIT06RAJ/DeadlineOS

- Active branch: `master`

## 2. Project Goal

DeadlineOS is an academic task and deadline management application for tracking assignments, due dates, subtasks, and progress.

The main goal is to help students organise academic work and avoid last-minute submissions.

Planned future features include:

- React dashboard and forms.

- Assignment and subtask management.

- Deadline sorting and overdue summaries.

- Reminders and workload tracking.

- Improved validation, security, and automated testing.

- Docker and CI/CD.

- Optional AI-assisted assignment detail extraction from documents.

AI-extracted information must be reviewed and explicitly confirmed by the user before being saved. The application must remain usable when the optional AI feature is unavailable.

### MVP decisions

- The initial version is designed for a single student.

- Authentication and multiple-user accounts are outside the initial MVP.

- Courses are deferred until a later version.

- Assignments support `pending`, `in_progress`, and `completed` statuses.

- An assignment can contain multiple subtasks.

- Deleting an assignment must also delete its subtasks.

- The backend uses FastAPI, SQLite, Pydantic schemas, and automated tests.

- The frontend uses React and Vite.

## 3. Completed Work History

### Day 1 — Thursday, 15 October 2026: Foundation Setup

- [x] Checked the development tools.

- [x] Created the Git repository in the correct project directory.

- [x] Removed an accidentally created `.git` folder from the Desktop root.

- [x] Created `README.md`.

- [x] Created `.gitignore`.

- [x] Created `docs/PROJECT_PLAN.md`.

- [x] Created `backend/app`, `backend/tests`, and `frontend`.

- [x] Created the Python virtual environment at `backend\.venv`.

- [x] Installed FastAPI and `uvicorn[standard]`.

- [x] Created `backend/app/__init__.py`.

- [x] Created `backend/app/main.py`.

- [x] Added `GET /` and `GET /health` endpoints.

- [x] Started the backend at `http://127.0.0.1:8000`.

- [x] Verified that `/health` returns `{"status":"healthy"}`.

- [x] Created initial commit `0b0d2f8`.

- [x] Created backend commit `a704806` — `feat: add initial FastAPI backend`.

- [x] Reviewed basic pip, FastAPI, REST API, and foreign-key concepts.

### Day 2 — Friday, 16 October 2026: SQLite and Automated Tests

- [x] Created `backend/requirements.txt` containing FastAPI, Uvicorn, and pytest.

- [x] Verified installed dependencies.

- [x] Created `backend/app/database.py`.

- [x] Configured a SQLite database at `backend/deadlineos.db`.

- [x] Enabled SQLite foreign-key enforcement in the database setup.

- [x] Created the `assignments` table.

- [x] Created the `subtasks` table.

- [x] Added a foreign-key relationship from subtasks to assignments.

- [x] Added cascading deletion of subtasks when an assignment is deleted.

- [x] Created `backend/tests/test_database.py`.

- [x] Verified all four database tests passed.

- [x] Removed the temporary `backend/check_db.py` verification script.

- [x] Committed the database work as `f45ebd1` — `feat: add SQLite database and tests`.

- [x] Successfully pushed the database commit to `origin/master`.

#### Verified Day 2 database tests

1. Table creation.

2. Valid assignment–subtask relationships.

3. Rejection of invalid assignment IDs.

4. Cascading deletion of subtasks.

Day 2 test result: \***\*4 passed\*\***.

### Day 3 — Saturday, 17 October 2026: Python Service Logic and Testing

- [x] Created `backend/app/services/assignment_service.py`.

- [x] Implemented `calculate_days_remaining(due_date: date, today: date) -> int`.

- [x] Tested future deadlines, overdue assignments, and deadlines due today.

- [x] Implemented `validate_assignment_title(title: str) -> str`.

- [x] Added title trimming and rejection of empty or whitespace-only titles using `ValueError`.

- [x] Created `backend/tests/test_assignment_service.py`.

- [x] Added assignment-service tests covering deadline calculations and title validation.

- [x] Resolved the Python import-path issue for pytest by setting `PYTHONPATH` to the backend directory during testing.

- [x] Verified the complete test suite: \***\*10 passed\*\***.

- [x] Verified package dependencies using `pip check`.

- [x] Confirmed `backend/requirements.txt` contains `fastapi`, `uvicorn[standard]`, and `pytest`.

- [x] Committed and pushed the Day 3 changes, as previously confirmed by the user.

- [x] Completed a basic Python class and object practice exercise on 20 October.

- [ ] Reinforce the concept that each object instance maintains its own attributes.

#### Verified Day 3 tests

The test suite covered:

1. Future deadline calculation.

2. Overdue assignment calculation.

3. Deadline due today.

4. Assignment title trimming.

5. Rejection of an empty title.

6. Rejection of a whitespace-only title.

7. Database table creation.

8. Valid assignment–subtask relationships.

9. Rejection of invalid assignment IDs.

10. Cascading deletion of subtasks.

Verified command:

```powershell

$env:PYTHONPATH = "$PWD\backend"

backend\.venv\Scripts\python.exe -m pytest backend\tests -v -p no:cacheprovider

```

Result: \***\*10 passed\*\***.

Dependency verification:

```powershell

backend\.venv\Scripts\python.exe -m pip check

```

Historical result: `No broken requirements found.`

Note: The Day 3 commit hash has not been independently verified here. Retrieve it using `git log -5 --oneline` rather than guessing.

### Day 4 — Sunday, 18 October 2026: SQL and Database Design

#### SQL queries and relationships

- [x] Inspected the existing `assignments` and `subtasks` tables.

- [x] Verified column names, data types, primary keys, and the foreign-key relationship.

- [x] Practised `SELECT` queries.

- [x] Practised filtering records with `WHERE`.

- [x] Practised counting records with `COUNT(*)`.
- [x] Practised aggregation with `GROUP BY`.

- [x] Practised joining assignments and subtasks with `JOIN`.

- [x] Practised counting subtasks per assignment with `LEFT JOIN`.

- [x] Used temporary practice data and verified that the practice script removed those records afterward.

- [x] Removed the temporary `backend/sql_practice.py` script.

#### Database constraints

Inspected the existing SQLite schema and verified that it already contains:

- [x] `PRIMARY KEY` constraints for both tables.

- [x] `NOT NULL` constraints on required fields.
