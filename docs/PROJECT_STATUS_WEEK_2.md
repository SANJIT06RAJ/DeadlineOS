# PROJECT STATUS — DEADLINEOS WEEK 2

**Week:** 22–28 October 2026
**Last updated:** Friday, 23 October 2026
**Primary project status:** `docs/PROJECT_STATUS.md`
**Learning schedule:** `ROADMAP.md`

---

## 1. Week 2 Goal

Build a reliable, database-backed FastAPI foundation for DeadlineOS, including:

- Database schema and relationships.
- API structure and configuration.
- Assignment and subtask CRUD.
- Request validation and error handling.
- Filtering, sorting, and pagination where needed.
- Automated API tests and documentation.

**Important:** The backend was implemented ahead of the original schedule during Week 1. Week 2 should improve and verify the existing implementation instead of rebuilding completed features unnecessarily.

## 2. Environment

- OS: Windows
- Project directory: `C:\Users\kefztv\Desktop\DeadlineOS`
- Git branch: `master`
- Backend: FastAPI + Uvicorn
- Database: SQLite
- Validation: Pydantic
- Testing: pytest
- Python virtual environment: `backend\.venv`
- Frontend: React + Vite
- Remote repository: https://github.com/SANJIT06RAJ/DeadlineOS

## 3. Existing Implementation

### Database

File: `backend/app/database.py`

- [x] SQLite connection setup.
- [x] `assignments` table.
- [x] `subtasks` table.
- [x] Primary keys and required-field constraints.
- [x] Assignment status constraint: `pending`, `in_progress`, `completed`.
- [x] Subtask completion constraint: `0` or `1`.
- [x] Foreign key from `subtasks.assignment_id` to `assignments.id`.
- [x] Cascading deletion of subtasks when an assignment is deleted.
- [x] Foreign-key enforcement enabled for each database connection.
- [x] Database schema and foreign-key behavior covered by a dedicated test.

### API and validation

Files:

- `backend/app/main.py`
- `backend/app/schemas.py`
- `backend/app/services/assignment_service.py`

- [x] Root and health endpoints.
- [x] Assignment create, list, retrieve, update, and delete endpoints.
- [x] Subtask create, list, update, and delete endpoints.
- [x] Pydantic request and response schemas.
- [x] Assignment title validation.
- [x] Subtask title validation.
- [x] Partial-update handling and empty PATCH rejection.
- [x] Parameterized SQL queries for user-provided values.
- [x] Deadline calculations and overdue detection.
- [x] Deadline-based assignment sorting.
- [x] Assignment summary endpoint.

These features already exist. Their remaining edge cases and response behavior still need systematic verification where indicated in the daily plan.

### Automated tests

- [x] Database tests.
- [x] Assignment service tests.
- [x] API integration tests.
- [x] Database tests updated to use a temporary SQLite database per test.
- [x] Invalid foreign-key test updated to use `pytest.raises(sqlite3.IntegrityError)`.
- [x] Added `test_database_schema_and_foreign_keys`.
- [x] Full backend test suite passed: **37 passed**.
- [x] Reviewed the intended staged test changes.
- [x] `git diff --cached --check` passed before the test commit.

Run the backend test suite from the `backend` directory:

```powershell
python -m pytest tests -v
```

**Test execution note:** A root-level pytest invocation previously failed during test
collection with `ModuleNotFoundError: No module named 'app'`. Running the full suite from
the `backend` directory resolved the import-path issue; all 37 tests passed.

Run future tests from the `backend` directory and record the actual result. Do not assume the test count remains unchanged after adding or removing tests.

## 4. Daily Progress

### Day 8 — Thursday, 22 October 2026

**Focus:** Database schema, relationships, ER diagram, and regression testing.

- [x] Inspected the actual SQLite schema.
- [x] Documented the assignment–subtask relationship.
- [x] Reviewed primary keys, foreign keys, constraints, defaults, and cascading deletion.
- [x] Reviewed `backend/app/schemas.py`.
- [x] Reviewed `backend/app/main.py` for validation, PATCH handling, and SQL parameterization.
- [x] Ran the complete test suite successfully: **36 passed**.
- [x] Created `docs/ER_DIAGRAM.md`.
- [x] Created `docs/PROJECT_STATUS_WEEK_2.md`.
- [x] Ran `git diff --check` after creating the ER diagram.
- [x] Subsequently verified that `docs/ER_DIAGRAM.md` exists on GitHub under `master`.

**Day 8 outcome:** Database design reviewed, ER documentation created and subsequently verified on GitHub, Week 2 status documented, and regression tests passed.

**Original Day 8 Git checkpoint:**

- `docs/ER_DIAGRAM.md` — reported as staged at that checkpoint; its current presence on GitHub was verified separately.
- `docs/PROJECT_STATUS_WEEK_2.md` — reported as staged at that checkpoint.
- `backend/oop_practice.py` — untracked and intentionally left untouched.

The earlier staged state must not be assumed to reflect the current Git index.

### Day 9 — Backend Test Isolation and Regression Verification

**Scheduled focus:** FastAPI configuration and project structure.

**Work completed and verified:**

- [x] Reviewed the existing backend routes, schemas, database setup, service logic, and tests.
- [x] Updated `backend/tests/test_database.py` to use a separate temporary SQLite database for each test through `tmp_path` and `monkeypatch`.
- [x] Updated the invalid foreign-key test to explicitly expect `sqlite3.IntegrityError` using `pytest.raises`.
- [x] Reviewed the database test changes.
- [x] Ran the backend test suite successfully at the Day 9 checkpoint: **36 passed**.
- [x] Ran `git diff --check` successfully with no reported whitespace errors.
- [x] Preserved the Day 8 history in the Week 2 status record.
- [x] Committed and pushed the database test-isolation changes in commit `81a9d80` (`test: isolate database tests and update week 2 status`).

**Day 9 outcome:** Database tests use isolated temporary databases, and invalid foreign-key rejection is tested explicitly. The Day 9 changes were published to GitHub. Additional schema verification was completed during the following session.

### Day 10 — Friday, 23 October 2026

**Roadmap schedule:** Saturday, 24 October 2026.
**Actual session date:** Friday, 23 October 2026.

**Focus:** Database initialization, schema verification, and test reliability.

**Work completed and verified:**

- [x] Inspected `backend/app/database.py`.
- [x] Reviewed how the SQLite database path is derived from `__file__`.
- [x] Confirmed that `get_connection()` enables SQLite foreign-key enforcement on each connection.
- [x] Reviewed the `assignments` and `subtasks` table definitions, constraints, and cascading deletion.
- [x] Reviewed the `create_tables()` database initialization function.
- [x] Reviewed how `backend/app/main.py` calls `create_tables()` through the FastAPI lifespan.
- [x] Reviewed the temporary-database isolation approach in `backend/tests/test_database.py`.
- [x] Added `test_database_schema_and_foreign_keys` to verify required schema columns, connection-level foreign-key enforcement, and the foreign-key relationship with `ON DELETE CASCADE`.
- [x] Ran the full backend test suite from the `backend` directory: **37 passed**.
- [x] Corrected the trailing newline in `backend/tests/test_database.py` and reran the full suite: **37 passed**.
- [x] Reviewed the intended staged diff and confirmed it contained the database test changes.
- [x] Ran `git diff --cached --check` successfully.
- [x] Committed the schema-verification test.
- [x] Pushed the commit to GitHub and verified that local `master` was synchronized with `origin/master`.
- [x] Verified the commit: `6b70998` — `test: verify database schema and foreign keys`.
- [x] Verified that `docs/ER_DIAGRAM.md` exists on GitHub under `master`.

**Day 10 Git checkpoint:**

- Latest verified commit: `6b70998` — `test: verify database schema and foreign keys`.
- Remote: `origin/master`.
- Local branch: `master`, reported up to date with `origin/master`.
- `backend/tests/test_database.py` — schema-verification test committed and pushed.
- `backend/oop_practice.py` — untracked and intentionally excluded from the project commit.

**Still pending:**

- [ ] Decide whether a migration tool is justified for the current MVP.
- [ ] Verify database creation and initialization in a fresh environment.
- [ ] Record the reproducibility result and any required setup steps.

**Day 10 outcome:** Added database schema and foreign-key regression coverage, verified that all 37 backend tests passed, and pushed the intended test change. Fresh-database reproducibility and the migration-tool decision remain open.

### Day 11 — Sunday, 25 October 2026

**Planned focus:** CRUD verification.

- [x] Assignment CRUD endpoints already exist.
- [x] Subtask CRUD endpoints already exist.
- [ ] Review endpoint edge cases and response consistency.
- [ ] Confirm missing-resource and invalid-input behavior through tests.

**Completion criteria:** Existing CRUD behavior verified without duplicating completed implementation.

### Day 12 — Monday, 26 October 2026

**Planned focus:** Validation, filtering, sorting, and pagination.

- [x] Deadline-based assignment sorting already exists.
- [x] Assignment summary counts already exist.
- [x] Pydantic validation already exists.
- [ ] Audit filtering and pagination requirements.
- [ ] Implement only missing features useful for the MVP.
- [ ] Add tests for any new behavior.

**Completion criteria:** Requirements audit completed and any chosen additions tested.

### Day 13 — Tuesday, 27 October 2026

**Planned focus:** Error handling and API testing.

- [x] Existing API integration tests are present.
- [ ] Review HTTP status codes and error responses systematically.
- [ ] Test invalid payloads and missing resources.
- [ ] Verify partial-update edge cases.
- [ ] Run the full regression suite.

**Completion criteria:** Error handling tested and results recorded.

### Day 14 — Wednesday, 28 October 2026

**Planned focus:** Bug fixing and API documentation.

- [ ] Resolve confirmed Week 2 bugs.
- [ ] Review FastAPI Swagger documentation at `/docs`.
- [ ] Review API request and response examples.
- [ ] Run the complete regression suite.
- [ ] Review Git changes and record verified progress.

**Completion criteria:** Backend tested, useful API documentation reviewed, and Week 2 status accurately updated.

## 5. Known Outstanding Work

- [x] Create `docs/ER_DIAGRAM.md` and verify that it exists on GitHub under `master`.
- [x] Correct the previously reported trailing whitespace in the Week 2 status document; `git diff --check` subsequently passed.
- [x] Review the changes to `backend/tests/test_database.py`.
- [x] Update the Week 2 status record while preserving Day 8 and Day 9 history.
- [x] Rerun the full backend test suite from the `backend` directory: **37 passed**.
- [x] Review the staged database test diff before committing.
- [x] Commit and push the schema-verification test.
- [x] Verify the latest test commit and that local `master` is synchronized with `origin/master`.
- [x] Keep `backend/oop_practice.py` untouched and excluded from the project commit.
- [ ] Verify fresh-database creation and reproducibility.
- [ ] Decide whether database migration tooling is necessary for the MVP.
- [ ] Continue auditing API validation and error responses.
- [ ] Practise API requests using Swagger UI, Postman, or an equivalent client where useful.
- [ ] Confirm dependency consistency with `backend/requirements.txt` when needed.
- [ ] Continue frontend development and React–FastAPI integration according to the roadmap.

Items are marked complete only when the work has been performed and verified. Historical test results remain historical; use new test output when validating later changes.

## 6. Git and Testing Rules

Before committing, inspect the working tree:

```powershell
git status --short
git diff --check
git diff
```

Inspect staged changes separately:

```powershell
git diff --cached --check
git diff --cached --stat
git diff --cached
```

Stage only files intended for the commit. Avoid `git add .` while unrelated untracked files exist.

Run backend tests from the `backend` directory:

```powershell
python -m pytest tests -v
```

Record the actual result after each test run. Do not assume the test count remains unchanged after adding or removing tests.

Keep `backend/oop_practice.py` untouched and excluded unless deliberately resuming that exercise.

## 7. Week 2 Completion Criteria

Week 2 is complete when:

- [x] Database relationships and constraints are documented.
- [x] ER diagram created and verified on GitHub.
- [ ] Existing FastAPI configuration and project structure are understood and reviewed.
- [ ] Database initialization, fresh-database reproducibility, and schema decisions are verified and documented.
- [ ] Existing CRUD behavior is verified, including relevant edge cases.
- [ ] Validation, sorting, filtering, and pagination requirements are audited.
- [ ] API error handling and regression tests are reviewed.
- [ ] API documentation is checked.
- [x] Backend test suite passed at the latest verified checkpoint: **37 passed**.
- [x] Intended database test changes were committed and pushed.
- [ ] Remaining Week 2 verification work is completed and recorded.
- [ ] The cumulative project status is preserved and updated only when appropriate.

**Progress rule:** Existing features count as implemented, but planned verification tasks remain unfinished until checked. Never mark future work complete without evidence.

---

**Next action:** Continue with Day 10's outstanding checks. First, determine whether migration tooling is necessary for the current SQLite MVP. Then verify that the database can be created reproducibly in a fresh environment. Keep `backend/oop_practice.py` excluded from all project changes.
