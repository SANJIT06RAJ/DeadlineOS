# PROJECT_STATUS — DeadlineOS Week 3

_Last updated: Monday, 2 November 2026_

## 1. Week 3 Overview

**Week:** 29 October – 4 November 2026
**Focus:** Frontend development and full-stack integration.

**Goal:** Build the React frontend for DeadlineOS and prepare it for integration with the existing FastAPI backend.

### Starting checkpoint

- Repository: `SANJIT06RAJ/DeadlineOS`
- Branch: `master`
- Last verified repository HEAD before Week 3 frontend work: `677af6a`
- Local branch was synchronized with `origin/master`.
- Existing backend implementation and tests were preserved.
- Week 2 work is complete. Its history remains in `docs/PROJECT_STATUS_WEEK_2.md`.

## 2. Development Environment

- OS: Windows
- Frontend directory: `frontend/`
- Node.js: `v24.18.0`
- npm: `11.16.0`
- React: `19.3.1`
- Vite: `8.3.5`
- React Router DOM: `7.18.5`
- Axios: `1.21.0`
- Lucide React: `1.65.0`
- ESLint: `10.14.0`

## 3. Week 3 Progress

### Day 15 — React/Vite Setup and Component Planning

**Status: COMPLETED**

Work completed:

- Initialized React + Vite frontend.
- Selected ESLint.
- Installed frontend dependencies:
  - `react-router-dom`
  - `axios`
  - `lucide-react`
- Created modular frontend directories:
  - `src/components/common/`
  - `src/components/assignments/`
  - `src/components/layout/`
  - `src/pages/`
  - `src/services/`
  - `src/hooks/`
- Created layout components:
  - `Sidebar.jsx`
  - `Header.jsx`
  - `AppLayout.jsx`
- Created pages:
  - `DashboardPage.jsx`
  - `AssignmentsPage.jsx`
- Configured React Router in `App.jsx`.
- Replaced the default Vite styling with the initial DeadlineOS interface.
- Added responsive layout styling.

### Frontend Architecture

Current structure:

```text
frontend/
├── public/
├── src/
│   ├── assets/
│   ├── components/
│   │   ├── common/
│   │   ├── assignments/
│   │   │   └── AssignmentForm.jsx
│   │   └── layout/
│   │       ├── AppLayout.jsx
│   │       ├── Header.jsx
│   │       └── Sidebar.jsx
│   ├── hooks/
│   ├── pages/
│   │   ├── AssignmentsPage.jsx
│   │   └── DashboardPage.jsx
│   ├── services/
│   ├── App.jsx
│   ├── App.css
│   ├── index.css
│   └── main.jsx
├── eslint.config.js
├── package.json
└── vite.config.js
```

### Routing

| Route          | Page        |
| -------------- | ----------- |
| `/`            | Dashboard   |
| `/assignments` | Assignments |

### Initial UI

- Dark sidebar navigation.
- DeadlineOS branding.
- Dashboard welcome section.
- Assignment overview statistic placeholders.
- Assignments empty state.
- Responsive layout for narrower screens.

**Important:** Dashboard statistics are placeholders. No real backend data is connected yet.

### Day 16 — Dashboard and Navigation

**Status: COMPLETED**

Work completed:

- Improved the dashboard layout.
- Added dashboard statistic cards.
- Added an Upcoming Deadlines section.
- Added a Work Progress section.
- Added navigation from the dashboard to the assignments page.
- Improved dashboard styling and spacing.
- Verified the dashboard in the browser.

**Verification:**

- `npm run lint`: PASSED.
- `npm run build`: PASSED.

Dashboard statistics and progress remain placeholders. They do not yet use live backend data.

### Day 17 — Assignment Creation Form

**Status: COMPLETED**

Work completed:

- Created `src/components/assignments/AssignmentForm.jsx`.
- Added assignment title input.
- Added optional description field.
- Added optional due-date input.
- Added assignment status selection:
  - `pending`
  - `in_progress`
  - `completed`
- Added title validation:
  - Title is required.
  - Whitespace is trimmed.
  - Maximum length is 200 characters.
- Added status validation.
- Added form error messages.
- Added Create Assignment and Cancel actions.
- Integrated the form into `AssignmentsPage.jsx`.
- Added assignment cards displaying title, description, due date and status.
- Added an empty state when no assignments exist.
- Tested the assignment creation flow in the browser.

**Verification:**

- `npm run lint`: PASSED.
- `npm run build`: PASSED.
- Production build completed successfully with 2,042 modules transformed.

**Current limitation:**

Assignments are currently stored in React component state only. They disappear after refreshing the page because the frontend has not yet been connected to the FastAPI backend.

This is expected before Day 18 integration.

### Day 18 — React–FastAPI Integration

**Status: COMPLETED, VERIFIED, COMMITTED, AND PUSHED**

Implementation:

- [x] Added the Vite `/api` development proxy targeting FastAPI at `http://127.0.0.1:8000`.
- [x] Created `src/services/api.js` with Axios configuration and assignment list/create functions.
- [x] Updated `src/pages/AssignmentsPage.jsx` to load assignments on mount and create them through the backend.
- [x] Added initial loading and request-error feedback.
- [x] Replaced temporary-only React assignment storage with backend-backed assignment retrieval and creation.

Files changed:

- `frontend/vite.config.js`
- `frontend/src/services/api.js` (new)
- `frontend/src/pages/AssignmentsPage.jsx`

Manual integration verification:

- FastAPI started successfully; `GET /health` returned `healthy`.
- Vite frontend loaded successfully.
- Created `Day 18 Integration Test` through the UI.
- Assignment remained visible after browser refresh.
- Direct `GET /assignments` returned the saved record (ID `59`) with its title, description, due date, and `in_progress` status.

Automated checks:

- `npm --prefix frontend run lint`: PASSED.
- `npm --prefix frontend run build`: PASSED; 2,101 modules transformed.
- Backend `python -m pytest -v`: **59 passed**.

No backend source changes were required for this integration.

## 4. Verification Results

### Frontend dependencies

- `npm list --depth=0` completed successfully.
- Required dependencies are installed.
- Initial `npm audit` reported zero vulnerabilities.

### ESLint

Command:

```powershell
npm run lint
```

Latest result: PASSED with no errors.

### Production build

Command:

```powershell
npm run build
```

Latest result: PASSED.

Latest build output:

- 2,042 modules transformed.
- JavaScript bundle: 272.54 kB.
- Gzipped JavaScript: 86.43 kB.
- Build completed successfully.

### Browser verification

User confirmed:

- Dashboard loads.
- Assignments page loads.
- Navigation works.
- Initial layout looks correct.
- Assignment creation form opens.
- Assignment details can be entered and submitted.
- Created assignments appear in the assignments list.

**Known limitation:** Assignment data is not persistent yet and disappears after refreshing the page.

## 5. Existing Backend Checkpoint

The backend remains implemented using FastAPI, SQLite and pytest.

Last recorded backend verification:

- 59 tests passed.
- Latest verified backend code commit: `725ce1b`.
- Existing repository documentation subsequently advanced.
- No backend changes were made during Days 15–17.

The backend API is ready for frontend integration.

## 6. Outstanding Work

- Test the complete frontend/backend workflow and fix integration bugs (Day 21).
- Implement assignment editing, functional dashboard data, and subtask management UI in their planned later tasks.

## 7. Week 3 Roadmap

| Day             | Scheduled task                              | Status                                                                        |
| --------------- | ------------------------------------------- | ----------------------------------------------------------------------------- |
| Day 15 — 29 Oct | React/Vite setup and component planning     | COMPLETED                                                                     |
| Day 16 — 30 Oct | Dashboard and navigation                    | COMPLETED                                                                     |
| Day 17 — 31 Oct | Task creation/editing forms                 | COMPLETED — creation form implemented; editing remains future work            |
| Day 18 — 1 Nov  | React–FastAPI integration using Axios       | COMPLETED — API-backed retrieval/creation and refresh persistence verified   |
| Day 19 — 2 Nov  | Search and status filters                   | COMPLETED — committed and pushed in `c741796`                              |
| Day 20 — 3 Nov  | Loading, empty, success and error states    | COMPLETED — committed and pushed in `7f48e60`; lint/build and listed manual checks passed; noted checks remain unverified |
| Day 21 — 4 Nov  | Integration workflow testing and bug fixing | COMPLETED — manual full-stack workflow checks passed; backend 59 tests, frontend lint, and production build passed |

**Week 3 deliverable:** Working full-stack task-management MVP.

## 8. Git Notes

- Day 18 frontend integration commit: `bf67fb5` — `feat: integrate React assignments with FastAPI`.
- The commit was pushed successfully to `origin/master`.
- Final local verification confirmed `master` and `origin/master` synchronized (`## master...origin/master`).
- `backend/oop_practice.py` remains untracked, untouched, and excluded from all commits.
- Week 2 status history remains unchanged.

---

**Week 3 completed:** Day 21 integration workflow testing and bug fixing is verified. Next roadmap task: Week 4 Day 22 — due-date sorting and overdue detection. Assignment editing, live dashboard data, and subtask UI remain future work.

_End of Week 3 status._


## 9. Day 18 Completion and Next Action

Day 18 integration is complete and manually verified. Assignment creation now persists through FastAPI/SQLite and the frontend reloads the saved assignment after a browser refresh. The backend regression suite remains green (**59 passed**); frontend lint and production build both passed.

**Updated next action after Day 19 completion:** Day 20 — refine loading, empty, success, and error states. Do not add course filters; courses remain deferred from the MVP.



## 10. Day 19 — Assignment Search and Status Filtering (1 November 2026)

**Status: IMPLEMENTED, VERIFIED, COMMITTED, AND PUSHED.** Completed ahead of the scheduled 2 November slot; included in `c741796`.

### Implementation

- Added assignment search by title and description.
- Added status filtering: All, Pending, In Progress, and Completed.
- Search and status filters work together.
- Added a no-matching-assignments state with a Clear filters action.
- Used useMemo to derive filtered assignments.
- Corrected the assignment CSS section so desktop styles are outside the existing mobile media query; retained responsive styling.
- Reused the existing API-backed assignment list; no backend changes were required.
- Course filtering was not added; courses remain deferred from the MVP.

### Files changed

- `frontend/src/pages/AssignmentsPage.jsx`
- `frontend/src/App.css`

### Verification

- Manual checks passed for title search, description search, each status filter, combined filters, no-results state, clearing filters, and assignment creation.
- `npm run lint` — PASSED.
- `npm run build` — PASSED; 2,101 modules transformed.
- `git diff --check` — PASSED.

### Git state

- Day 19 source changes were committed and pushed in `c741796`.
- The working tree also contains the existing untracked `backend/oop_practice.py`, which remains untouched and excluded.

**Next:** Day 21 — integration workflow testing and bug fixing.



## 11. Day 20 — Loading, Success, and Error States (2 November 2026)

**Status: IMPLEMENTED, VERIFIED, COMMITTED, AND PUSHED.** Completed ahead of the scheduled 3 November slot; frontend changes were committed and pushed in `7f48e60`. 

### Implementation

- Added a loading indicator while assignments are retrieved.
- Added a load-error state with retry handling.
- Separated assignment-loading errors from assignment-creation errors.
- Added a dismissible success notification after assignment creation.
- Added submission loading feedback and disabled form controls while submitting.
- Kept the creation modal open and preserved entered values after a failed request; displayed the error inside the modal.
- Added a mounted guard and retry handling for assignment retrieval.

### Files changed

- `frontend/src/pages/AssignmentsPage.jsx`
- `frontend/src/components/assignments/AssignmentForm.jsx`
- `frontend/src/App.css`

### Verification

- `npm --prefix frontend run lint` — PASSED.
- `npm --prefix frontend run build` — PASSED; 2,101 modules transformed.
- `git diff --check` — PASSED.
- Manual checks passed for assignment loading/display, creation success, backend-down load error, retry recovery, failed creation feedback, form-data preservation, and successful retry after backend recovery.
- Empty-state behaviour was not explicitly retested during this session.
- Submission loading was implemented but its transient visual state was too brief to verify manually.
- Rapid double-submission prevention was not deliberately tested.

### Git state

- Day 20 frontend changes were committed and pushed in `7f48e60` — `feat: improve assignment loading and error states`.
- Final `git status -sb` confirmed `## master...origin/master`; `git log` confirmed `7f48e60` at `HEAD`, `origin/master`, and `origin/HEAD`.
- `backend/oop_practice.py` remains untracked, untouched, and excluded.
- No backend files were changed during Day 20.

**Next:** Day 21 — integration workflow testing and bug fixing.


## 12. Day 21 — Integration Workflow Testing and Bug Fixing (2 November 2026)

**Status: COMPLETED — full-stack integration workflow verified.**

### Manual integration checks

- [x] Started FastAPI successfully; `GET /health` returned `healthy`.
- [x] Confirmed the API returned the existing assignment records and the frontend displayed all seven records present at the time of the check.
- [x] Created an assignment through the frontend.
- [x] Refreshed the browser and confirmed the new assignment remained visible.
- [x] Verified search by assignment title and description.
- [x] Verified All, Pending, In Progress, and Completed status filters.
- [x] Verified combined search and status filtering.
- [x] Verified the no-results message.
- [x] Stopped FastAPI and confirmed the frontend displayed an assignment-loading error.
- [x] Restarted FastAPI and confirmed the retry action reloaded assignments without a browser refresh.
- [x] Stopped FastAPI and submitted an assignment; confirmed an error appeared and the form remained open with entered values preserved.
- [x] Restarted FastAPI and successfully retried the submission using the preserved form values.

### Automated checks

- Backend `python -m pytest -v`: **59 passed**.
- `npm --prefix frontend run lint`: PASSED with no ESLint errors.
- `npm --prefix frontend run build`: PASSED; 2,101 modules transformed.
- `git diff --check`: PASSED.

### Verification limitations

- The true empty-assignment state was not separately tested; the no-results state was tested.
- The transient submission-loading visual state was not separately confirmed.
- Rapid double-submission prevention was not deliberately tested.

These are verification limitations, not confirmed defects. No application source changes were required during Day 21.

### Git state

- Before the documentation updates, local `master` was synchronized with `origin/master` at `9828898`.
- No tracked application files were modified during Day 21.
- `backend/oop_practice.py` remains untracked, untouched, and excluded.
- Day 21 status documentation was committed directly to `master` in the documentation updates; the local working copy still needs to pull those commits.

### Week 3 outcome

**Week 3 deliverable achieved:** the DeadlineOS frontend communicates with the FastAPI backend, creates and retrieves persistent assignments, supports search and status filtering, and handles the tested loading, request-error, and recovery workflows.

Assignment editing, live dashboard statistics, and subtask UI remain future work and are outside the completed Week 3 scope.

**Next roadmap task:** Week 4 — Advanced Functionality, beginning with due-date sorting and overdue detection.
