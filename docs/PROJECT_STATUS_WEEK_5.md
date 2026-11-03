# Week 5 — AI Integration and Reliability

## Day 29 — PDF Text Extraction and Malformed-File Handling

**Status: COMPLETED AND TESTED LOCALLY — CHANGES NOT YET COMMITTED OR PUSHED.**

### Objectives

- [x] Introduce PDF text extraction using a free Python library.
- [x] Handle empty and malformed PDF files.
- [x] Handle encrypted PDF files.
- [x] Detect PDFs without extractable text.
- [x] Add automated tests for PDF extraction and error handling.

### Implementation

- [x] Installed `pypdf==6.21.4` inside the backend virtual environment.
- [x] Added `pypdf==6.21.4` to `backend/requirements.txt`.
- [x] Created `backend/app/services/pdf_service.py`.
- [x] Implemented `extract_pdf_text(pdf_bytes)` to extract text page by page.
- [x] Added validation for empty PDF bytes.
- [x] Added handling for malformed and unreadable PDFs.
- [x] Added rejection of encrypted PDFs.
- [x] Added detection of PDFs without extractable text.
- [x] Kept PDF extraction independent of assignment CRUD and database operations.

### Files changed

- `backend/requirements.txt`
- `backend/app/services/pdf_service.py` (new)
- `backend/tests/test_pdf_service.py` (new)

### Testing and verification

- [x] Verified pypdf installation and version: `6.21.4`.
- [x] Added five automated PDF extraction tests.
- [x] Valid PDF text extraction test — PASSED.
- [x] Empty PDF rejection test — PASSED.
- [x] Malformed PDF rejection test — PASSED.
- [x] PDF without extractable text test — PASSED.
- [x] Encrypted PDF rejection test — PASSED.
- [x] Dedicated PDF test suite: **5 passed**.
- [x] Full backend pytest suite: **79 passed**.
- [x] `git diff --check` — PASSED.
- [x] Reviewed implementation and test files.

### Known limitations

- Scanned/image-only PDFs are not supported because OCR has not been implemented.
- PDF extraction is currently a standalone backend service.
- No assignment data is automatically created or saved.
- AI extraction and user confirmation will be handled in later roadmap tasks.

### Git status

- Changes have been verified locally but have not yet been committed or pushed.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.
- `docs/PROJECT_STATUS_WEEK_5.md` is being initialized as the Week 5 history record.

### Next task

**Day 30 — Assignment-document upload and preview workflow.**

Continue with the existing React + Vite frontend and FastAPI backend architecture. Preserve the single-student MVP scope and require user confirmation before saving any AI-extracted assignment details.
