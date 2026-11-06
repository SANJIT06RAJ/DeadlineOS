# PROJECT_STATUS_WEEK_6 — DeadlineOS

_Last updated: Friday, 6 November 2026_

## Week 6 — Day 36: Authentication, Sessions, and Password Handling

**Status: COMPLETED — SECURITY LEARNING LAB VERIFIED LOCALLY.**

### Learning

- [x] Reviewed authentication versus authorization.
- [x] Understood why passwords must be securely hashed instead of stored as plaintext.
- [x] Reviewed session-cookie authentication flow.
- [x] Learned the purpose of `HttpOnly`, `Secure`, `SameSite`, session expiry, session rotation, and server-side session invalidation.

### Implementation

- [x] Installed `argon2-cffi==25.1.0` in the local backend virtual environment.
- [x] Created `backend/scripts/security_lab_passwords.py`.
- [x] Implemented password hashing and verification using Argon2id.
- [x] Added handling for incorrect passwords and invalid stored hashes.
- [x] Created `backend/tests/test_security_lab_passwords.py`.

### Verification

- [x] Confirmed generated hashes use the Argon2id format.
- [x] Confirmed correct passwords are accepted.
- [x] Confirmed incorrect passwords are rejected.
- [x] Confirmed identical passwords generate different salted hashes.
- [x] Confirmed empty passwords are rejected.
- [x] Confirmed malformed stored hashes are rejected.
- [x] Dedicated security lab tests: **6 passed**.

### Scope and dependency decisions

- Authentication and multiple-user accounts remain outside the initial single-student MVP.
- This is an isolated learning lab; no login, registration, session management, or user-account functionality was added to the application.
- `argon2-cffi` was installed locally for the exercise and was not added to `backend/requirements.txt`.

### Files created

- `backend/scripts/security_lab_passwords.py`
- `backend/tests/test_security_lab_passwords.py`

### Git state at Day 36 checkpoint

- The two security lab files and this Week 6 status file were committed as `6c8aa81` — `security: add Argon2id password hashing lab`.
- The commit was successfully pushed to `origin/master`.
- `backend/oop_practice.py` remains untouched, untracked, and intentionally excluded.
- The overall project status will be synchronized separately.

**Next roadmap task:** Day 37 — User-level access controls. Keep the exercise within the existing single-student MVP scope unless a scope change is explicitly approved.

## Week 6 — Day 37: User-Level Access Controls (6 November 2026)

**Status: IMPLEMENTED, VERIFIED, COMMITTED, AND PUSHED (`9bdc7b2`).**

### Learning
- [x] Reviewed resource ownership and user-level authorization.
- [x] Practised allowing users to access only resources they own.
- [x] Distinguished between HTTP 403 (forbidden) and HTTP 404 (not found).

### Implementation
- [x] Created `backend/scripts/security_lab_access_control.py`.
- [x] Implemented a `Resource` data class with resource ID, owner ID, and title.
- [x] Implemented `get_owned_resource()` to verify resource ownership.
- [x] Returned HTTP 404 when a resource does not exist.
- [x] Returned HTTP 403 when a user attempts to access another user's resource.
- [x] Created `backend/tests/test_security_lab_access_control.py`.

### Verification
- [x] Confirmed a user can access their own resource.
- [x] Confirmed access to another user's resource is blocked with HTTP 403.
- [x] Confirmed missing resources return HTTP 404.
- [x] Dedicated access-control tests: **4 passed**.
- [x] Standalone security lab execution: PASSED.
- [x] Full backend pytest suite: **118 passed**.

### Scope decisions
- The exercise remains an isolated security learning lab.
- No production authentication, user accounts, database ownership fields, or multi-user functionality were added.
- The initial DeadlineOS MVP remains single-student.

### Files created
- `backend/scripts/security_lab_access_control.py`
- `backend/tests/test_security_lab_access_control.py`

### Git state
- `backend/scripts/security_lab_access_control.py` and `backend/tests/test_security_lab_access_control.py` were committed as `9bdc7b2` — `security: add user-level access control lab`.
- The commit was successfully pushed to `origin/master`.
- Local `master` and `origin/master` were verified synchronized at `9bdc7b2`.
- `backend/oop_practice.py` remains untouched, untracked, and intentionally excluded.

**Next roadmap task:** Day 38 — Unit tests for deadline logic and business rules.

## Week 6 — Day 38: Unit Tests for Deadline Logic and Business Rules (6 November 2026)

**Status: COMPLETED, VERIFIED, COMMITTED, AND PUSHED (`5ed6388`).**

### Implementation
- [x] Expanded `backend/tests/test_assignment_service.py` with four additional boundary tests.
- [x] Added leap-year deadline calculation coverage.
- [x] Added year-boundary deadline calculation coverage.
- [x] Added overdue classification coverage for an in-progress assignment.
- [x] Added coverage confirming a completed assignment due today is not overdue.

### Verification
- [x] Assignment service test suite: **14 passed**.
- [x] Full backend pytest regression suite: **122 passed**.
- [x] `git diff --check`: PASSED.
- [x] Reviewed the final diff and confirmed only the intended test file was staged.
- [x] Confirmed `backend/oop_practice.py` remained untouched and excluded.

### Files changed
- `backend/tests/test_assignment_service.py`

### Git state
- The test changes were committed as `5ed6388` — `test: expand assignment service boundary coverage`.
- The commit was successfully pushed to `origin/master`.
- Final Git verification confirmed local `master` and `origin/master` synchronized at `5ed6388`.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.

**Next roadmap task:** Day 39 — API integration and frontend workflow tests.

## Week 6 — Day 39: API Integration and Frontend Workflow Tests

**Status: COMPLETED, VERIFIED, COMMITTED, AND PUSHED (`7512b24`).**

### Implementation
- [x] Installed Vitest and React Testing Library dependencies.
- [x] Configured Vitest with the jsdom environment.
- [x] Created the shared test setup file.
- [x] Added frontend test scripts.
- [x] Created AssignmentForm component tests.
- [x] Created AssignmentsPage workflow tests.
- [x] Mocked API service functions to isolate frontend workflow behaviour.

### Test coverage

**AssignmentForm — 7 tests**
- Form rendering.
- Empty-title validation.
- Input trimming and submission.
- Existing assignment data in edit mode.
- Cancel callback.
- Disabled controls during submission.
- Submission error display.

**AssignmentsPage — 6 tests**
- Assignment loading and display.
- Search by title and description.
- Status filtering.
- Assignment creation and success message.
- Assignment loading error.
- Retry after loading failure.

### Verification
- [x] Frontend test suite: **13 passed**.
- [x] Frontend ESLint: PASSED.
- [x] Vite production build: PASSED; 2,105 modules transformed.
- [x] `git diff --check`: PASSED.
- [x] Reviewed the frontend testing configuration and both test files.

### Files changed
- `frontend/package.json`
- `frontend/package-lock.json`
- `frontend/vite.config.js`
- `frontend/src/test/setup.js`
- `frontend/src/components/assignments/AssignmentForm.test.jsx`
- `frontend/src/pages/AssignmentsPage.test.jsx`

### Testing scope note
- Frontend API calls are mocked in the AssignmentsPage tests.
- These tests verify frontend workflows and API-service interactions, not a live end-to-end connection against FastAPI.
- Existing backend API integration tests remain separate.

### Git state
- The six intended Day 39 frontend testing/configuration files were committed as `7512b24` — `test: add frontend assignment workflow tests`.
- The commit was successfully pushed to `origin/master`.
- Final local Git verification confirmed `HEAD` and `origin/master` both point to `7512b24`, with no pending tracked changes.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.

**Next roadmap task:** Day 40 — Invalid-input, missing-field, upload, and permission tests.

## Week 6 — Day 40: Invalid-Input, Missing-Field, Upload, and Permission Tests

**Status: COMPLETED, VERIFIED, COMMITTED, AND PUSHED (`c22197f`).**

### Implementation
- [x] Created `backend/tests/test_document_api.py`.
- [x] Added seven tests for the PDF document preview endpoint.
- [x] Covered missing uploads, invalid extensions, empty files, invalid PDF signatures, oversized files, PDFs without extractable text, and successful previews.

### Verification
- [x] Dedicated document API tests: **7 passed**.
- [x] Full backend pytest suite: **129 passed**.
- [x] `git diff --check` and `git diff --cached --check`: PASSED.
- [x] Reviewed the staged changes and confirmed only the intended test file was committed.

### Files changed
- `backend/tests/test_document_api.py`

### Git state
- Committed as `c22197f` — `test: add PDF document preview API tests`.
- Successfully pushed to `origin/master`.
- Verified local `HEAD` and `origin/master` are synchronized at `c22197f`.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.

**Next roadmap task:** Day 41 — Dependency checks and OWASP guidance.

