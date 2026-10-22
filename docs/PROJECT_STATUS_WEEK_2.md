# PROJECT STATUS — DEADLINEOS WEEK 2

**Week:** 22–28 October 2026
**Last updated:** Thursday, 22 October 2026
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

### Automated tests

- [x] Database tests.
- [x] Assignment service tests.
- [x] API integration tests.
- [x] Latest confirmed test result: **36 passed**.

The successful test command was run from the `backend` directory:

```powershell
python -m pytest tests -v -p no:cacheprovider
```

Running pytest from the repository root with `python -m pytest backend/tests -v` previously caused `ModuleNotFoundError: No module named 'app'` during test collection. This was an import-path issue, not a failed application assertion.

## 4. Daily Progress

### Day 8 — Thursday, 22 October 2026

**Focus:** Database schema, relationships, ER diagram, and regression testing.

- [x] Inspected the actual SQLite schema.
- [x] Documented the assignment–subtask relationship.
- [x] Reviewed primary keys, foreign keys, constraints, defaults, and cascading deletion.
- [x] Reviewed `backend/app/schemas.py`.
- [x] Reviewed `backend/app/main.py` for validation, PATCH handling, and SQL parameterization.
- [x] Ran the complete test suite successfully: **36 passed**.
- [x] Created `docs/ER_DIAGRAM.md` locally.
- [x] Created `docs/PROJECT_STATUS_WEEK_2.md` locally.
- [x] Ran `git diff --check` after creating the ER diagram.

**Day 8 outcome:** Database design reviewed, ER documentation created, Week 2 status documented, and regression tests passed.

**Git status at the latest checkpoint:**

- `docs/ER_DIAGRAM.md` — staged for commit.
- `docs/PROJECT_STATUS_WEEK_2.md` — staged for commit.
- `backend/oop_practice.py` — untracked and intentionally left untouched.

The latest staged whitespace check reported trailing whitespace on lines 3–5 of `docs/PROJECT_STATUS_WEEK_2.md`. Those lines need to be corrected, then the file restaged and `git diff --cached --check` rerun before committing.

**Commit and push status:** Not yet confirmed.

### Day 9 — Friday, 23 October 2026

**Planned focus:** FastAPI configuration and project structure.

- [ ] Review the current application structure.
- [ ] Review configuration and dependency management.
- [ ] Check how the application starts and creates database tables.
- [ ] Identify worthwhile structural improvements without unnecessary refactoring.
- [ ] Run regression tests after any changes.

**Completion evidence:** Configuration and startup behavior verified, changes documented where applicable, and actual test results recorded.

### Day 10 — Saturday, 24 October 2026

**Planned focus:** Database models and schema evolution.

- [ ] Review the current SQLite schema and database initialization.
- [ ] Determine whether a migration tool is justified for the current MVP.
- [ ] Verify database creation in a fresh environment.
- [ ] Recheck constraints and foreign-key behavior.

**Completion evidence:** Reproducible database setup and documented schema decisions.

### Day 11 — Sunday, 25 October 2026

**Planned focus:** CRUD verification.

- [x] Assignment CRUD endpoints already exist.
- [x] Subtask CRUD endpoints already exist.
- [ ] Review endpoint edge cases and response consistency.
- [ ] Confirm missing-resource and invalid-input behavior through tests.

**Completion evidence:** Existing CRUD behavior verified without duplicating completed implementation.

### Day 12 — Monday, 26 October 2026

**Planned focus:** Validation, filtering, sorting, and pagination.

- [x] Deadline-based assignment sorting already exists.
- [x] Assignment summary counts already exist.
- [x] Pydantic validation already exists.
- [ ] Audit filtering and pagination requirements.
- [ ] Implement only missing features useful for the MVP.
- [ ] Add tests for any new behavior.

**Completion evidence:** Requirements audit completed and any chosen additions tested.

### Day 13 — Tuesday, 27 October 2026

**Planned focus:** Error handling and API testing.

- [x] Existing API integration tests are present.
- [ ] Review HTTP status codes and error responses systematically.
- [ ] Test invalid payloads and missing resources.
- [ ] Verify partial-update edge cases.
- [ ] Run the full regression suite.

**Completion evidence:** Error handling tested and results recorded.

### Day 14 — Wednesday, 28 October 2026

**Planned focus:** Bug fixing and API documentation.

- [ ] Resolve confirmed Week 2 bugs.
- [ ] Review FastAPI Swagger documentation at `/docs`.
- [ ] Review API request and response examples.
- [ ] Run the complete regression suite.
- [ ] Review Git changes and record verified progress.

**Completion evidence:** Backend tested, useful API documentation reviewed, and Week 2 status accurately updated.

## 5. Known Outstanding Work

- [ ] Correct the trailing whitespace in lines 3–5 of this file and rerun the staged whitespace check.
- [ ] Review the staged changes for `docs/ER_DIAGRAM.md` and `docs/PROJECT_STATUS_WEEK_2.md`.
- [ ] Commit and push the intended documentation changes to GitHub.
- [ ] Keep this Week 2 status file separate from the cumulative `docs/PROJECT_STATUS.md`.
- [ ] Continue auditing API validation and error responses.
- [ ] Practise API requests using Swagger UI, Postman, or an equivalent client where useful.
- [ ] Confirm dependency consistency with `backend/requirements.txt` when needed.
- [ ] Review whether database migration tooling is necessary for the MVP.
- [ ] Continue frontend development and React–FastAPI integration according to the roadmap.
- [ ] Leave `backend/oop_practice.py` untouched unless deliberately resuming that exercise.

These items must only be marked complete after the work has been performed and verified.

## 6. Git and Testing Rules

Before committing:

```powershell
git status --short
git diff --check
git diff
```

When checking staged changes:

```powershell
git diff --cached --check
git diff --cached --stat
git diff --cached
```

Stage only the files intended for the commit. Avoid `git add .` while unrelated untracked files exist.

For backend tests, run from the `backend` directory:

```powershell
python -m pytest tests -v -p no:cacheprovider
```

Record the actual result after each test run. Do not assume the test count remains unchanged after adding or removing tests.

## 7. Week 2 Completion Criteria

Week 2 is complete when:

- [ ] Database relationships and constraints are documented.
- [ ] ER diagram is reviewed and committed.
- [ ] Existing FastAPI configuration and project structure are understood.
- [ ] Database initialization and schema decisions are documented.
- [ ] Existing CRUD behavior is verified.
- [ ] Validation, sorting, filtering, and pagination requirements are audited.
- [ ] API error handling and regression tests are reviewed.
- [ ] API documentation is checked.
- [ ] Final test results are recorded.
- [ ] Intended documentation changes are committed and pushed.
- [ ] The cumulative project status is preserved and updated only when appropriate.

**Progress rule:** Existing features count as implemented, but planned verification tasks remain unfinished until checked. Never mark future work complete without evidence.

---

**Next action:** Save this file, remove the trailing whitespace from lines 3–5, restage it, and rerun `git diff --cached --check`. Then verify both staged documentation files before committing and pushing them.
