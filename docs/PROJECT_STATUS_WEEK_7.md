# Week 7 — DevOps and Reproducibility

## Day 43 — Dockerfiles for Backend and Frontend

**Date:** 8 November 2026
**Status:** COMPLETED AND VERIFIED LOCALLY — NOT YET COMMITTED OR PUSHED.

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

- Five intended Docker files remain untracked locally.
- No Day 43 commit or push has been performed.
- `backend/oop_practice.py` remains untracked, untouched, and excluded.
- The Week 7 status file was empty locally before this update.

### Notes

- Frontend and backend currently communicate through the temporary Docker network `deadlineos-day43`.
- Nginx expects the backend hostname `backend`, which will be configured through Docker Compose in Day 45.
- Persistent SQLite configuration and environment variables are deferred to Day 44.

**Next task:** Day 44 — Environment variables and local database configuration.
