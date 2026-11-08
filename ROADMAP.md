# IT Level-Up Roadmap

## Overview

- **Preparation period:** 15 October – 6 December 2026 (original schedule).
- **Degree start date:** 7 December 2026.
- **Main project:** DeadlineOS — Academic Task & Deadline Intelligence.
- **Current milestone:** DeadlineOS v1.0.0 released; post-release distribution and deployment work begins at Day 50.

DeadlineOS is a system for tracking academic assignments, deadlines, subtasks, progress, and reminders. Its optional AI document extraction suggests assignment details and **requires user confirmation before saving**.

The original eight-week learning schedule is retained as the historical plan. Actual progress is tracked by verified day numbers, not assumed from calendar dates. Days 50 onward extend the roadmap to cover the user's newly approved goals: a downloadable Windows desktop application and a separately deployable online version.

---

## Original Eight-Week Schedule — Days 1–49

### Week 1: 15–21 October — Foundation reset

| Date | Task |
|---|---|
| Thu, 15 Oct | Baseline assessment of Python, SQL, Git, HTTP, APIs, and Linux; identify weak areas and prepare workspace. |
| Fri, 16 Oct | Git/GitHub practice: branches, commits, pull requests, `.gitignore`, and merge conflicts; create repository. |
| Sat, 17 Oct | Python functions, classes, exceptions, type hints, virtual environments, and package management. |
| Sun, 18 Oct | SQL queries, joins, grouping, constraints, primary/foreign keys, and indexes. |
| Mon, 19 Oct | HTTP requests/responses, status codes, JSON, headers, validation, authentication concepts, and Postman. |
| Tue, 20 Oct | Linux/command line, permissions, environment variables, processes, ports, logs, and Bash. |
| Wed, 21 Oct | Review, design architecture, define MVP, create GitHub issues. |

**Deliverable:** Working environment, repository, fundamentals checklist, project design.

### Week 2: 22–28 October — Backend engineering

| Date | Task |
|---|---|
| Thu, 22 Oct | Database schema and relationships; ER diagram. |
| Fri, 23 Oct | FastAPI, configuration, and project structure; running API. |
| Sat, 24 Oct | Database models and schema/migrations; working database. |
| Sun, 25 Oct | CRUD for tasks and courses. |
| Mon, 26 Oct | Validation, filtering, sorting, and pagination. |
| Tue, 27 Oct | Error handling and pytest API tests. |
| Wed, 28 Oct | Bug fixing and API documentation. |

**Deliverable:** Database-backed API with validation and automated tests.

### Week 3: 29 October–4 November — Frontend and integration

| Date | Task |
|---|---|
| Thu, 29 Oct | React/Vite setup and component planning. |
| Fri, 30 Oct | Dashboard and navigation. |
| Sat, 31 Oct | Task creation/editing forms. |
| Sun, 1 Nov | React–FastAPI integration using Axios. |
| Mon, 2 Nov | Assignment search and status filters. |
| Tue, 3 Nov | Loading, empty, success, and error states. |
| Wed, 4 Nov | Integration workflow testing and bug fixing. |

**Deliverable:** Working full-stack task-management MVP.

### Week 4: 5–11 November — Advanced functionality

| Date | Task |
|---|---|
| Thu, 5 Nov | Due-date sorting and overdue detection. |
| Fri, 6 Nov | Priority levels and upcoming-deadline summaries. |
| Sat, 7 Nov | Calendar or weekly deadline view. |
| Sun, 8 Nov | Progress tracking and course summaries. |
| Mon, 9 Nov | In-app reminders and notification states. |
| Tue, 10 Nov | Assignment checklist and estimated workload. |
| Wed, 11 Nov | Date-boundary, overdue, and edge-case testing. |

**Deliverable:** Useful academic task manager with deadline intelligence.

### Week 5: 12–18 November — AI integration and reliability

| Date | Task |
|---|---|
| Thu, 12 Nov | PDF text extraction and malformed-file handling. |
| Fri, 13 Nov | Assignment-document upload and preview workflow. |
| Sat, 14 Nov | Local LLM extraction of title, due date, and requirements. |
| Sun, 15 Nov | Human confirmation before saving extracted data. |
| Mon, 16 Nov | Test missing dates, ambiguity, and incorrect suggestions. |
| Tue, 17 Nov | File validation, error handling, and upload limits. |
| Wed, 18 Nov | Measure extraction success, errors, and response time. |

**Deliverable:** Optional AI importer with human approval. The core application must work when Ollama is offline.

### Week 6: 19–25 November — Testing, cybersecurity, and code quality

| Date | Task |
|---|---|
| Thu, 19 Nov | Authentication, sessions, and password handling. |
| Fri, 20 Nov | User-level access controls. |
| Sat, 21 Nov | Unit tests for deadline logic and business rules. |
| Sun, 22 Nov | API integration and frontend workflow tests. |
| Mon, 23 Nov | Invalid-input, missing-field, upload, and permission tests. |
| Tue, 24 Nov | Dependency checks and OWASP guidance. |
| Wed, 25 Nov | Fix high-priority issues and rerun tests. |

**Deliverable:** Tested release candidate and documented security review.

### Week 7: 26 November–2 December — DevOps and reproducibility

| Date | Task |
|---|---|
| Thu, 26 Nov | Dockerfiles for backend and frontend. |
| Fri, 27 Nov | Environment variables and local database configuration. |
| Sat, 28 Nov | Docker Compose. |
| Sun, 29 Nov | GitHub Actions automated test workflow. |
| Mon, 30 Nov | Linting, formatting, and dependency checks. |
| Tue, 1 Dec | Clean-install and failed-startup recovery testing. |
| Wed, 2 Dec | Release tagging, Git history review, and final bug fixes. |

**Deliverable:** Reproducible application and version 1.0 candidate.

### Week 8: 3–6 December — Portfolio and degree preparation

| Date | Task |
|---|---|
| Thu, 3 Dec | README, architecture notes, and setup instructions. |
| Fri, 4 Dec | Three-to-five-minute demo and screenshots. |
| Sat, 5 Dec | Update CV, GitHub profile, and internship descriptions. |
| Sun, 6 Dec | Review fundamentals, organise degree materials, and rest. |

**Deliverable:** Portfolio-ready project and preparation for degree.

---

## Post-v1.0.0 Roadmap — Day 50 Onward

### Purpose and scheduling

This extension continues from the verified Day 49 release. Days 50–85 are sequential learning and implementation sessions, not fixed calendar dates. Work may continue after the degree starts on 7 December 2026. A day is complete only after implementation (where applicable), verification, and status evidence are recorded.

The two target editions are:

1. **Desktop edition:** A downloadable Windows application for an individual user. Core assignment management must work offline and store data locally.
2. **Online edition:** A hosted web application with registration, authentication, and strict per-user data isolation.

Both editions should reuse the existing React frontend and FastAPI application wherever practical. Avoid maintaining two unrelated implementations.

### Phase 1: Desktop distribution — Days 50–58

**Target:** A Windows installer that lets a user install and run DeadlineOS without separately installing Python, Node.js, Docker, or VS Code.

| Day | Objective |
|---|---|
| 50 | Distribution architecture review: inspect frontend build/startup, FastAPI lifecycle, SQLite persistence, current configuration, and packaging constraints. Document the desktop and online architecture and identify risks. |
| 51 | Desktop shell architecture: evaluate Electron and alternatives; define how the desktop shell starts, monitors, communicates with, and shuts down the backend. |
| 52 | Desktop database and configuration: define a per-user persistent application-data directory, database location, backups, and configuration handling. |
| 53 | Offline reliability: ensure core features work without network access or Ollama; handle missing optional AI service gracefully. |
| 54 | Backend packaging: prototype PyInstaller packaging for FastAPI and verify bundled resources, dependencies, startup, and shutdown. |
| 55 | Desktop integration: connect the desktop shell to the packaged backend and production React frontend; handle startup failures and port/process management safely. |
| 56 | Windows installer: configure electron-builder and an appropriate Windows installer target such as NSIS; define application identity, icons, install paths, and versioning. |
| 57 | Clean-install and upgrade testing: test installation, launch, uninstall behaviour, upgrade, persistent data, and recovery on a clean Windows environment. |
| 58 | Desktop release preparation: document requirements, known limitations, installation steps, and produce a verified downloadable release artifact. |

**Proposed desktop stack (subject to Day 50–51 review):**
- Electron desktop shell.
- Existing React + Vite frontend.
- Existing FastAPI backend.
- PyInstaller for backend packaging.
- electron-builder / NSIS for Windows distribution.
- SQLite for local persistent data.

**Desktop acceptance criteria:**
- Core assignment, subtask, dashboard, and reminder functionality works without an internet connection.
- User data persists outside the installation directory and survives application upgrades.
- Ollama is optional; the application remains usable if Ollama is not installed or running.
- Backend process startup, health, failure, and shutdown are handled safely.
- A clean Windows installation does not require the development toolchain.

### Phase 2: Database architecture for online use — Days 59–63

| Day | Objective |
|---|---|
| 59 | Database architecture review: document the current SQLite/direct-SQL design, identify migration risks, and define compatibility requirements for desktop and online editions. |
| 60 | SQLAlchemy integration: introduce a maintainable database access layer while preserving existing API behaviour and tests. |
| 61 | Alembic migrations: establish versioned schema migrations and test fresh database creation and upgrades from existing SQLite data. |
| 62 | PostgreSQL integration: configure PostgreSQL for the online deployment while retaining SQLite for the desktop edition where appropriate. |
| 63 | Multi-user data model: introduce user identity and assignment ownership, relationships, constraints, and migration strategy. |

**Acceptance criteria:**
- Database changes are versioned and reproducible.
- Existing user data can be migrated safely with backups and validation.
- Desktop SQLite and online PostgreSQL differences are explicit and tested.
- No existing assignment or subtask data is silently discarded.

### Phase 3: Authentication and security — Days 64–70

| Day | Objective |
|---|---|
| 64 | User registration: implement validated account creation and duplicate-account handling. |
| 65 | Login and logout: implement the selected authentication flow and session lifecycle. |
| 66 | Password and session security: use Argon2id for password hashing and secure session/token handling, including expiry and revocation decisions. |
| 67 | Backend authorization: enforce authenticated access and ownership checks on every user-specific resource and operation. |
| 68 | Frontend authentication: add registration, login, logout, session handling, and protected application routes. |
| 69 | User-isolation testing: verify that one account cannot read, modify, delete, or infer another account's data. |
| 70 | Security regression: test authentication failures, authorization boundaries, input validation, session handling, and relevant OWASP risks. |

**Acceptance criteria:**
- Every online assignment and subtask is associated with an authenticated owner.
- Authorization is enforced on the backend, not merely hidden in the frontend.
- Cross-account access tests pass.
- Passwords are never stored in plaintext.
- The desktop single-user mode does not accidentally expose an unauthenticated public service.

### Phase 4: Online deployment — Days 71–79

| Day | Objective |
|---|---|
| 71 | Production configuration: separate development and production settings, secrets, CORS, trusted hosts, and safe defaults. |
| 72 | Production containers: harden Dockerfiles and Compose configuration, health checks, non-root execution where practical, and persistent storage. |
| 73 | Hosting evaluation and deployment: compare genuinely free or low-cost options, limitations, database availability, and deployment requirements; deploy a test environment. |
| 74 | Domain and HTTPS: configure a domain if available, TLS, reverse proxy, and secure transport. |
| 75 | Database backups: automate or document backups, retention, restore procedures, and recovery testing. |
| 76 | Logging and monitoring: implement useful application logs, health monitoring, error visibility, and privacy-conscious operational practices. |
| 77 | Online integration testing: test registration through assignment workflows, persistence, frontend/API integration, and deployment behaviour. |
| 78 | Online security review: review configuration, secrets, dependencies, authorization, database exposure, uploads, and backup security. |
| 79 | Online beta release: publish a controlled beta only after security, recovery, and acceptance checks pass. |

**Acceptance criteria:**
- The online service uses PostgreSQL and secure production configuration.
- HTTPS is enabled before real users or sensitive data are accepted.
- Database backups and a tested restore procedure exist.
- User data isolation is verified in the deployed environment.
- Hosting cost, free-tier limits, and operational risks are documented. Do not assume a free tier is permanent or suitable for production.

**Online AI decision:** The online core must not depend on the user's local Ollama instance. Keep AI extraction optional and disabled or unavailable gracefully until a separately approved online AI architecture, privacy model, and operating cost are established.

### Phase 5: Portfolio and final distribution — Days 80–85

| Day | Objective |
|---|---|
| 80 | Documentation: complete architecture, desktop installation, online deployment, configuration, database migration, backup, and troubleshooting guides. |
| 81 | Edition comparison: document desktop versus online features, offline behaviour, data storage, privacy, and limitations. |
| 82 | Demo preparation: prepare a concise demonstration covering the desktop and online editions, core workflows, and technical architecture. |
| 83 | GitHub portfolio: improve README, screenshots, release notes, repository organisation, and project presentation. |
| 84 | Career preparation: update CV, GitHub profile, and project/internship descriptions with accurate, verifiable achievements. |
| 85 | Final review: review technical fundamentals, project quality, unresolved issues, degree preparation, and the next learning priorities. |

**Final deliverable:** A documented and demonstrated DeadlineOS project with a downloadable Windows desktop edition and a separately deployed online edition, provided both pass their verification and security gates.

---

## Cross-Phase Engineering Rules

- Preserve the existing v1.0.0 release and its Git history.
- Keep `backend/oop_practice.py` untouched and excluded unless explicitly requested.
- Preserve the single-user desktop experience; online multi-user functionality must use proper authentication and server-side ownership enforcement.
- Do not introduce courses unless explicitly approved.
- Keep the core assignment-management experience functional without AI.
- AI-extracted assignment details must always be reviewed and explicitly confirmed before saving.
- Do not expose the current single-user backend publicly as a multi-user service.
- Prefer free and local development tools. Investigate hosting free tiers carefully; do not promise permanent free hosting.
- Make database migrations reversible or provide a tested backup-and-restore path before applying destructive changes.
- Do not commit secrets, local databases, personal data, generated installers, or unrelated files.
- Work incrementally: inspect the current architecture, make a focused change, run relevant tests, review the diff, and record verified results.
- Do not mark a roadmap day complete merely because it was planned or discussed.

---

## Learning and Certification Preferences

Prioritise free resources and genuinely free credentials:

- [freeCodeCamp](https://www.freecodecamp.org/learn/)
- [IBM SkillsBuild](https://skillsbuild.org/)
- [Cisco Networking Academy](https://www.netacad.com/)
- [Microsoft Learn Applied Skills](https://learn.microsoft.com/en-us/credentials/applied-skills/)
- [Fortinet Training Institute](https://training.fortinet.com/)
- [AWS Skill Builder](https://skillbuilder.aws/)

Distinguish **free course completion badges** from **formal certifications with paid exams**. Do not recommend paid exams unless explicitly requested.

---

## Roadmap Rules

- Follow the planned sequence, but never fake progress to match a date.
- Prioritise unfinished tasks and adjust the schedule when necessary.
- Treat Days 1–49 as historical completed progress, subject to the evidence in project status files.
- Continue at Day 50; do not restart the roadmap.
- Check the latest overall and weekly status files, roadmap, and relevant project plan before planning each daily session.
- Keep weekly status files as separate historical records; do not overwrite previous weeks.
- Update `PROJECT_STATUS.md` and the applicable weekly status file only after work is verified and the proposed status changes have been reviewed.
- Current verified implementation progress lives in `docs/PROJECT_STATUS.md` and the applicable weekly status file.
