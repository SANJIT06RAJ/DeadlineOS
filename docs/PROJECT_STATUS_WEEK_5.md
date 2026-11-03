# Week 5 — AI Integration and Reliability

## Day 29 — PDF Text Extraction and Malformed-File Handling

**Status: COMPLETED, VERIFIED, COMMITTED, AND PUSHED (`0832a21`).**

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

- Day 29 changes were committed as `0832a21` — `feat: add PDF text extraction service`.
- The commit was successfully pushed to `origin/master`.
- Final Git verification confirmed local `master` and `origin/master` synchronized at `0832a21`.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.
- This Week 5 history record was committed and pushed with the Day 29 implementation.

### Next task

**Day 30 — Assignment-document upload and preview workflow.**

Continue with the existing React + Vite frontend and FastAPI backend architecture. Preserve the single-student MVP scope and require user confirmation before saving any AI-extracted assignment details.


## Day 30 — Assignment-Document Upload and Preview Workflow

**Status: COMPLETED, VERIFIED, COMMITTED, AND PUSHED (`c55a181`).**

### Objectives

- [x] Allow users to upload PDF assignment documents.
- [x] Validate uploaded files and enforce a 10 MB size limit.
- [x] Extract PDF text using the existing PDF extraction service.
- [x] Display extracted text and character count in the frontend.
- [x] Keep document preview separate from assignment creation and saving.

### Implementation

- [x] Installed `python-multipart==0.0.33` in the backend virtual environment.
- [x] Added `python-multipart==0.0.33` to `backend/requirements.txt`.
- [x] Added `POST /documents/preview` to `backend/app/main.py`.
- [x] Added PDF filename, empty-file, file-size, and PDF-signature validation.
- [x] Reused `extract_pdf_text()` from `backend/app/services/pdf_service.py`.
- [x] Added `frontend/src/components/assignments/DocumentUploader.jsx`.
- [x] Added `previewDocument()` to `frontend/src/services/api.js`.
- [x] Integrated the uploader into `frontend/src/pages/AssignmentsPage.jsx`.
- [x] Added responsive uploader styling to `frontend/src/App.css`.
- [x] Kept the existing assignment creation workflow unchanged.
- [x] Confirmed that previewing a document does not create or save an assignment.

### Files changed

- `backend/app/main.py`
- `backend/requirements.txt`
- `backend/tests/test_pdf_upload.py` (new)
- `frontend/src/App.css`
- `frontend/src/pages/AssignmentsPage.jsx`
- `frontend/src/services/api.js`
- `frontend/src/components/assignments/DocumentUploader.jsx` (new)

### Testing and verification

- [x] Backend upload test suite: **7 passed**.
- [x] Full backend test suite: **86 passed**.
- [x] Frontend ESLint: **PASSED**.
- [x] Frontend production build: **PASSED**.
- [x] Python compilation check for `backend/app/main.py`: **PASSED**.
- [x] Manual browser test of PDF upload and preview: **PASSED**.

### Known limitations

- Scanned/image-only PDFs are not supported because OCR has not been implemented.
- AI extraction of assignment details is not implemented yet.
- Extracted text is preview-only; no assignment is automatically created or saved.
- The future AI workflow must allow the user to review and confirm extracted details before saving.

### Git state

- Seven intended application files were committed as `c55a181` — `feat: add PDF assignment document preview`.
- The application commit was successfully pushed to `origin/master`.
- Final Git verification confirmed local `master` and `origin/master` synchronized at `c55a181911d27190669d30d7f8b4d364c122ddb5`.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.

### Next task

**Day 31 — Local LLM extraction of assignment title, due date, and requirements.**

Build on the PDF preview workflow using the existing local AI setup. Extract suggested assignment details without saving them automatically; user confirmation will be handled in the following roadmap task.
