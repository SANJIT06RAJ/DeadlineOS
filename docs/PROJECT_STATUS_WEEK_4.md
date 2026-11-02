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
| Day 23 | Priority levels and upcoming-deadline summaries | Completed locally; uncommitted |
| Day 24 | Calendar or weekly deadline view                | Pending   |
| Day 25 | Progress tracking and course summaries          | Pending   |
| Day 26 | In-app reminders and notification states        | Pending   |
| Day 27 | Assignment checklist and estimated workload     | Pending   |
| Day 28 | Date-boundary, overdue, and edge-case testing   | Pending   |

**Next task:** Day 24 — Calendar or weekly deadline view.

**Day 23 status:** Implemented and verified locally. Eight tracked application files are modified and have not yet been committed or pushed.

**Scope reminder:** DeadlineOS remains a single-student MVP. Courses are deferred and must not be introduced without explicit approval.

---

## Week 4 Deliverable

Build a useful academic task manager with deadline intelligence, while preserving the existing React, FastAPI, and SQLite architecture.

## Day 23 — Priority Levels and Upcoming-Deadline Summaries

**Status: IMPLEMENTED AND VERIFIED LOCALLY — NOT YET COMMITTED OR PUSHED.**

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

- Eight tracked application files are modified locally.
- The reported local status showed `master...origin/master` before these documentation commits.
- Day 23 application changes remain local and have not been committed or pushed.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.

---

