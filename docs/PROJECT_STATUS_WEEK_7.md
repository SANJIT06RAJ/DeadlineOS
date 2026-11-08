# Week 7 — DevOps and Reproducibility

## Day 43 — Dockerfiles for Backend and Frontend

**Date:** 8 November 2026
**Status:** COMPLETED, VERIFIED, COMMITTED, AND PUSHED (`5f26c7c`).

### Implementation

- [x] Created `backend/Dockerfile` using Python 3.13 slim.
- [x] Created `frontend/Dockerfile` using a multi-stage Node.js and Nginx build.
- [x] Created `frontend/nginx.conf` for React routing and FastAPI reverse proxying.
- [x] Created `backend/.dockerignore`.
- [x] Created `frontend/.dockerignore`.

### Docker images

- `deadlineos-backend:day43`
- `deadlineos-frontend:day43`

### Verification

- [x] Backend image built successfully.
- [x] Frontend image built successfully.
- [x] Backend container started successfully.
- [x] Backend `/health` returned `healthy`.
- [x] Frontend served successfully with HTTP 200.
- [x] Nginx successfully proxied `/api/health` to FastAPI.
- [x] Rebuilt both images after adding `.dockerignore` files.
- [x] Recreated containers using the rebuilt images.
- [x] Repeated frontend and backend proxy tests successfully.
- [x] Backend Docker build context reduced to 930 bytes.
- [x] Frontend Docker build context reduced to 2.17 KB.
- [x] `git diff --check` passed.

### Files created

- `backend/Dockerfile`
- `backend/.dockerignore`
- `frontend/Dockerfile`
- `frontend/.dockerignore`
- `frontend/nginx.conf`

### Git state

- The five Docker implementation files are included in the Day 43 changes.
- `docs/PROJECT_STATUS_WEEK_7.md` records the verified Day 43 progress.
- `backend/oop_practice.py` remains local-only, untouched, and excluded from the changes.
- The five Docker implementation files and this Week 7 record were committed as `5f26c7c` — `build: add Docker support for frontend and backend` — and pushed to `origin/master`.
- The Week 7 Git-state wording was corrected in commit `478df4a` and pushed to `origin/master`.

### Notes

- Frontend and backend currently communicate through the temporary Docker network `deadlineos-day43`.
- Nginx expects the backend hostname `backend`, which will be configured through Docker Compose in Day 45.
- Persistent SQLite configuration and environment variables are deferred to Day 44.

**Next task:** Day 44 — Environment variables and local database configuration.

## Day 44 — Environment Variables and Persistent SQLite Configuration

**Date:** 8 November 2026

**Status: IMPLEMENTED, VERIFIED, COMMITTED, AND PUSHED (`c8f0c31`).**

### Implementation

- [x] Created `backend/app/config.py` for centralized application configuration.
- [x] Added configurable `DATABASE_PATH` with the existing SQLite location as its default.
- [x] Added configurable `OLLAMA_URL` and `OLLAMA_MODEL` with existing defaults preserved.
- [x] Updated `backend/app/database.py` to import `DATABASE_PATH` from the centralized configuration.
- [x] Updated `backend/app/services/ai_extraction_service.py` to import Ollama settings from centralized configuration.
- [x] Added `backend/.env.example` documenting the environment variables.
- [x] Preserved the existing database schema and AI extraction behaviour.

### Verification

- [x] Database test suite: **8 passed**.
- [x] Full backend pytest suite: **132 passed**.
- [x] `git diff --check` passed.
- [x] Backend Docker image built successfully.
- [x] Backend container started with `DATABASE_PATH=/data/deadlineos.db`.
- [x] Backend `/health` returned `healthy`.
- [x] Verified the `assignments` and `subtasks` tables exist.
- [x] Verified the `deadlineos-data` named volume is mounted at `/data`.
- [x] Removed and recreated the backend container using the same volume.
- [x] Verified the database tables remained present after container recreation.
- [x] Backend `/health` returned `healthy` after recreation.

### Files changed

- `backend/app/config.py` (new)
- `backend/app/database.py`
- `backend/app/services/ai_extraction_service.py`
- `backend/.env.example` (new)

### Docker verification details

- Image: `deadlineos-backend`
- Container: `deadlineos-api`
- Host port: `8000`
- Container port: `8000`
- Named volume: `deadlineos-data`
- Database path inside container: `/data/deadlineos.db`

### Git state

- The four intended application files were committed as `c8f0c31` — `feat: centralize environment configuration`.
- The commit was successfully pushed to `origin/master`.
- The push advanced GitHub `master` from `4868a33` to `c8f0c31`.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.

### Notes

- `.env.example` is a configuration template; it is not automatically loaded by Python.
- Environment variables were explicitly passed when starting the Docker container.
- Docker Compose integration remains planned for Day 45.

**Next task:** Day 45 — Docker Compose integration.


## Day 45 — Docker Compose Integration

**Date:** 8 November 2026

**Status: COMPLETED, VERIFIED, COMMITTED, AND PUSHED (`ce71cbd`).**

### Implementation

- [x] Created the root-level `docker-compose.yml`.
- [x] Configured the FastAPI backend service using `backend/Dockerfile`.
- [x] Configured the Nginx frontend service using `frontend/Dockerfile`.
- [x] Configured the frontend host mapping as `5173:80`.
- [x] Kept the backend on the internal Compose network; Nginx forwards `/api/` requests to the `backend` service.
- [x] Reused the existing external named volume `deadlineos-data`.
- [x] Configured SQLite at `/data/deadlineos.db`.
- [x] Configured Ollama access through `host.docker.internal:11434`, with `qwen2.5:3b` as the default model.
- [x] Kept the existing architecture and application code unchanged.

### Verification

- [x] `docker compose config` completed successfully.
- [x] Backend Docker image built successfully.
- [x] Frontend Docker image built successfully.
- [x] `docker compose up -d` started both services successfully.
- [x] `docker compose ps` confirmed both services were running.
- [x] Frontend production HTML returned HTTP **200 OK** through Nginx.
- [x] Inspected the frontend container and confirmed the compiled production HTML and hashed assets are present.
- [x] Nginx reverse proxy request to `/api/health` returned `healthy`.
- [x] Retrieved **27 existing assignments** through the Compose frontend/API route.
- [x] Restarted both Compose services and retrieved all **27 assignments** again.
- [x] Confirmed the existing `deadlineos-data` volume is mounted at `/data`.
- [x] Confirmed the backend container can reach host Ollama; `/api/tags` returned HTTP **200**.
- [x] Confirmed the configured `qwen2.5:3b` model is available.
- [x] Reviewed backend and frontend logs; startup succeeded and no application errors were observed.
- [x] `git diff --check` passed.

### Files created

- `docker-compose.yml` (new)

### Git state

- Committed `docker-compose.yml` as `ce71cbd` — `feat: add Docker Compose configuration` — and successfully pushed it to `origin/master`.
- Final Git verification confirmed local `master` and `origin/master` synchronized at `ce71cbd`.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.
- The pre-existing `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.
- The previous manually started `deadlineos-api` container was stopped, not removed.
- The existing `deadlineos-data` volume was reused and preserved.

### Notes

- The Compose volume is declared external. On another machine, create it before starting the application with `docker volume create deadlineos-data`.
- The backend is intentionally not published on a host port; access it through the frontend's Nginx `/api/` proxy.
- Ollama remains installed on the host machine and is not run as a Compose service.

**Next task:** Check `ROADMAP.md` for the exact Day 46 objective before planning the next session.

## Day 46 — GitHub Actions Automated Test Workflow

**Date:** 8 November 2026

**Status: COMPLETED, VERIFIED, COMMITTED, AND PUSHED (`312733d`).**

### Implementation

- [x] Created `.github/workflows/ci.yml`.
- [x] Configured the workflow to run on pushes and pull requests targeting `master`.
- [x] Added a backend job using Python 3.13.
- [x] Added backend dependency installation and automated pytest execution.
- [x] Added a frontend job using Node.js 24.
- [x] Added frontend dependency installation using `npm ci`.
- [x] Added Vitest, ESLint, and production-build checks.
- [x] Added `argon2-cffi==25.1.0` to `backend/requirements.txt` after the initial CI run exposed the missing dependency.

### Verification

- [x] Initial CI run identified the missing Argon2 dependency.
- [x] Corrected the workflow database environment configuration.
- [x] Added the missing Argon2 dependency.
- [x] GitHub Actions Run #3 completed successfully: https://github.com/SANJIT06RAJ/DeadlineOS/actions/runs/42468602211
- [x] Backend pytest suite: **132 passed**.
- [x] Frontend Vitest suite: **13 passed across 2 test files**.
- [x] Frontend ESLint — PASSED.
- [x] Frontend production build — PASSED.
- [x] Both GitHub Actions jobs reported success.

### Files changed

- `.github/workflows/ci.yml` (new)
- `backend/requirements.txt`

### Git state

- Workflow created in commit `b709f7b`.
- Workflow database-path correction committed as `3bf85a3`.
- Argon2 dependency correction committed as `312733d`.
- All commits successfully pushed to `origin/master`.
- Local `master` synchronized with `origin/master` at `312733d`.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.

### Notes

- GitHub Actions reported Node.js 20 deprecation warnings for the current action versions.
- The `ubuntu-latest` runner migration notice is informational.
- These notices did not affect the successful CI result.

**Next task:** Day 47 — Linting, formatting, and dependency checks.

## Day 47 — Linting, Formatting, and Dependency Checks

**Date:** 8 November 2026

**Status: COMPLETED, VERIFIED, COMMITTED, AND PUSHED.**

### Implementation

- [x] Reviewed the existing Python and frontend quality-check configuration.
- [x] Added root-level `pyproject.toml` with Ruff configuration: line length 88 and Python 3.13 target.
- [x] Excluded the pre-existing local-only `backend/oop_practice.py` from Ruff.
- [x] Scoped Ruff's `B008` exception to `backend/app/main.py` for FastAPI parameter declarations.
- [x] Fixed lint findings and applied Ruff formatting to the backend Python files.
- [x] Kept Ruff installed in the local backend virtual environment; it was not added to the runtime requirements or CI workflow.

### Verification

- [x] `python -m ruff check backend`: all checks passed.
- [x] `python -m ruff format --check backend`: **20 files already formatted**.
- [x] `python -m pip check`: no broken requirements found.
- [x] `python -m pip_audit -r backend/requirements.txt`: no known vulnerabilities found.
- [x] Backend pytest suite: **132 passed**.
- [x] Frontend ESLint: passed.
- [x] Frontend Vitest suite: **13 passed across 2 test files**.
- [x] Frontend production build: passed with Vite 8.3.5.
- [x] `npm --prefix frontend audit --omit=dev`: **0 vulnerabilities**.
- [x] `git diff --check` and `git diff --cached --check`: passed.
- [x] Reviewed the changed Python files and staged diff before committing.

### Files changed

- Added `pyproject.toml`.
- Applied lint and formatting fixes to 17 existing backend Python files.

### Git state

- Committed as `06492bc` — `chore: add Python linting and formatting checks`.
- Successfully pushed to `origin/master` on 8 November 2026.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.

### Notes

- Pytest completed with **132 passed** and one non-blocking Windows cache-permission warning when creating `.pytest_cache`.
- Ruff is configured in the repository, but the Ruff package itself is currently installed only in the local virtual environment. A future development-dependency setup can make installation reproducible.

**Next task:** Day 48 — Clean-install and failed-startup recovery testing.

