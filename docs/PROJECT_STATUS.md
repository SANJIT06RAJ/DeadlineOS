# PROJECT_STATUS — DeadlineOS

_Last updated: Friday, 6 November 2026_

**Latest development commit:** `5ed6388` — `test: expand assignment service boundary coverage`.

**Latest verified progress:** Week 6 Day 38 — Unit tests for deadline logic and business rules — completed, committed, and pushed.

**Day 38 verification:**
- Added four boundary tests to `backend/tests/test_assignment_service.py`.
- Covered leap-year deadline calculations.
- Covered year-boundary deadline calculations.
- Covered overdue classification for in-progress assignments.
- Covered completed assignments due today.
- Assignment service tests: **14 passed**.
- Full backend pytest suite: **122 passed**.
- `git diff --check`: PASSED.
- Commit `5ed6388` pushed successfully to `origin/master`.

**Week 6 status:** Days 36–38 completed and pushed. Detailed history is recorded in `docs/PROJECT_STATUS_WEEK_6.md`.

**Current roadmap progress:** Week 6 — Day 38 completed.

**Next roadmap task:** Week 6 Day 39 — API integration and frontend workflow tests.

**Git state:** Day 38 application/test commit `5ed6388` was pushed successfully. The overall and Week 6 status documentation was then updated directly on GitHub in separate commits. `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.

**Scope reminder:** DeadlineOS remains a single-student MVP. Authentication and multiple-user accounts remain outside the initial application scope.

Day 28 verification:
- Backend baseline: **71 passed**.
- Added parametrized API tests for yesterday, today, and tomorrow deadlines.