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

- The Day 22 frontend changes were locally modified and had not yet been committed at the last Git status check.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.
- `docs/PROJECT_STATUS_WEEK_4.md` was created locally and is awaiting its first committed version.
- No claim is made that the Day 22 changes or this status file have been pushed.

---

## Week 4 Progress

| Day    | Topic                                           | Status    |
| ------ | ----------------------------------------------- | --------- |
| Day 22 | Due-date sorting and overdue detection          | Completed |
| Day 23 | Priority levels and upcoming-deadline summaries | Pending   |
| Day 24 | Calendar or weekly deadline view                | Pending   |
| Day 25 | Progress tracking and course summaries          | Pending   |
| Day 26 | In-app reminders and notification states        | Pending   |
| Day 27 | Assignment checklist and estimated workload     | Pending   |
| Day 28 | Date-boundary, overdue, and edge-case testing   | Pending   |

**Next task:** Day 23 — Priority levels and upcoming-deadline summaries.

**Scope reminder:** DeadlineOS remains a single-student MVP. Courses are deferred and must not be introduced without explicit approval.

---

## Week 4 Deliverable

Build a useful academic task manager with deadline intelligence, while preserving the existing React, FastAPI, and SQLite architecture.
