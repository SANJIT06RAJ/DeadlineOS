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

- The two security lab files are included in the Day 36 changes.
- `docs/PROJECT_STATUS_WEEK_6.md` records the Week 6 progress.
- `backend/oop_practice.py` remains untouched and intentionally excluded.
- Commit and push status will be verified after the changes are committed.

- The two security lab files are untracked and have not been committed.
- `docs/PROJECT_STATUS_WEEK_6.md` is a new weekly status file.
- `backend/oop_practice.py` remains untouched and intentionally excluded.
- Git commit and push status must be verified after the status updates are reviewed.

**Next roadmap task:** Day 37 — User-level access controls. Keep the exercise within the existing single-student MVP scope unless a scope change is explicitly approved.
