# PROJECT_STATUS — DeadlineOS

_*Last updated: Tuesday, 3 November 2026*_

**Latest committed application-code checkpoint:** `0450917` — `feat: add due-date sorting and overdue indicators`.

**Latest verified local work:** Week 4 Day 23 — Priority levels and upcoming-deadline summaries. Implemented and verified locally, but not yet committed or pushed.

Day 23 verification:
- Backend pytest: **59 passed**.
- Frontend ESLint: PASSED.
- Frontend production build: PASSED.
- Dashboard browser checks: PASSED, including refresh.
- `git diff --check`: PASSED.
- Eight tracked application files modified locally.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.

**Next roadmap task:** Week 4 Day 24 — Calendar or weekly deadline view.

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

- [x] Default values for assignment status, creation timestamp, and subtask completion.

- [x] `CHECK` constraint limiting assignment status to `pending`, `in_progress`, or `completed`.

- [x] `CHECK` constraint limiting `is_completed` to `0` or `1`.

- [x] Foreign-key constraint linking `subtasks.assignment_id` to `assignments.id`.

- [x] `ON DELETE CASCADE` for removing subtasks when their parent assignment is deleted.

#### Indexing

- [x] Inspected existing indexes.

- [x] Created the index `idx_subtasks_assignment_id` on `subtasks(assignment_id)`.

- [x] Verified that SQLite lists the new index using `PRAGMA index_list(subtasks)`.

Command used:

```sql

CREATE INDEX IF NOT EXISTS idx_subtasks_assignment_id

ON subtasks(assignment_id);

```

The index was created in the local SQLite database. Because the database file may be ignored by Git, the index may not exist in a fresh checkout or another environment. Reverify it after any database recreation or reset.

#### Constraint verification

- [x] Verified that an assignment with a `NULL` title is rejected.

- [x] Verified that an invalid assignment status is rejected.

- [x] Verified that a subtask referencing a nonexistent assignment is rejected.

- [x] Verified that an invalid subtask completion value is rejected.

- [x] Confirmed that the test script rolled back its attempted invalid inserts.

Foreign-key testing explicitly enabled `PRAGMA foreign_keys = ON` on the test connection.

#### Regression testing and cleanup

- [x] Reran the complete pytest suite after the database changes.

- [x] Verified all \***\*10 tests passed in 0.49 seconds\*\***.

- [x] Removed `backend/sql_practice.py`.

- [x] Verified that the working tree was clean at the time of the Day 4 check.

- [x] Verified that local `master` was up to date with `origin/master` at that time.

Day 4 result: \***\*SQL exercises, index creation, constraint verification, regression testing, and temporary-file cleanup completed.\*\***

The database index is a local database change. Do not claim that it has been committed or pushed to GitHub.

### Day 5 — Monday, 19 October 2026: HTTP and REST API Fundamentals

#### HTTP and REST concepts

- [x] Reviewed HTTP request and response fundamentals.

- [x] Reviewed REST resource URLs.

- [x] Reviewed HTTP methods and their purposes.

- [x] Reviewed HTTP status codes.

- [x] Reviewed JSON as a common API request and response format.

- [x] Reviewed HTTP headers.

- [x] Reviewed request validation.

- [x] Discussed authentication and authorization.

#### Knowledge check

- [x] Identified `/assignments/5` as a resource URL.

- [x] Correctly explained that authorization controls whether a logged-in student may edit another student's assignment.

- [x] Correctly identified `PATCH` as a method for partially updating a resource.

Day 5 result: \***\*HTTP/REST fundamentals and the knowledge check completed.\*\***

Note: A dedicated API client exercise using Postman or an equivalent tool has not yet been recorded as completed.

### Day 6 — Tuesday, 20 October 2026: Linux/CLI and Git Branching

#### Linux and WSL

- [x] Installed and started Ubuntu using WSL 2.

- [x] Verified the Ubuntu distribution was running as WSL version 2.

- [x] Navigated to the Windows project directory from Ubuntu at `/mnt/c/Users/kefztv/Desktop/DeadlineOS`.

- [x] Practised `pwd` to inspect the current directory.

- [x] Practised `ls -la` to inspect project files, including hidden files.

- [x] Practised `find backend -maxdepth 2 -type f` to locate backend files.

- [x] Practised changing directories into and out of `backend`.

- [x] Used `ss -ltnp` to inspect listening TCP sockets.

- [x] Used `ps aux` to inspect running processes.

- [x] Used Windows `netstat -ano` to inspect the port 8000 listener.

- [x] Used PowerShell `Get-Process` to inspect a Python process by PID.

- [x] Verified that `http://127.0.0.1:8000/health` returned a healthy status when the backend was running.

#### Processes and ports

- [x] Learned that `LISTENING` indicates a socket accepting incoming connections.

- [x] Learned that a PID identifies a process.

- [x] Compared the Windows-hosted FastAPI process with Linux process and socket inspection.

- [x] Identified that the FastAPI process was running on Windows rather than inside Ubuntu during the initial Linux checks.

Observed Windows listener:

```text

127.0.0.1:8000 ... LISTENING 15444

```

The Uvicorn server process was also inspected separately. The listener PID and Python server PID differed because Uvicorn reload mode can use a parent reloader process and a child server process.

#### Git branching and merge-conflict practice

- [x] Checked that `master` was up to date with `origin/master` before starting.

- [x] Created the local practice branch `practice/git-branching`.

- [x] Created and committed a temporary `git-practice.txt` file.

- [x] Created the local practice branch `practice/git-conflict`.

- [x] Changed the same line differently on each branch.

- [x] Triggered a real content merge conflict using `git merge practice/git-conflict`.

- [x] Inspected the conflict markers in `git-practice.txt`.

- [x] Resolved the conflict by writing the intended final content.

- [x] Staged the resolution and committed it as `c27ba48` — `practice: resolve Git merge conflict`.

- [x] Inspected the branch history with `git log --oneline --graph --all`.

- [x] Switched back to `master`.

- [x] Removed the accidental file `witch master`, which contained copied Git history output.

- [x] Deleted both temporary local practice branches after confirming that their commits were not part of `master`.

- [x] Verified that only `master` remained as a local branch.

- [x] Verified that `master` was still up to date with `origin/master`.

- [x] Confirmed that no practice commits were pushed to GitHub.

The practice merge and its commits were intentionally kept off `master`. The temporary branches were deleted after the exercise, so their commits are not part of the project's current `master` history.

Day 6 result: \***\*Linux/CLI fundamentals, process and port inspection, and Git branching/merge-conflict practice completed.\*\***

One concept remains to reinforce: distinguish a merge commit's two parents from a normal commit with a single parent.

### Backend API Implementation — Tuesday, 20 October 2026

#### Architecture review and MVP planning

- [x] Defined the initial MVP as a single-student assignment and subtask management application.

- [x] Deferred authentication, multiple-user accounts, and courses from the initial MVP.

- [x] Confirmed that assignment deletion should cascade to its subtasks.

- [x] Defined the first implementation priorities: assignment CRUD, subtask CRUD, validation, API testing, and frontend integration.

- [x] Created six GitHub issues for the planned MVP work.

GitHub issues:

1. [Assignment CRUD API](https://github.com/SANJIT06RAJ/DeadlineOS/issues/1)

2. [Subtask CRUD API](https://github.com/SANJIT06RAJ/DeadlineOS/issues/2)

3. [Assignment and subtask validation](https://github.com/SANJIT06RAJ/DeadlineOS/issues/3)

4. [API integration tests](https://github.com/SANJIT06RAJ/DeadlineOS/issues/4)

5. [Frontend dashboard and forms](https://github.com/SANJIT06RAJ/DeadlineOS/issues/5)

6. [Deadline sorting and overdue summaries](https://github.com/SANJIT06RAJ/DeadlineOS/issues/6)

The issues were created and were reported as open. Their current GitHub status has not been independently checked here.

#### Pydantic schemas

- [x] Created `backend/app/schemas.py`.

- [x] Defined assignment creation, update, and response schemas.

- [x] Defined subtask creation, update, and response schemas.

- [x] Restricted assignment status values to `pending`, `in_progress`, and `completed`.

- [x] Added request validation through Pydantic schemas.

Schemas implemented:

- `AssignmentCreate`

- `AssignmentUpdate`

- `AssignmentResponse`

- `SubtaskCreate`
- `SubtaskUpdate`

- `SubtaskResponse`

#### Assignment API endpoints

Implemented in `backend/app/main.py`:

- [x] `GET /assignments` — list assignments.

- [x] `POST /assignments` — create an assignment.

- [x] `GET /assignments/{assignment_id}` — retrieve one assignment.

- [x] `PATCH /assignments/{assignment_id}` — partially update an assignment.

- [x] `DELETE /assignments/{assignment_id}` — delete an assignment.

The assignment update logic rejects an update with no supplied fields and rejects `null` values for fields that are not optional. `description` and `due_date` are allowed to be set to `null`.

#### Subtask API endpoints

Implemented in `backend/app/main.py`:

- [x] `GET /assignments/{assignment_id}/subtasks` — list subtasks for an assignment.

- [x] `POST /assignments/{assignment_id}/subtasks` — create a subtask for an assignment.

- [x] `PATCH /subtasks/{subtask_id}` — partially update a subtask.

- [x] `DELETE /subtasks/{subtask_id}` — delete a subtask.

Subtask completion values are converted to Boolean values in API responses.

#### Application lifecycle

- [x] Replaced the deprecated FastAPI startup event pattern with an application lifespan handler.

- [x] Configured table creation through the lifespan handler.

- [x] Retained the root and health endpoints.

#### API integration testing

- [x] Created `backend/tests/test_assignment_api.py`.

- [x] Added tests for assignment and subtask API behaviour.

- [x] Added tests for update edge cases.

- [x] Installed the additional `httpx2` package into the backend virtual environment after the test client reported a missing requirement.

- [x] Resolved the FastAPI startup-event deprecation warning by using lifespan.

- [x] Ran the complete test suite after the API implementation.

- [x] Recorded the earlier full-suite result: \***\*27 passed\*\***.

- [x] Subsequently expanded the suite as part of deadline-summary implementation; the latest reported result is \***\*36 passed\*\***.

The installed `httpx2` dependency still needs to be checked against `backend/requirements.txt`. Do not assume the dependency has been recorded in the requirements file until it has been inspected and updated if necessary.

#### Git checkpoint

- [x] Committed the API implementation as `eb6a533` — `feat: implement assignment and subtask CRUD APIs`.

- [x] Successfully pushed the API commit to `origin/master`.

The API implementation commit included:

- `backend/app/main.py`

- `backend/app/schemas.py`

- `backend/tests/test_assignment_api.py`

The commit reported three files changed, with 599 insertions and two deletions.

### Deadline Sorting and Overdue Summaries — Completed

GitHub issue: [#6 — Deadline sorting and overdue summaries](https://github.com/SANJIT06RAJ/DeadlineOS/issues/6)

#### Implementation

- [x] Added deadline information to assignment API responses.

- [x] Added the `days_remaining` response field.

- [x] Added the `is_overdue` response field.

- [x] Ensured completed assignments are not classified as overdue.

- [x] Ensured assignments without due dates are not classified as overdue.

- [x] Added deadline-based sorting to `GET /assignments`.

- [x] Added `GET /assignments/summary`.

- [x] Added assignment counts by status.

- [x] Added overdue assignment counts.

- [x] Added due-today assignment counts.

- [x] Added upcoming assignment counts.

- [x] Added no-due-date assignment counts.

- [x] Added tests for assignment deadline response fields.

- [x] Added tests for overdue logic and completed assignments.

- [x] Added tests for deadline sorting.

- [x] Added tests for summary counts.

#### Files changed

- `backend/app/main.py`

- `backend/app/schemas.py`

- `backend/app/services/assignment_service.py`

- `backend/tests/test_assignment_api.py`

- `backend/tests/test_assignment_service.py`

#### Summary response schema

The `AssignmentSummary` schema contains:

- `total_assignments`

- `pending_assignments`

- `in_progress_assignments`

- `completed_assignments`

- `overdue_assignments`

- `due_today_assignments`

- `upcoming_assignments`

- `no_due_date_assignments`

#### Automated test result

Latest reported complete test suite: \***\*36 passed\*\***.

Command used:

```powershell

$env:PYTHONPATH = "$PWD\backend"

python -m pytest backend\tests -v -p no:cacheprovider

```

The test suite passed according to the latest reported output. Dependency verification and manual Swagger verification remain separate tasks.

#### Git checkpoint

- [x] Committed the implementation as `1e26949` — `feat: add deadline sorting and assignment summaries`.

- [x] Pushed the commit to `origin/master`.

- [x] Confirmed that local `master` was up to date with `origin/master`.

- [x] Left `backend/oop_practice.py` untracked and untouched.

Commit: https://github.com/SANJIT06RAJ/DeadlineOS/commit/1e26949

The deadline-summary feature implementation is complete. Manual API verification was subsequently completed during Day 7.

### Day 7 — Wednesday, 21 October 2026: API Verification and Deadline Response Fix

#### Manual Swagger verification

- [x] Started the FastAPI backend and opened Swagger UI at `http://127.0.0.1:8000/docs`.
- [x] Verified `GET /assignments/summary` returned HTTP 200.
- [x] Created temporary assignments to check overdue, due-today, upcoming, and status counts.
- [x] Confirmed the summary response matched the seven temporary records:
  - `total_assignments`: 7
  - `pending_assignments`: 6
  - `in_progress_assignments`: 1
  - `completed_assignments`: 0
  - `overdue_assignments`: 2
  - `due_today_assignments`: 3
  - `upcoming_assignments`: 2
  - `no_due_date_assignments`: 0
- [x] Found a bug: `GET /assignments` returned raw database rows and therefore did not calculate `days_remaining` and `is_overdue`.
- [x] Updated `list_assignments()` in `backend/app/main.py` to return `[serialize_assignment(row) for row in rows]`.
- [x] Rechecked the list endpoint and confirmed overdue assignments showed negative `days_remaining` and `is_overdue: true`; due-today and future assignments showed the expected values.
- [x] Confirmed the list was sorted by due date.
- [x] Reran the complete test suite after the fix: **36 passed**.
- [x] Deleted all temporary manual-test assignments with IDs `48` through `54`.

#### Git checkpoint

- [x] Committed the fix as `74532d1` — `fix: calculate deadline fields in assignment list`.
- [x] Pushed the commit to `origin/master`.
- [x] Confirmed `master` was up to date with `origin/master`.
- [x] Confirmed `backend/oop_practice.py` remained the only untracked file and was left untouched.

Day 7 result: **manual deadline API verification, response serialization fix, test rerun, temporary-data cleanup, and Git push completed.**


### Day 12 — Sunday, 25 October 2026: Assignment Filtering and Pagination

#### Requirements audit

- [x] Inspected `backend/app/main.py`, `backend/app/schemas.py`, and `backend/tests/test_assignment_api.py` before changing the implementation.
- [x] Confirmed that deadline sorting, deadline calculations, summary counts, and assignment status validation already existed.
- [x] Identified that `GET /assignments` did not yet support status filtering or pagination.

#### Implementation

- [x] Added an optional `status` query parameter to `GET /assignments`, reusing the existing `AssignmentStatus` type.
- [x] Supported filtering by `pending`, `in_progress`, and `completed`.
- [x] Added `limit` pagination, defaulting to 10 and accepting values from 1 to 100.
- [x] Added `offset` pagination, defaulting to 0 and rejecting negative values.
- [x] Used parameterized SQL values for the status filter, limit, and offset.
- [x] Preserved the existing response schema and due-date ordering, including placing assignments without due dates last.

#### Automated verification

- [x] Added `test_list_assignments_filters_by_status`.
- [x] Added `test_list_assignments_supports_limit_and_offset`.
- [x] Added `test_list_assignments_rejects_invalid_status_filter`.
- [x] Added `test_list_assignments_rejects_invalid_pagination`.
- [x] Verified the focused assignment API test file: **32 passed**.
- [x] Verified the full backend suite: **47 passed in 3.81 seconds**.
- [x] Ran `git diff --check` successfully with no reported whitespace errors.

**Day 12 outcome:** Assignment listing supports status filtering and pagination, with four tests covering the added behavior and invalid query parameters. The full backend suite passed on the committed version (**47 passed in 4.39 seconds**). Commit `77b135f` was pushed to `origin/master`; local and remote branches were verified synchronized. `backend/oop_practice.py` remains untracked and excluded.
### Day 13 — Monday, 26 October 2026: API Error-Handling Test Audit

#### Review and targeted tests

- [x] Inspected `backend/app/main.py`, `backend/app/schemas.py`, and the existing API tests before changing anything.
- [x] Confirmed existing coverage for missing resources (`404`), invalid title/status/query parameters (`422`), empty PATCH payloads (`400`), successful creation (`201`), and successful deletion (`204`).
- [x] Added `test_update_assignment_rejects_null_status`.
- [x] Added `test_update_subtask_rejects_null_completion_state`.
- [x] Added `test_create_assignment_rejects_invalid_due_date`.
- [x] Added `test_create_assignment_rejects_missing_title`.
- [x] Focused API test run reported: **36 passed in 2.08 seconds**.- [x] Added `test_update_assignment_rejects_mixed_valid_and_null_fields`, confirming a mixed valid/invalid PATCH returns HTTP 422 and leaves the assignment unchanged.
- [x] Reviewed `git diff --check`; no whitespace errors were reported.
- [x] Committed the five API validation tests as `0c0caab` — `test: expand API validation edge cases`.
- [x] Pushed the commit to `origin/master` and verified local `master` matches `origin/master`.
- [x] Full backend regression suite reported by the user: **52 passed**.
- [x] Confirmed `backend/oop_practice.py` remains untracked and excluded.

**Day 13 status:** Five targeted API validation tests are committed and pushed in `0c0caab`; the user reported 52 backend tests passed. The broader systematic review of HTTP responses and partial-update edge cases remains unfinished, so Day 13 is not yet complete.

### Day 14 — Thursday, 29 October 2026: API Documentation Review

**Planned focus:** Bug fixing and API documentation (scheduled for Wednesday, 28 October; completed review work on 29 October).

- [x] Reviewed `backend/app/main.py`, `backend/app/schemas.py`, and existing API test coverage.
- [x] Started the backend and confirmed Swagger UI at `/docs` opens successfully.
- [x] Reviewed the `POST /assignments` request schema, `PATCH /assignments/{assignment_id}` partial-update schema, and `GET /assignments` query parameters.
- [x] Confirmed the displayed request schemas, query parameters, and response examples looked correct.
- [x] Added explicit `404` response documentation to seven assignment/subtask operations in `backend/app/main.py`.
- [x] Retrieved the generated `/openapi.json` and verified `404` documentation for all seven operations.
- [x] Reran the full backend test suite after the changes: **52 passed**.
- [x] Reviewed `git status --short`, `git diff --check`, and the `main.py` diff; no whitespace errors were reported. `backend/oop_practice.py` remained untracked and excluded.
- [x] Committed the intended `backend/app/main.py` documentation change as `2000ce2` — `docs: document API not-found responses`.
- [x] Pushed the commit to `origin/master` and verified local `master` and `origin/master` match.

**Findings:** No confirmed functional bug requiring a code fix was identified in this review. The change documents existing missing-resource behavior without intentionally changing endpoint logic.

**Day 14 status:** Swagger and request/response documentation review, seven OpenAPI `404` checks, regression testing, and the code commit/push are complete. Commit `2000ce2` is synchronized with `origin/master`. The broader API validation/error-handling audit remains unfinished.

## 4. Current Database Design

Defined in `docs/PROJECT_PLAN.md` and previously verified against the local database schema.

### Assignments

- `id`: integer primary key with auto-increment.

- `title`: required text.

- `description`: optional text.

- `due_date`: optional date/time text.

- `status`: required text, default `pending`; allowed values are `pending`, `in_progress`, and `completed`.

- `created_at`: required text, default `CURRENT_TIMESTAMP`.

### Subtasks

- `id`: integer primary key with auto-increment.

- `assignment_id`: required integer foreign key referencing `assignments.id`.

- `title`: required text.

- `is_completed`: required integer Boolean (`0` or `1`), default `0`.

One assignment can have multiple subtasks. Deleting an assignment cascades to its subtasks.

### Indexes

- `idx_subtasks_assignment_id` on `subtasks(assignment_id)` existed in the local database when verified on 18 October 2026.

- Reverify this index if the database is recreated.

The index's presence in the local database does not mean the database file or index has been committed to Git.

## 5. Known Project Structure

```text

DeadlineOS/

├── .gitignore

├── README.md

├── ROADMAP.md

├── docs/

│   ├── PROJECT_PLAN.md

│   └── PROJECT_STATUS.md

├── backend/

│   ├── .venv/

│   ├── requirements.txt

│   ├── deadlineos.db

│   ├── oop_practice.py          # Local OOP exercise; currently untracked

│   ├── app/

│   │   ├── __init__.py

│   │   ├── main.py

│   │   ├── database.py

│   │   ├── schemas.py

│   │   └── services/

│   │       └── assignment_service.py

│   └── tests/

│       ├── test_database.py

│       ├── test_assignment_service.py

│       └── test_assignment_api.py

└── frontend/

```

Notes:

- `backend/deadlineos.db` is generated by the database connection. Verify the local file and `.gitignore` rules before committing database files.

- `backend/oop_practice.py` is an untracked local exercise file. Leave it untouched unless explicitly working on that exercise.

- The structure above records files known to exist from project history. Check the actual directory if additional files are needed.

## 6. Current Progress

### Completed

- [x] Day 1: Foundation setup.

- [x] Day 2: SQLite connection, tables, relationships, and database tests.

- [x] Day 3: Deadline calculations, assignment title validation, automated tests, and dependency verification.

- [x] Day 4: SQL queries, joins, grouping, constraints, index creation, and regression testing.

- [x] Day 5: HTTP and REST API fundamentals and knowledge check.

- [x] Day 6: Linux/CLI fundamentals, process and port inspection, and Git branching/merge-conflict practice.
- [x] Day 7: Manual Swagger verification, deadline response bug fix, regression tests, and temporary test-data cleanup.
- [x] Day 10: Fresh-database verification, SQLite initialization cleanup, and regression suite (**37 passed**); commit `ece13f6`.
- [x] Day 11: Added six CRUD edge-case tests, reran the full suite (**43 passed**), and pushed commit `15e89df`.
- [x] Day 12: Audited assignment-list requirements and implemented status filtering and pagination; the committed version passed (**47 passed**). Later API validation tests are recorded under Day 13.

- [x] Basic Python class and object practice exercise executed successfully.

- [x] Defined the initial MVP and implementation priorities.

- [x] Created six GitHub issues covering backend APIs, validation, testing, frontend work, and deadline summaries.

- [x] Implemented assignment CRUD endpoints.

- [x] Implemented subtask CRUD endpoints.

- [x] Added Pydantic request and response schemas.

- [x] Added API integration tests.

- [x] Replaced the deprecated FastAPI startup event with a lifespan handler.

- [x] Committed and pushed the API implementation as `eb6a533`.

- [x] Implemented deadline sorting and overdue summaries.

- [x] Added `days_remaining` and `is_overdue` to assignment responses.

- [x] Added `GET /assignments/summary`.

- [x] Added tests for overdue logic, deadline sorting, and summary counts.

- [x] Achieved a reported complete test suite result of \***\*36 passed\*\***.

- [x] Committed and pushed the deadline-summary implementation as `1e26949`.
- [x] Completed Day 7 manual Swagger verification and fixed assignment-list deadline serialization.
- [x] Reran the full test suite after the fix: **36 passed**.
- [x] Deleted temporary manual-test assignments `48`–`54`.
- [x] Committed and pushed the fix as `74532d1`.

### Outstanding

- [ ] Review additional API validation and error responses systematically; the Day 14 Swagger/OpenAPI review is complete, but the broader audit remains unfinished.
- [x] Review Swagger request schemas, query parameters, and response examples; verify the seven missing-resource `404` responses in OpenAPI.
- [x] Rerun the full backend suite after the Day 14 documentation changes: **52 passed**.
- [ ] Practise API requests using Postman or an equivalent client.
- [ ] Reinforce independent Python object-instance attributes.
- [ ] Reinforce the two-parent structure of a merge commit.
- [x] Create `docs/ER_DIAGRAM.md` documenting the `assignments`–`subtasks` relationship and verify it exists on GitHub.
- [x] Verify fresh SQLite database creation, required tables, foreign-key enforcement, repeatable initialization, and temporary database cleanup.
- [x] Defer migration tooling for the current SQLite MVP until safe modifications to existing tables or preservation of deployed data require it.
- [x] Reviewed and committed the `backend/app/database.py` connection-cleanup change as `ece13f6` — `fix: close database connections after initialization`.
- [x] Day 10 regression suite from `backend`: **37 passed** (historical result).
- [x] Day 11 regression suite from `backend`: **43 passed** after adding six CRUD edge-case tests.
- [x] Pushed the Day 11 test commit `15e89df` to `origin/master` and verified `master` was synchronized with `origin/master`.
- [x] Confirmed `backend/oop_practice.py` remains untracked, untouched, and excluded.
- [ ] Build the React dashboard and forms.
- [ ] Integrate the React frontend with the FastAPI backend.
- [ ] Implement reminders and workload tracking.
- [ ] Continue security improvements and broader testing.
- [ ] Add Docker and CI/CD when the application foundation is stable.
- [ ] Plan the optional AI document extraction feature with explicit user confirmation.

## 7. Unfinished Tasks and Exact Next Steps

The deadline-sorting and summary feature has been implemented, tested, committed, and pushed. The ER diagram is created and verified on GitHub. Day 10 fresh-database verification passed, including required tables, foreign-key enforcement, repeatable initialization, and temporary cleanup; migration tooling is deferred for the current SQLite MVP. The `backend/app/database.py` connection-cleanup change was reviewed, tested, committed as `ece13f6`, and pushed to `origin/master`. Day 11 added six CRUD edge-case tests and the full backend suite passed (**43 passed**); commit `15e89df` is pushed and local `master` is synchronized with `origin/master`. Next, audit validation, filtering, sorting, and pagination requirements as planned for Day 12.

### Step 1 — Completed: dependency verification

`backend/requirements.txt` includes `httpx2==2.15.1` according to the latest known project state. The latest reported `pip check` result was `No broken requirements found.`

### Step 2 — Completed: regression tests

The full test suite was rerun after the Day 7 assignment-list fix and reported **36 passed**.

### Step 3 — Completed: manual Swagger verification

The user verified deadline sorting, `days_remaining`, `is_overdue`, and the `/assignments/summary` counts. Temporary assignments with IDs `48`–`54` were deleted.

### Step 4 — Completed: ER diagram

`docs/ER_DIAGRAM.md` has been created and its presence on GitHub under `master` was verified. It documents the `assignments`–`subtasks` relationship.

### Step 5 — Completed: targeted CRUD edge-case verification

Reviewed the existing assignment and subtask API tests and added six tests in `backend/tests/test_assignment_api.py` covering missing assignment updates, listing subtasks for a missing assignment, missing subtask updates/deletes, and empty assignment/subtask PATCH payloads. The full backend suite passed (**43 passed**). The staged diff and `git diff --cached --check` were reviewed before commit `15e89df` (`test: cover CRUD API edge cases`) was pushed to `origin/master`; local `master` and `origin/master` are synchronized.

This completes the targeted Day 11 checks only. Broader systematic API validation/error-response review remains outstanding. The Day 10 database connection-cleanup change remains recorded as commit `ece13f6`. Keep `backend/oop_practice.py` untouched and excluded.

### Step 6 — Day 12 implementation verified; review and commit pending

- [x] Audited existing validation, deadline sorting, and summary behavior.
- [x] Implemented status filtering and pagination for `GET /assignments`.
- [x] Added four API tests covering filtering, pagination, and invalid query parameters.
- [x] Verified the complete backend suite: **47 passed in 3.81 seconds**.
- [x] Verified `git diff --check` reported no whitespace errors.
- [ ] Review the complete implementation and documentation diffs.
- [ ] Stage only the intended files: `backend/app/main.py`, `backend/tests/test_assignment_api.py`, `docs/PROJECT_STATUS.md`, and `docs/PROJECT_STATUS_WEEK_2.md`.
- [ ] Review the staged diff before committing.
- [ ] Commit and push the reviewed changes.
- [ ] Verify the resulting commit and synchronization with `origin/master`.

Keep `backend/oop_practice.py` untouched and untracked.

### Next feature after the Day 12 changes are committed

Proceed toward [GitHub issue #5 — Frontend dashboard and forms](https://github.com/SANJIT06RAJ/DeadlineOS/issues/5), following the roadmap and any remaining prerequisites.
### Historical verification details

The previous detailed dependency-verification instructions are retained below only as reference. Do not repeat completed steps unless a fresh check is needed.

<!-- Historical instructions begin -->

#### Historical Step — Inspect the requirements file

Open the project in VS Code:

`C:\Users\kefztv\Desktop\DeadlineOS`

Open:

`backend/requirements.txt`

Check whether `httpx2` is listed. It was installed in the virtual environment to resolve a test-client dependency error, but its presence in the requirements file has not yet been verified.

If it is missing, inspect the installed package version first:

```powershell

backend\.venv\Scripts\python.exe -m pip show httpx2

```

Confirm that the package is actually required by the current test setup before adding it. Record the appropriate version constraint rather than guessing or replacing the existing dependencies.

### Step 2 — Verify dependencies

From PowerShell in the project root, run:

```powershell

backend\.venv\Scripts\python.exe -m pip check

```

Record the actual output. Resolve dependency errors before proceeding.

### Step 3 — Rerun the complete test suite

Run:

```powershell

$env:PYTHONPATH = "$PWD\backend"

backend\.venv\Scripts\python.exe -m pytest backend\tests -v -p no:cacheprovider

```

Confirm the actual number of passing tests. The latest reported result is 36 passed, but record a new result only after seeing the command output.

If any test fails, resolve the failure before continuing.

### Step 4 — Inspect the API through Swagger UI

From the project root, start the backend:

```powershell

backend\.venv\Scripts\python.exe -m uvicorn app.main:app --app-dir backend --reload

```

Open:

`http://127.0.0.1:8000/docs`

Check the following read-only endpoints first:

1. `GET /health` — confirm that the backend is healthy.

2. `GET /assignments` — inspect assignment sorting and the `days_remaining` and `is_overdue` fields.

3. `GET /assignments/summary` — inspect the summary counts.

Compare the responses with the actual database contents. If you test create, update, or delete operations, use disposable test records and avoid deleting data that needs to be preserved.

Do not mark manual API verification complete until the results have been checked.

### Step 5 — Update and commit the status file

After dependency checks and API verification:

1. Update `docs/PROJECT_STATUS.md` with the actual results.

2. Run `git diff --check`.

3. Review `git diff`.

4. Stage only the intended project status changes.

5. Commit and push the status update.

6. Confirm the final output of `git status`.

Example commands after reviewing the changes:

```powershell

git status --short

git add docs/PROJECT_STATUS.md

git diff --cached --check

git diff --cached

```

Then, if the staged changes are correct:

```powershell

git commit -m "docs: update project status after deadline summaries"

git push origin master

git status

```

Leave `backend/oop_practice.py` untracked and untouched.

<!-- Historical instructions end -->

### Next feature after verification

Proceed to [GitHub issue #5 — Frontend dashboard and forms](https://github.com/SANJIT06RAJ/DeadlineOS/issues/5).

Build the React dashboard and forms, then integrate the frontend with the existing FastAPI backend.

Issue #6 — Deadline sorting and overdue summaries — has already been implemented and pushed. Check its current GitHub status rather than assuming whether the issue has been closed.

### Remaining reinforcement exercises

These short exercises can be completed separately without repeating the full lessons:

- Create two Python objects and demonstrate that changing one object's attributes does not change the other's attributes.

- Explain why a merge commit can have two parents while an ordinary commit normally has one.

- Send an API request and identify its HTTP method, status code, JSON response, and headers.

The schedule follows `ROADMAP.md`, but unfinished work takes priority over the calendar. Do not mark future tasks complete without evidence.

## 8. Useful Commands

### Start the backend

From the project root:

```powershell

backend\.venv\Scripts\python.exe -m uvicorn app.main:app --app-dir backend --reload

```

### Run all tests

From the project root:

```powershell

$env:PYTHONPATH = "$PWD\backend"

backend\.venv\Scripts\python.exe -m pytest backend\tests -v -p no:cacheprovider

```

### Check dependencies

```powershell

backend\.venv\Scripts\python.exe -m pip check

```

### Check Git status

```powershell

git status

```

### Check recent commits

```powershell

git log -5 --oneline

```

### Inspect the subtask index

```powershell

backend\.venv\Scripts\python.exe -c "import sqlite3; c=sqlite3.connect('backend/deadlineos.db'); print(*c.execute('PRAGMA index_list(subtasks)').fetchall(), sep='\n'); c.close()"

```

### Useful local URLs

- Root: `http://127.0.0.1:8000/`

- Health check: `http://127.0.0.1:8000/health`

- Swagger UI: `http://127.0.0.1:8000/docs`

## 9. Rules for Maintaining This File

- Preserve completed work from every previous day.

- Add new accomplishments under the appropriate dated section; do not erase historical progress.

- Update the current progress, unfinished tasks, and exact next step whenever work changes.

- Keep environment information, database design, project structure, and important commit references accurate.

- Record test results only after seeing actual output.

- Do not assume tasks are complete without confirmation or verification.

- Troubleshoot reported errors before moving forward.

- Keep explanations concise and use free tools where practical.

- Keep `ROADMAP.md` stable unless the schedule is intentionally revised.

- At the end of each work session, provide the updated status content and save it to GitHub when the user confirms the changes.

## 10. Latest Verified Git Checkpoint

- Branch: `master`.

- Remote: `origin/master`.

- Latest verified code checkpoint before Day 18: `c3361d9` — `docs: update overall status with week 3 progress`. Day 18 frontend integration is verified locally; its three code files are not yet committed or pushed. The latest backend code commit remains `725ce1b`.

- Added `test_update_assignment_can_clear_due_date`, verifying PATCH with `due_date: null` clears the optional deadline.

- Added `test_update_assignment_rejects_whitespace_title_without_partial_update`, verifying a whitespace-only title returns HTTP `422` and preserves the original title.

- The user reported the complete backend suite passed: **59 passed in 3.65 seconds**. This result was reported before commit `725ce1b`.

- Local `master` and `origin/master` were subsequently verified synchronized at repository head `a4797b4` after the two status-document commits. The latest code commit remains `725ce1b`. `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.
- Previous checkpoint: `ece13f6` — `fix: close database connections after initialization`; Day 10's full test suite passed (**37 passed**).

- Previous checkpoint: `74532d1` — `fix: calculate deadline fields in assignment list`.

- Earlier API implementation commit: `eb6a533` — `feat: implement assignment and subtask CRUD APIs`.

- Day 2 checkpoint: `f45ebd1` — `feat: add SQLite database and tests`.

- Earlier backend checkpoint: `a704806` — `feat: add initial FastAPI backend`.

- Initial repository commit: `0b0d2f8`.

- Day 3 changes were committed and pushed, as previously confirmed by the user. The exact commit hash has not been independently verified here.

- Day 6 practice merge commit: `c27ba48` — `practice: resolve Git merge conflict`. This commit was on a temporary practice branch and is \***\*not\*\*** part of `master`.

- Historical test checkpoints: Day 10 — **37 passed**; Day 11 — **43 passed**. The latest user-reported full backend suite is **59 passed in 3.65 seconds**, reported before code commit `725ce1b`; the two later commits changed documentation only.

- `backend/requirements.txt` includes `httpx2==2.15.1` according to the latest known project state.

- Latest reported `pip check` result: `No broken requirements found.`

- Manual Swagger verification of deadline fields and summary counts was completed on Day 7.

- `backend/oop_practice.py` remains the only untracked file at the latest local check and is intentionally untouched and excluded.

- The index was created in the local SQLite database; do not assume it is committed or pushed.

- The deadline-summary commit changed `backend/app/main.py`, `backend/app/schemas.py`, `backend/app/services/assignment_service.py`, `backend/tests/test_assignment_api.py`, and `backend/tests/test_assignment_service.py`.

- `docs/PROJECT_STATUS_WEEK_2.md` preserves the detailed Week 2 history and now records the follow-up validation-test verification after Day 14.

---

**Current next action:** Begin Week 3 Day 19 — implement assignment search and status filtering using the existing API. Courses remain outside the MVP. Day 18 integration is committed and pushed in `bf67fb5`; backend tests (**59 passed**), frontend lint/build, and browser persistence verification all passed. Keep `backend/oop_practice.py` untouched and excluded.


## 11. Week 3 Frontend Checkpoint — Day 15 (31 October 2026)

**Status: Day 15 completed.** The user confirmed that the initial frontend pages and navigation render correctly in the browser.

### React/Vite foundation

- [x] Initialized the React + Vite frontend in `frontend/`.
- [x] Selected ESLint and verified its configuration.
- [x] Installed `react-router-dom`, `axios`, and `lucide-react`.
- [x] Created modular directories for common components, assignment components, layout components, pages, services, and hooks.
- [x] Created layout components: `Sidebar.jsx`, `Header.jsx`, and `AppLayout.jsx`.
- [x] Created `DashboardPage.jsx` and `AssignmentsPage.jsx`.
- [x] Configured routes for `/` (Dashboard) and `/assignments` (Assignments).
- [x] Replaced the Vite starter screen with the initial DeadlineOS layout and responsive styling.
- [x] User confirmed the dashboard, assignments page, and navigation look correct.

### Verified frontend checks

- Node.js: `v24.18.0`.
- npm: `11.16.0`.
- React: `19.3.1`.
- Vite: `8.3.5`.
- React Router DOM: `7.18.5`.
- Axios: `1.21.0`.
- Lucide React: `1.65.0`.
- ESLint: `10.14.0`.
- `npm run lint`: passed with no errors.
- `npm run build`: passed; 2,041 modules transformed; JavaScript bundle 265.97 kB (84.63 kB gzipped); build completed in 2.67 seconds.
- Initial `npm audit` after dependency installation reported zero vulnerabilities.

### Scope and remaining work

- Dashboard statistic values are placeholders; the frontend is not connected to FastAPI yet.
- Assignment creation/editing, functional dashboard data, and API integration remain outstanding.
- No backend files or backend tests were changed during Day 15.
- Keep `backend/oop_practice.py` untouched and untracked.
- Keep the detailed Week 2 history in `docs/PROJECT_STATUS_WEEK_2.md`; it is complete and must not be modified as part of this update.
- Detailed Week 3 history is maintained separately in `docs/PROJECT_STATUS_WEEK_3.md`.

**Next roadmap task:** Day 16 — Dashboard and navigation. Build on the verified application shell; do not treat the placeholder dashboard statistics as functional backend data.


## 12. Week 3 Checkpoint — Days 16–17 (31 October 2026)

**Status: Days 16 and 17 completed and pushed in commit `4db8b0a`.** Detailed daily history is preserved in `docs/PROJECT_STATUS_WEEK_3.md`.

### Day 16 — Dashboard and Navigation

- [x] Improved the dashboard layout and styling.
- [x] Added statistic cards, Upcoming Deadlines, and Work Progress sections.
- [x] Added navigation from the dashboard to the assignments page.
- [x] User verified the dashboard in the browser.
- [x] `npm run lint` passed.
- [x] `npm run build` passed.

Dashboard figures and progress remain placeholders; they are not connected to backend data.

### Day 17 — Assignment Creation Form

- [x] Created `AssignmentForm.jsx` with title, optional description, optional due date, and status fields.
- [x] Added title validation (required, trimmed, maximum 200 characters) and status validation.
- [x] Added form error messages, Create Assignment, and Cancel actions.
- [x] Integrated the form into `AssignmentsPage.jsx`.
- [x] Added assignment cards and an empty state.
- [x] User tested the creation flow in the browser.
- [x] `npm run lint` passed with no errors.
- [x] `npm run build` passed; 2,042 modules transformed; JavaScript bundle 272.54 kB (86.43 kB gzipped).

**Current limitation:** Assignments are held in temporary React state and disappear after refresh. Axios integration and API-backed persistence are scheduled for Day 18. Assignment editing is not yet implemented.

### Git and synchronization

- Commit: `4db8b0a` — `feat: build DeadlineOS React frontend`.
- Pushed successfully to `origin/master`.
- User verified `git status -sb` showed `master...origin/master`.
- `backend/oop_practice.py` remains the only untracked file and is intentionally excluded.
- `docs/PROJECT_STATUS_WEEK_3.md` contains the detailed Week 3 history.
- `docs/PROJECT_STATUS_WEEK_2.md` remains unchanged.

**Next roadmap task:** Day 18 — React–FastAPI integration using Axios. Replace temporary assignment state with backend API calls and verify persistent assignment creation and retrieval.


## 13. Week 3 — Day 18: React–FastAPI Integration (1 November 2026)

**Status: IMPLEMENTED AND VERIFIED LOCALLY.** The frontend now retrieves and creates assignments through the existing FastAPI backend rather than relying on temporary component state.

### Implementation

- [x] Configured a Vite development proxy for `/api` to `http://127.0.0.1:8000`, rewriting the prefix before forwarding requests.
- [x] Created `frontend/src/services/api.js` with a shared Axios instance and `getAssignments()` / `createAssignment()` functions.
- [x] Updated `frontend/src/pages/AssignmentsPage.jsx` to fetch assignments on mount with `useEffect`.
- [x] Replaced local-only assignment creation with `POST /assignments`; the API response (including the database ID) is added to the list.
- [x] Added initial loading and request-error feedback.
- [x] Preserved the existing assignment form and backend architecture; no backend code changes were needed.

### Files changed

- `frontend/vite.config.js`
- `frontend/src/services/api.js` (new)
- `frontend/src/pages/AssignmentsPage.jsx`

### Verification evidence

- [x] `npm --prefix frontend run lint` — passed with no ESLint errors.
- [x] `npm --prefix frontend run build` — passed; 2,101 modules transformed.
- [x] FastAPI started successfully with Uvicorn; `GET /health` returned `healthy`.
- [x] Vite frontend loaded successfully through the development server.
- [x] Created a test assignment through the UI; the item appeared in the list.
- [x] Refreshed the browser; the assignment remained visible, verifying retrieval from persistent backend storage.
- [x] Direct `GET /assignments` response returned assignment ID `59`, title `Day 18 Integration Test`, description, due date `2026-11-15`, and status `in_progress`.
- [x] Backend regression suite: **59 passed**.

### Git and synchronization

- Frontend implementation commit: `bf67fb5` — `feat: integrate React assignments with FastAPI`.
- Push to `origin/master` succeeded; the user's final `git status -sb` showed `## master...origin/master`.
- `git log -4 --oneline --decorate` confirmed `bf67fb5` as `HEAD`, `origin/master`, and `origin/HEAD`.
- Only `backend/oop_practice.py` remains untracked; it was not staged or committed.
- Day 18 implementation and documentation are synchronized to GitHub. This status update records the verified final code checkpoint.

**Next roadmap task:** Day 20 — refine loading, empty, success, and error states. Day 19 search and status filtering is implemented and verified locally but remains uncommitted. Do not add course filtering; courses remain deferred from the single-student MVP.


## 14. Week 3 — Day 19: Assignment Search and Status Filtering (1 November 2026)

**Status: IMPLEMENTED, VERIFIED, COMMITTED, AND PUSHED.** Day 19 was completed ahead of its scheduled 2 November slot and is included in commit `c741796`.

### Implementation

- [x] Added client-side assignment search by title and description.
- [x] Added status filtering for All, Pending, In Progress, and Completed.
- [x] Combined search and status filtering so both criteria apply together.
- [x] Added a no-matching-assignments state and a Clear filters action.
- [x] Used useMemo to derive the filtered assignment list from the API-loaded assignments and current controls.
- [x] Corrected assignment CSS placement so the general assignment styles are outside the existing mobile-only media query; retained responsive rules for narrow screens.
- [x] Reused the existing FastAPI integration; no backend changes were required.
- [x] Did not add course filtering because courses remain deferred from the single-student MVP.

### Files changed

- `frontend/src/pages/AssignmentsPage.jsx`
- `frontend/src/App.css`

### Verification evidence

- [x] Manually tested title search and description search.
- [x] Manually tested Pending, In Progress, and Completed filters.
- [x] Manually tested combined search and status filtering.
- [x] Manually tested the no-results state and Clear filters action.
- [x] Manually tested assignment creation after adding the filters.
- [x] `npm run lint` — passed with no ESLint errors.
- [x] `npm run build` — passed; 2,101 modules transformed.
- [x] `git diff --check` — passed with no whitespace errors.

### Git state

- Day 19 source changes were committed and pushed in `c741796`.
- The local branch was synchronized with origin/master at `1df86ba` before Day 19 implementation.
- `backend/oop_practice.py` remains untracked, untouched, and excluded.

**Next roadmap task:** Week 4 — Advanced Functionality, beginning with due-date sorting and overdue detection. Day 21 integration verification is recorded in Section 16.



## 15. Week 3 — Day 20: Loading, Success, and Error States (2 November 2026)

**Status: IMPLEMENTED, VERIFIED, COMMITTED, AND PUSHED.** Day 20 was completed ahead of its scheduled 3 November slot and committed/pushed in `7f48e60`.

### Implementation

- [x] Added a loading indicator while assignments are retrieved.
- [x] Added a load-error state with a retry action.
- [x] Kept assignment-loading errors separate from assignment-creation errors.
- [x] Added a dismissible success notification after assignment creation.
- [x] Added submission loading feedback and disabled form controls while submitting.
- [x] Kept the form open and preserved entered values when assignment creation fails; displayed the creation error inside the modal.
- [x] Added a mounted guard and retry handling for assignment retrieval.

### Files changed

- `frontend/src/pages/AssignmentsPage.jsx`
- `frontend/src/components/assignments/AssignmentForm.jsx`
- `frontend/src/App.css`

### Verification evidence

- [x] `npm --prefix frontend run lint` — PASSED.
- [x] `npm --prefix frontend run build` — PASSED; 2,101 modules transformed.
- [x] `git diff --check` — PASSED.
- [x] Manually verified assignment loading and display, successful creation, backend-down load error, retry recovery, failed creation feedback inside the modal, preservation of form data, and successful retry after backend recovery.
- [ ] Empty-state behaviour was not explicitly retested during Day 20.
- [ ] Submission loading was implemented but its transient visual state was too brief to verify manually.
- [ ] Rapid double-submission prevention was not deliberately tested.

### Git state

- Day 20 frontend changes were committed and pushed in `7f48e60` — `feat: improve assignment loading and error states`.
- Final `git status -sb` confirmed `## master...origin/master`; `git log` confirmed `7f48e60` at `HEAD`, `origin/master`, and `origin/HEAD`.
- `backend/oop_practice.py` remains untracked, untouched, and excluded.
- No backend files were changed during Day 20.

**Next roadmap task:** Day 21 — integration workflow testing and bug fixing.


## 16. Week 3 Completion — Day 21 Integration Verification (2 November 2026)

**Status: COMPLETED — full-stack integration workflow verified.**

### Manual integration checks

- [x] FastAPI `/health` returned `healthy`.
- [x] Existing assignments loaded in the React frontend.
- [x] Created an assignment through the frontend.
- [x] Verified assignment persistence after browser refresh.
- [x] Verified search by assignment title and description.
- [x] Verified All, Pending, In Progress, and Completed filters.
- [x] Verified combined search and status filtering.
- [x] Verified the no-results state.
- [x] Verified assignment loading errors when the backend was unavailable.
- [x] Verified recovery through the retry action after restarting FastAPI.
- [x] Verified failed assignment submission displays an error and preserves form values.
- [x] Verified successful submission after backend recovery.

### Automated checks

- Backend pytest: **59 passed**.
- Frontend ESLint: PASSED.
- Frontend production build: PASSED — 2,101 modules transformed.
- `git diff --check`: PASSED.

### Verification limitations

- The true empty-assignment state was not separately tested; the no-results state was tested.
- The transient submission-loading visual state was not separately confirmed.
- Rapid double-submission prevention was not deliberately tested.

These are verification limitations, not confirmed defects. No application code changes were required during Day 21.

### Git state

- Before the documentation updates, local `master` was synchronized with `origin/master` at `9828898`.
- No tracked application files were modified during Day 21.
- `backend/oop_practice.py` remains untracked, untouched, and excluded.

### Week 3 outcome

**Week 3 deliverable achieved:** the DeadlineOS frontend communicates with the FastAPI backend, creates and retrieves persistent assignments, supports search and status filtering, and handles the tested loading and request-error recovery workflows.

Assignment editing, live dashboard statistics, and subtask UI remain future work and are not part of the completed Week 3 scope.

**Next roadmap task:** Week 4 — Advanced Functionality, beginning with due-date sorting and overdue detection.

## 17. Week 4 — Day 23: Priority Levels and Upcoming-Deadline Summaries (3 November 2026)

**Status: IMPLEMENTED AND VERIFIED LOCALLY — NOT YET COMMITTED OR PUSHED.**

### Implementation

- [x] Added assignment priority levels: `low`, `medium`, and `high`.
- [x] Added a database migration to introduce the priority column for existing databases, defaulting to `medium`.
- [x] Updated Pydantic schemas to support priority during assignment creation, updates, and responses.
- [x] Updated assignment API logic to save and update priority.
- [x] Added a priority selector to the assignment form.
- [x] Added priority badges to assignment cards with distinct visual styling.
- [x] Connected the dashboard to the existing assignment summary API.
- [x] Replaced placeholder dashboard statistics with backend data.
- [x] Added upcoming-deadline entries to the dashboard.
- [x] Added a calculated assignment completion percentage.
- [x] Added loading, error, and empty states for dashboard data.
- [x] Added styling for upcoming-deadline entries and dashboard errors.

### Files changed

- `backend/app/database.py`
- `backend/app/main.py`
- `backend/app/schemas.py`
- `frontend/src/App.css`
- `frontend/src/components/assignments/AssignmentForm.jsx`
- `frontend/src/pages/AssignmentsPage.jsx`
- `frontend/src/pages/DashboardPage.jsx`
- `frontend/src/services/api.js`

### Verification evidence

- [x] Database migration command completed successfully.
- [x] Priority schema check passed.
- [x] Backend pytest: **59 passed**.
- [x] Frontend `npm run lint` — PASSED.
- [x] Frontend `npm run build` — PASSED; 2,101 modules transformed.
- [x] Manually verified assignment priority selection and priority badge display.
- [x] Manually verified dashboard statistics.
- [x] Manually verified upcoming deadlines and due-date information.
- [x] Manually verified the work-progress completion percentage.
- [x] Refreshed the dashboard and confirmed data loaded again.
- [x] `git diff --check` — PASSED.

### Git state

- Eight tracked application files are modified locally.
- Local `master` was aligned with `origin/master` before these documentation updates, according to the reported Git status.
- Day 23 application changes have not yet been committed or pushed.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.

**Next roadmap task:** Day 24 — Calendar or weekly deadline view.
