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
