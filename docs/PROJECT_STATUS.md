# PROJECT_STATUS — DeadlineOS

_Last updated: Thursday, 15 October 2026_

## Environment

- Windows PC
- Project directory: `C:\Users\kefztv\Desktop\DeadlineOS`
- Git: `2.55.0.windows.2`
- Python: `3.13.0`
- Node.js: `v24.18.0`
- npm: `11.16.0`
- VS Code: `1.141.2`

## Completed Work

- [x] Checked the development tools.
- [x] Created the correct Git repository at `C:\Users\kefztv\Desktop\DeadlineOS`.
- [x] Removed an accidentally created `.git` folder from the Desktop root.
- [x] Created `README.md`, `.gitignore`, and `docs/PROJECT_PLAN.md`.
- [x] Created `backend/app`, `backend/tests`, and `frontend` folders.
- [x] Created project virtual environment at `backend\.venv`.
- [x] Installed FastAPI and `uvicorn[standard]` in the virtual environment.
- [x] Created `backend/app/__init__.py`.
- [x] Created `backend/app/main.py` containing a FastAPI app and `GET /` and `GET /health` endpoints.
- [x] Started the backend at `http://127.0.0.1:8000`.
- [x] Verified `/health` returns `{"status":"healthy"}`.
- [x] Created initial Git commit `0b0d2f8`.
- [x] Created backend commit `a704806`, message `feat: add initial FastAPI backend`.
- [x] Confirmed `git status` shows a clean working tree.
- [x] Reviewed basic pip, FastAPI, REST API, and foreign-key concepts.

## Current Database Design

Recorded in `docs/PROJECT_PLAN.md`:

- **Assignment:** `id`, `title`, optional `description`, `due_date`, `status` (`pending`, `in_progress`, `completed`), `created_at`.
- **Subtask:** `id`, `assignment_id` (foreign key), `title`, `is_completed`.
- One assignment can have many subtasks.

## Known Project Structure

```text
DeadlineOS/
├── .gitignore
├── README.md
├── docs/
│   └── PROJECT_PLAN.md
├── backend/
│   ├── .venv/
│   ├── app/
│   │   ├── __init__.py
│   │   └── main.py
│   └── tests/
└── frontend/
```

## Current Progress

- Day 1 foundation setup is complete.
- Day 2 backend/database foundations are in progress.
- `backend/requirements.txt` has **not** been verified as created.
- SQLite connection, models, table creation, and pytest tests are **not** assumed to be implemented.
- Last confirmed command output:

  ```text
  On branch master
  nothing to commit, working tree clean
  ```

## Unfinished Tasks

- [ ] `backend/requirements.txt`
- [ ] SQLite connection
- [ ] Database models and table creation
- [ ] pytest tests
- [ ] Remaining Week 1 items (see `ROADMAP.md`); schedule to be adjusted based on verified progress

## Exact Next Step

Create `backend/requirements.txt` with:

```text
fastapi
uvicorn[standard]
```

Then run these commands from `C:\Users\kefztv\Desktop\DeadlineOS`:

```powershell
backend\.venv\Scripts\python.exe -m pip install -r backend\requirements.txt
backend\.venv\Scripts\python.exe -m pip show fastapi uvicorn
```

Wait for the terminal output to be shared. Verify the dependencies before proceeding to the SQLite connection.

## Useful Command to Start the Backend

```powershell
backend\.venv\Scripts\python.exe -m uvicorn app.main:app --app-dir backend --reload
```

Useful URLs:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/health
- http://127.0.0.1:8000/docs

## Operating Rules

- Read both files before continuing the roadmap.
- Follow the date-based roadmap, but never fake progress to match a date.
- Prioritise unfinished tasks and adjust the schedule when necessary.
- Work one step at a time; keep explanations concise.
- Give exact paths, filenames, commands, and complete code where necessary.
- Do not mark a task complete until confirmed or verified by output.
- Debug shared errors before moving forward.
- Avoid unnecessary rewrites, overengineering, and paid services.
- At the end of each session, provide updated `PROJECT_STATUS.md` content.
- Keep `ROADMAP.md` stable unless intentionally revised.
