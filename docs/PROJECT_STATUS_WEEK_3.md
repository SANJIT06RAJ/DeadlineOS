# PROJECT_STATUS — DeadlineOS Week 3

_Last updated: Saturday, 31 October 2026_

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

- Connect the frontend to the existing backend using Axios.
- Replace temporary React assignment state with API-backed data.
- Implement assignment editing and persistent assignment management.
- Build functional dashboard data using existing backend endpoints.
- Implement subtask management UI.
- Add loading, empty, success and error states.
- Test the complete frontend/backend workflow.

## 7. Week 3 Roadmap

| Day             | Scheduled task                              | Status                                                                        |
| --------------- | ------------------------------------------- | ----------------------------------------------------------------------------- |
| Day 15 — 29 Oct | React/Vite setup and component planning     | COMPLETED                                                                     |
| Day 16 — 30 Oct | Dashboard and navigation                    | COMPLETED                                                                     |
| Day 17 — 31 Oct | Task creation/editing forms                 | COMPLETED — creation form implemented; editing remains future work            |
| Day 18 — 1 Nov  | React–FastAPI integration using Axios       | NEXT                                                                          |
| Day 19 — 2 Nov  | Search and status filters                   | PENDING — course filters deferred because courses are outside the current MVP |
| Day 20 — 3 Nov  | Loading, empty, success and error states    | PENDING                                                                       |
| Day 21 — 4 Nov  | Integration workflow testing and bug fixing | PENDING                                                                       |

**Week 3 deliverable:** Working full-stack task-management MVP.

## 8. Git Notes

- Preserve `backend/oop_practice.py` as untracked and untouched unless explicitly instructed otherwise.
- Review all frontend changes before staging.
- Do not stage unrelated files.
- Check Git status and the generated `frontend/dist/` handling before committing.
- Week 2 status history must remain unchanged.
- Latest verified committed repository checkpoint before staging the current frontend work: `9ee7859`.
- The frontend files and this Week 3 status file were untracked at the latest local Git check and still require review before staging and committing.

---

**Next action:** Day 18 — Connect React to FastAPI using Axios and verify persistent assignment creation and retrieval.

_End of Week 3 status._
