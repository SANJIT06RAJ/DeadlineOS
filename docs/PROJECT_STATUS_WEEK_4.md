# DeadlineOS — Week 4 Project Status

**Week:** 4 — Advanced Functionality
**Period:** 5–11 November 2026

---

## Day 22 — Due-Date Sorting and Overdue Detection

**Status: COMPLETED AND VERIFIED LOCALLY**

### Implementation

- [x] Added due-date sorting to the assignments page.
- [x] Added **Due date: Soonest** sorting.
- [x] Added **Due date: Latest** sorting.
- [x] Kept assignments without due dates at the bottom in both sorting modes.
- [x] Added deadline indicators to assignment cards.
- [x] Displayed `No due date set` for assignments without deadlines.
- [x] Displayed `Completed` for completed assignments, even when their due dates have passed.
- [x] Displayed `Overdue by N day(s)` for overdue assignments.
- [x] Displayed `Due today` for assignments due today.
- [x] Displayed `Due in N day(s)` for future deadlines.
- [x] Added distinct visual styling for overdue, due-today, upcoming, and completed states.
- [x] Corrected the sorting comparator to handle assignments where both due dates are missing.

### Files changed

- `frontend/src/pages/AssignmentsPage.jsx`
- `frontend/src/App.css`

No backend implementation changes were required. The frontend uses the existing API response fields:

- `days_remaining`
- `is_overdue`

### Verification

**Automated checks**

- [x] `npm --prefix frontend run lint` — PASSED.
- [x] `npm --prefix frontend run build` — PASSED; 2,101 modules transformed.
- [x] `git diff --check` — PASSED with no reported whitespace errors.

**Manual browser checks**

- [x] Verified Soonest sorting.
- [x] Verified Latest sorting.
- [x] Verified assignments without due dates remain at the bottom in both sorting modes.
- [x] Verified an overdue assignment displays the correct overdue indicator.
- [x] Verified a completed assignment with a past due date displays `Completed`, not `Overdue`.
- [x] Verified existing assignments continue to display normally.

**Temporary test-data cleanup**

- [x] Created a temporary overdue assignment for testing.
- [x] Created a temporary completed assignment with a past due date.
- [x] Verified both records appeared correctly in the API.
- [x] Deleted both temporary assignments through the existing DELETE API endpoint.
- [x] User confirmed both temporary records were gone.

### Git state

- Day 22 frontend changes and this Week 4 status record were committed and pushed in `0450917` — `feat: add due-date sorting and overdue indicators`.
- Final local Git verification confirmed `master` and `origin/master` synchronized at `0450917`.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.

---

## Week 4 Progress

| Day    | Topic                                           | Status    |
| ------ | ----------------------------------------------- | --------- |
| Day 22 | Due-date sorting and overdue detection          | Completed |
| Day 23 | Priority levels and upcoming-deadline summaries | Completed, committed, and pushed (`cf67812`) |
| Day 24 | Weekly calendar view                           | Completed, committed, and pushed (`6c45ae6`) |
| Day 25 | Assignment progress tracking                    | Completed, committed, and pushed (`4ffc8c4`) |
| Day 26 | In-app reminders and notification states        | Completed, committed, and pushed (`34c8ceb`) |
| Day 27 | Assignment checklist and estimated workload     | Completed, committed, and pushed (`b84a871`) |
| Day 28 | Date-boundary, overdue, and edge-case testing   | Completed locally; pending commit and push |

**Day 28 status:** Completed and verified locally; test changes are pending commit and push.

**Day 23 status:** Implemented, verified, committed as `cf67812`, and pushed to `origin/master`.

**Scope reminder:** DeadlineOS remains a single-student MVP. Courses are deferred and must not be introduced without explicit approval.

---

## Week 4 Deliverable

Build a useful academic task manager with deadline intelligence, while preserving the existing React, FastAPI, and SQLite architecture.

## Day 23 — Priority Levels and Upcoming-Deadline Summaries

**Status: IMPLEMENTED, VERIFIED, COMMITTED, AND PUSHED (`cf67812`).**

### Implementation

- [x] Added assignment priority levels: `low`, `medium`, and `high`.
- [x] Added a SQLite migration that adds the priority column to existing databases with a default of `medium`.
- [x] Updated assignment create, update, and response schemas to support priority.
- [x] Updated assignment API persistence and partial-update handling for priority.
- [x] Added a priority selector to the assignment form.
- [x] Added distinct Low, Medium, and High priority badges to assignment cards.
- [x] Connected dashboard statistics to the existing `GET /assignments/summary` endpoint.
- [x] Replaced dashboard statistic placeholders with live backend values.
- [x] Added upcoming-deadline entries, including formatted due dates and days remaining.
- [x] Added the assignment completion percentage to Work Progress.
- [x] Added dashboard loading, error, and empty states.
- [x] Added CSS for upcoming-deadline entries and dashboard errors.

### Files changed

- `backend/app/database.py`
- `backend/app/main.py`
- `backend/app/schemas.py`
- `frontend/src/App.css`
- `frontend/src/components/assignments/AssignmentForm.jsx`
- `frontend/src/pages/AssignmentsPage.jsx`
- `frontend/src/pages/DashboardPage.jsx`
- `frontend/src/services/api.js`

### Verification

- [x] SQLite migration executed successfully.
- [x] Priority schema check passed; new assignments default to `medium`.
- [x] Backend pytest: **59 passed**.
- [x] Frontend `npm run lint` — PASSED.
- [x] Frontend `npm run build` — PASSED; 2,101 modules transformed.
- [x] Browser-tested priority selection and the displayed priority badge.
- [x] Browser-tested dashboard overview statistics.
- [x] Browser-tested upcoming deadlines and remaining-day labels.
- [x] Browser-tested Work Progress completion percentage.
- [x] Refreshed the dashboard and confirmed data reloaded successfully.
- [x] `git diff --check` — PASSED.

### Git state

- Eight tracked application files were committed as `cf67812` — `feat: add assignment priorities and dashboard summaries`.
- The commit was successfully pushed to `origin/master`.
- The successful push advanced the remote from `7190d21` to `cf67812`.
- The local branch and remote were confirmed synchronized at `7190d21` before the application commit; the push then updated the remote to `cf67812`.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.

---

## Day 24 — Weekly Calendar View (3 November 2026)

**Status: IMPLEMENTED, VERIFIED, COMMITTED, AND PUSHED (`6c45ae6`).**

### Implementation

- [x] Created a weekly calendar page with Monday–Sunday columns.
- [x] Added previous-week and next-week navigation.
- [x] Added a Today shortcut.
- [x] Displayed assignments on their due dates.
- [x] Displayed assignment priority indicators.
- [x] Added visual states for completed, overdue, due-today, and upcoming assignments.
- [x] Added empty-day and no-assignment states.
- [x] Added loading, error, and retry states.
- [x] Added responsive calendar styling.
- [x] Added Calendar navigation to the sidebar and application routes.

### Files changed

- `frontend/src/pages/CalendarPage.jsx`
- `frontend/src/App.jsx`
- `frontend/src/components/layout/Sidebar.jsx`
- `frontend/src/App.css`

### Verification

- [x] Frontend ESLint — PASSED.
- [x] Frontend production build — PASSED; 2,102 modules transformed.
- [x] `git diff --check` — PASSED.
- [x] User manually verified calendar loading, dates, navigation, and page appearance.

### Git state

- Four intended frontend files committed as `6c45ae6` — `feat: add weekly assignment calendar`.
- Successfully pushed to `origin/master`.
- Final Git verification confirmed local `master` and `origin/master` synchronized at `6c45ae6`.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.
- No backend or database files were changed.

---


## Day 25 — Assignment Progress Tracking (3 November 2026)

**Status: IMPLEMENTED, VERIFIED, COMMITTED, AND PUSHED (`4ffc8c4`).**

### Implementation

- [x] Added frontend API helpers for retrieving subtasks.
- [x] Added frontend API helpers for creating, updating, and deleting subtasks.
- [x] Created `AssignmentProgress.jsx` to manage subtasks for individual assignments.
- [x] Added subtask creation and deletion.
- [x] Added completion checkboxes.
- [x] Added automatic progress percentage calculation.
- [x] Added a visual progress bar.
- [x] Added loading, error, empty, and all-completed states.
- [x] Integrated progress tracking into assignment cards.
- [x] Added styling for progress tracking and subtasks.

### Files changed

- `frontend/src/services/api.js`
- `frontend/src/components/assignments/AssignmentProgress.jsx`
- `frontend/src/pages/AssignmentsPage.jsx`
- `frontend/src/App.css`

### Verification evidence

- [x] Frontend ESLint — PASSED.
- [x] Frontend production build — PASSED; 2,103 modules transformed.
- [x] Backend pytest — **59 passed**.
- [x] Browser-tested subtask creation.
- [x] Browser-tested subtask completion and progress recalculation.
- [x] Browser-tested subtask deletion and progress recalculation.
- [x] Refreshed the browser and confirmed subtasks persisted.
- [x] Verified subtasks belonging to different assignments remain separate.
- [x] `git diff --check` — PASSED.

### Git state

- Four intended frontend files committed as `4ffc8c4` — `feat: add assignment progress tracking`.
- Successfully pushed to `origin/master`.
- Final Git verification confirmed local `master` and `origin/master` synchronized at `4ffc8c4`.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.

**Next task:** Day 26 — In-app reminders and notification states.

**Scope reminder:** Course summaries remain deferred. DeadlineOS continues as a single-student MVP.

## Day 26 — In-App Reminders and Notification States (3 November 2026)

**Status: IMPLEMENTED, VERIFIED, COMMITTED, AND PUSHED (`34c8ceb`).**

### Implementation

- [x] Created an in-app notification center using the existing assignment API.
- [x] Integrated the notification bell and active reminder count into the shared header.
- [x] Added overdue, due-today, and upcoming-within-7-days reminder classifications.
- [x] Excluded completed assignments and assignments without due dates.
- [x] Added loading, error, and empty states.
- [x] Added a close control and a View assignments link.
- [x] Added reminder navigation to the selected assignment.
- [x] Added automatic scrolling and temporary highlighting of the selected assignment.

### Files changed

- `frontend/src/components/notifications/NotificationCenter.jsx` (new)
- `frontend/src/components/layout/Header.jsx`
- `frontend/src/pages/AssignmentsPage.jsx`
- `frontend/src/App.css`

### Verification

- [x] `npm --prefix frontend run lint` — PASSED.
- [x] `npm --prefix frontend run build` — PASSED; 2,104 modules transformed.
- [x] Browser-tested upcoming, due-today, and overdue reminder classifications.
- [x] Browser-tested exclusion of completed assignments.
- [x] Browser-tested reminder navigation, automatic scrolling, and temporary highlighting.
- [x] `git diff --check` — PASSED.

No backend or database changes were required.

### Git state

- Four intended frontend files were committed as `34c8ceb` — `feat: add in-app deadline reminders`.
- The commit was successfully pushed to `origin/master`; the remote advanced from `bc674e4` to `34c8ceb`.
- Final Git verification confirmed local `master` and `origin/master` synchronized at `34c8ceb`.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.

**Next task:** Day 27 — Assignment checklist and estimated workload.

## Day 27 — Assignment Checklist and Estimated Workload (3 November 2026)

**Status: IMPLEMENTED, VERIFIED, COMMITTED, AND PUSHED (`b84a871`).**

### Implementation

- [x] Extended the existing subtask database schema with optional `estimated_minutes`.
- [x] Added a safe SQLite migration for existing databases.
- [x] Preserved existing subtasks during migration.
- [x] Updated Pydantic schemas to validate positive integer estimates.
- [x] Updated the subtask creation API to accept optional estimates.
- [x] Updated the subtask update API to edit or clear estimates.
- [x] Added optional workload estimates when creating subtasks.
- [x] Added editable workload estimates for existing subtasks.
- [x] Added total estimated workload calculation.
- [x] Added completed and remaining workload calculations.
- [x] Added workload formatting in minutes and hours.
- [x] Preserved existing checklist progress tracking and subtask functionality.

### Files changed

- `backend/app/database.py`
- `backend/app/main.py`
- `backend/app/schemas.py`
- `backend/tests/test_assignment_api.py`
- `backend/tests/test_database.py`
- `frontend/src/components/assignments/AssignmentProgress.jsx`
- `frontend/src/services/api.js`

### Verification

- [x] Backend pytest: **71 passed, 1 warning**.
- [x] Frontend ESLint — PASSED.
- [x] Frontend production build — PASSED; 2,104 modules transformed.
- [x] Browser-tested subtask creation with an estimate.
- [x] Browser-tested editing an existing estimate.
- [x] Browser-tested workload recalculation after editing estimates.
- [x] Browser-tested completed workload recalculation after completing a subtask.
- [x] Browser-tested estimate persistence after refreshing.
- [x] Browser-tested clearing an estimate.
- [x] Database migration test confirmed existing subtasks survive migration.
- [x] API tests confirmed invalid estimates are rejected.
- [x] `git diff --check` — PASSED.

The pytest warning concerned `.pytest_cache` access being denied on Windows; all 71 tests passed.

### Git state

- Seven intended application files were committed as `b84a871` — `feat: add subtask workload estimates`.
- The commit was successfully pushed to `origin/master`; the remote advanced from `201bd05` to `b84a871`.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.

**Next task:** Day 28 — Date-boundary, overdue, and edge-case testing.

**Scope reminder:** DeadlineOS remains a single-student MVP. Courses are deferred and must not be introduced without explicit approval.

## Day 28 — Date-Boundary, Overdue, and Edge-Case Testing (3 November 2026)

**Status: COMPLETED AND VERIFIED LOCALLY — TEST CHANGES NOT YET COMMITTED OR PUSHED.**

### Implementation
- [x] Reviewed existing deadline and overdue test coverage.
- [x] Added parametrized API tests for yesterday, today, and tomorrow deadlines.
- [x] Verified `days_remaining` returns -1, 0, and 1 for the respective dates.
- [x] Verified overdue classification is true only for the past deadline among these three cases.
- [x] Restored the existing invalid-estimate parametrization decorator after detecting a test setup error.
- [x] Preserved the existing application implementation; no backend application or database code was changed.

### Files changed
- `backend/tests/test_assignment_api.py`

### Verification
- [x] Initial backend baseline: **71 passed**.
- [x] Assignment API tests: **56 passed**.
- [x] Full backend pytest suite: **74 passed**.
- [x] `git diff --check` — PASSED.
- [x] Reviewed the final diff: 31 insertions and no deletions.
- [x] Browser-tested Calendar date display and week navigation.
- [x] Browser-tested overdue styling.
- [x] Browser-tested Notification Center overdue and upcoming reminders.
- [x] Confirmed completed assignments are excluded from overdue notifications.
- [x] User confirmed all Calendar and Notification Center checks behaved correctly.

### Git state
- Day 28 test changes remain local and uncommitted.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.
- No Day 28 commit or push has been performed.

**Next task:** Week 5 — PDF text extraction and malformed-file handling.

