# PROJECT_STATUS — DeadlineOS

_Last updated: Sunday, 18 October 2026_

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

## 2. Project Goal

DeadlineOS is an academic task and deadline management application for tracking assignments, due dates, subtasks, and progress.

Planned future features include deadline reminders, a React dashboard, Docker, CI/CD, security improvements, and optional AI-assisted document extraction. AI-extracted information must be reviewed and confirmed by the user before saving.

## 3. Completed Work History

### Day 1 — Thursday, 15 October 2026: Foundation Setup

- [x] Checked the development tools.
- [x] Created the Git repository at the correct project directory.
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
- [x] Verified all four database tests pass.
- [x] Removed the temporary `backend/check_db.py` verification script.
- [x] Committed the database work as `f45ebd1` — `feat: add SQLite database and tests`.
- [x] Successfully pushed the database commit to `origin/master`.

#### Verified Day 2 database tests

1. Table creation.
2. Valid assignment–subtask relationships.
3. Rejection of invalid assignment IDs.
4. Cascading deletion of subtasks.

Day 2 test result: **4 passed**.

### Day 3 — Saturday, 17 October 2026: Python Service Logic and Testing

- [x] Created `backend/app/services/assignment_service.py`.
- [x] Implemented `calculate_days_remaining(due_date: date, today: date) -> int`.
- [x] Tested future deadlines, overdue assignments, and deadlines due today.
- [x] Implemented `validate_assignment_title(title: str) -> str`.
- [x] Added title trimming and rejection of empty or whitespace-only titles using `ValueError`.
- [x] Created `backend/tests/test_assignment_service.py`.
- [x] Added six assignment-service tests covering deadline calculations and title validation.
- [x] Resolved the Python import-path issue for pytest by setting `PYTHONPATH` to the backend directory during testing.
- [x] Verified the complete test suite: **10 passed**.
- [x] Verified package dependencies using `pip check`.
- [x] Confirmed `backend/requirements.txt` contains `fastapi`, `uvicorn[standard]`, and `pytest`.
- [x] Committed and pushed the Day 3 changes, as previously confirmed by the user.
- [ ] Python class and object-oriented programming practice remains unfinished.

#### Verified Day 3 tests

The full test suite covers:

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

Result: **10 passed**.

Dependency verification:

```powershell
backend\.venv\Scripts\python.exe -m pip check
```

Result: `No broken requirements found.`

Note: The Day 3 commit hash has not been verified in this session. Retrieve it using `git log -5 --oneline` rather than guessing.

### Day 4 — Sunday, 18 October 2026: SQL and Database Design

#### SQL queries and relationships

- [x] Inspected the existing `assignments` and `subtasks` tables.
- [x] Verified the column names, data types, primary keys, and foreign-key relationship.
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

The index was created in the local SQLite database. Confirm that it exists after any database recreation or reset. Because the database file may be ignored by Git, the index may not be present in a fresh checkout or another environment.

#### Constraint verification

- [x] Verified that an assignment with a `NULL` title is rejected.
- [x] Verified that an invalid assignment status is rejected.
- [x] Verified that a subtask referencing a nonexistent assignment is rejected.
- [x] Verified that an invalid subtask completion value is rejected.
- [x] Confirmed that the test script rolled back its attempted invalid inserts.

Foreign-key testing explicitly enabled `PRAGMA foreign_keys = ON` on the test connection.

#### Regression testing and cleanup

- [x] Reran the complete pytest suite after the database changes.
- [x] Verified all **10 tests passed in 0.49 seconds**.
- [x] Removed `backend/sql_practice.py`.
- [x] Ran `git status`.
- [x] Verified that the working tree is clean.
- [x] Verified that the local `master` branch was up to date with `origin/master` at the time of the Git status check.

Day 4 result: **SQL exercises, index creation, constraint verification, regression testing, and temporary-file cleanup completed.**

The database index is a local database change; it was not separately committed to Git because the database file may be ignored. Do not claim that the index has been pushed to GitHub.

## 4. Current Database Design

Defined in `docs/PROJECT_PLAN.md` and verified against the local database schema.

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
- `is_completed`: required integer boolean (`0` or `1`), default `0`.

One assignment can have multiple subtasks. Deleting an assignment cascades to its subtasks.

### Indexes

- `idx_subtasks_assignment_id` on `subtasks(assignment_id)` exists in the local database as verified on 18 October 2026.
- Reverify this index if the database is recreated.

## 5. Known Project Structure

```text
DeadlineOS/
├── .gitignore
├── README.md
├── ROADMAP.md
├── docs/
│   ├── PROJECT_PLAN.md
│   └── PROJECT_STATUS.md
├── backend/
│   ├── .venv/
│   ├── requirements.txt
│   ├── deadlineos.db
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── database.py
│   │   └── services/
│   │       └── assignment_service.py
│   └── tests/
│       ├── test_database.py
│       └── test_assignment_service.py
└── frontend/
```

Note: `backend/deadlineos.db` is generated by the database connection. Verify the local file and `.gitignore` rules before committing database files.

## 6. Current Progress

- [x] Day 1: Foundation setup.
- [x] Day 2: SQLite connection, tables, relationships, and database tests.
- [x] Day 3: Deadline calculations, assignment title validation, automated tests, and dependency verification.
- [x] Day 4: SQL queries, joins, grouping, constraints, index creation, and regression testing.
- [ ] Python classes and object-oriented programming practice.
- [ ] Git branches, pull requests, and merge-conflict practice.
- [ ] HTTP methods, status codes, JSON, headers, validation, and authentication concepts.
- [ ] Linux/CLI fundamentals.
- [ ] Architecture review, MVP definition, and GitHub issues.
- [ ] Backend CRUD API and subsequent roadmap tasks.
- [ ] React frontend integration and subsequent planned features.

## 7. Unfinished Tasks and Next Step

### Immediate next task: Python classes and object-oriented programming

The original Day 3 plan included class practice, but completion has not been verified. Finish this outstanding task before moving deeper into HTTP/API topics.

1. Practise defining a class, its constructor, attributes, and instance methods.
2. Build a small assignment-related class without changing the existing production code.
3. Practise creating instances and calling methods.
4. Explain how a class differs from an instance and how this could be useful in DeadlineOS.
5. Run the relevant practice and review the results before marking the task complete.

### Remaining Week 1 topics

- [ ] Python class and object-oriented programming practice.
- [ ] Git branches, pull requests, and merge-conflict practice.
- [ ] HTTP methods, status codes, JSON, headers, request validation, and authentication concepts.
- [ ] Linux/CLI fundamentals.
- [ ] Architecture review, MVP definition, and GitHub issues.

SQL joins, grouping, constraints, and index practice were completed on Day 4. Do not repeat these topics unnecessarily; revisit them only if a knowledge check or implementation exposes a gap.

### After Python OOP

Proceed to HTTP and API fundamentals, then Linux/CLI practice and the Week 1 architecture review. Begin Week 2 backend CRUD work only after checking the remaining foundations and the roadmap.

The schedule follows `ROADMAP.md`, but unfinished work takes priority over the calendar. Do not mark future tasks complete without evidence.

## 8. Useful Commands

### Start the backend

```powershell
backend\.venv\Scripts\python.exe -m uvicorn app.main:app --app-dir backend --reload
```

### Run all tests

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

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/health`
- `http://127.0.0.1:8000/docs`

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
- Day 2 checkpoint: `f45ebd1` — `feat: add SQLite database and tests`.
- Day 3 changes: commit and push completed successfully, as confirmed by the user.
- Day 3 commit hash has not been verified in this session. Retrieve it with `git log -5 --oneline` rather than guessing.
- Latest verified full test suite: **10 passed in 0.49 seconds**, after the Day 4 database changes.
- Latest verified dependency check: `No broken requirements found.` (from Day 3).
- Latest verified working-tree status after cleanup: clean, with `master` up to date with `origin/master`.
- The index was created in the local SQLite database; do not assume it is committed or pushed.
