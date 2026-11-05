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


## Day 31 — Local LLM Assignment-Detail Extraction

**Status: COMPLETED, VERIFIED, COMMITTED, AND PUSHED (`7f1f507`).**

### Objectives

- [x] Connect the existing PDF text-extraction workflow to a local LLM.
- [x] Extract assignment titles, due dates, and requirements.
- [x] Validate structured AI responses.
- [x] Handle missing information and Ollama errors.
- [x] Ensure extraction does not automatically save assignments.

### Implementation

- [x] Benchmarked local Ollama models.
- [x] Selected `qwen2.5:3b` as the initial extraction model.
- [x] Created `backend/app/services/ai_extraction_service.py`.
- [x] Added the `AssignmentExtraction` Pydantic model.
- [x] Implemented structured JSON extraction through Ollama.
- [x] Added configurable Ollama URL and model settings.
- [x] Added `AssignmentExtractionRequest` to `backend/app/schemas.py`.
- [x] Added `POST /documents/extract`.
- [x] Added validation and error handling for invalid model responses and unavailable Ollama.
- [x] Kept extraction separate from assignment creation and database operations.

### Files changed

- `backend/app/main.py`
- `backend/app/schemas.py`
- `backend/app/services/ai_extraction_service.py` (new)
- `backend/tests/test_ai_extraction.py` (new)

### Testing and verification

- [x] Local Ollama API test — PASSED.
- [x] Direct Python-to-Ollama extraction test — PASSED.
- [x] AI service tests: **7 passed**.
- [x] AI endpoint tests: **5 passed**.
- [x] Full backend pytest suite: **98 passed**.
- [x] Full backend suite without pytest cache: **98 passed, no warnings**.
- [x] Python compilation checks — PASSED.
- [x] Frontend ESLint — PASSED.
- [x] Frontend production build — PASSED; 2,105 modules transformed.
- [x] `git diff --check` — PASSED.
- [x] Verified through API tests that extraction does not create or save assignments.

### Known limitations

- AI suggestions are not guaranteed to be correct.
- User confirmation before saving is not implemented yet.
- OCR for scanned/image-only PDFs remains unsupported.
- Ollama is optional; the core application must continue working if it is unavailable.

### Git state

- Four intended Day 31 application files were committed as `7f1f507` — `feat: add local AI assignment extraction`.
- The commit was successfully pushed to `origin/master`.
- Final Git verification confirmed local `master` and `origin/master` synchronized at `7f1f507`.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.

### Next task

**Day 32 — Human confirmation before saving extracted assignment details.**

Build a review workflow that allows the user to inspect and edit extracted fields before explicitly confirming assignment creation. Never save AI-generated information automatically.

## Day 32 — Human Confirmation Before Saving AI-Extracted Details (4 November 2026)

**Status: IMPLEMENTED, VERIFIED, COMMITTED, AND PUSHED (`d2f5b56`).**

### Objectives
- [x] Let users review AI-extracted assignment details before saving.
- [x] Allow editing the suggested title, due date, and requirements.
- [x] Require an explicit confirmation action before assignment creation.
- [x] Allow users to discard AI suggestions without saving.
- [x] Verify that confirmed assignments persist after a browser refresh.

### Implementation
- [x] Improved the extraction prompt to identify assignment titles, explicit due dates, and relevant requirements more reliably.
- [x] Added instructions to treat document content as untrusted input.
- [x] Used the Pydantic `AssignmentExtraction` JSON schema for Ollama structured output and set `temperature: 0`.
- [x] Added editable fields for the extracted title, due date, and requirements in the document uploader.
- [x] Added **Confirm & Save Assignment** and discard actions.
- [x] Connected confirmed details to the existing assignment-creation workflow.
- [x] Kept the extracted document preview available when assignment saving fails and surfaced the error.
- [x] Fixed assignment-list visibility: the default list limit is now 100 and results are ordered by newest assignment first.

### Files changed
- `backend/app/main.py`
- `backend/app/services/ai_extraction_service.py`
- `frontend/src/components/assignments/DocumentUploader.jsx`
- `frontend/src/pages/AssignmentsPage.jsx`
- `frontend/src/services/api.js`

### Testing and verification
- [x] Full backend pytest suite: **98 passed**.
- [x] Frontend ESLint — PASSED.
- [x] Frontend production build — PASSED; 2,105 modules transformed.
- [x] `git diff --check` — PASSED.
- [x] Browser-tested editing the extracted assignment details before confirmation.
- [x] Browser-tested explicit confirmation and assignment creation.
- [x] Refreshed the browser and confirmed the saved assignment persisted.
- [x] Confirmed the assignment-list visibility fix.
- [x] Confirmed no assignment is created from AI suggestions without the user's confirmation.

### Git state
- Five intended application files were committed as `d2f5b56` — `feat: add human confirmation for AI assignments`.
- Successfully pushed to `origin/master`.
- Final local Git verification confirmed `master` and `origin/master` synchronized at `d2f5b56`.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.

### Next task
**Day 33 — Test missing dates, ambiguous instructions, and incorrect AI suggestions.**

## Day 33 — Missing Dates, Ambiguous Instructions, and Incorrect AI Suggestions (5 November 2026)

**Status: IMPLEMENTED, VERIFIED, COMMITTED, AND PUSHED (`7d32c29`).**

### Objectives
- [x] Test documents without explicit due dates.
- [x] Test ambiguous date instructions.
- [x] Reject unsupported AI-generated titles.
- [x] Reject unsupported due dates and requirements.
- [x] Validate extracted values against supporting evidence in the source document.
- [x] Verify the extraction workflow with a real assignment PDF and local Ollama.

### Implementation
- [x] Added title, due-date, and requirement evidence fields to `AssignmentExtraction`.
- [x] Updated the Ollama extraction prompt to request exact supporting evidence and treat document content as untrusted input.
- [x] Added normalized evidence comparison and validation for titles and requirements.
- [x] Added due-date validation requiring the date and an explicit deadline indicator on the same evidence line.
- [x] Added document-boundary handling to exclude content after the `-END-` marker.
- [x] Discard unsupported extracted values instead of returning them as valid suggestions.

### Files changed
- `backend/app/services/ai_extraction_service.py`
- `backend/tests/test_ai_extraction.py`

### Testing and verification
- [x] Tested missing due dates and ambiguous date instructions.
- [x] Tested unsupported titles and incorrect title evidence.
- [x] Tested unsupported requirements and unrelated evidence.
- [x] Tested unsupported due-date evidence.
- [x] Tested event dates being mistaken for deadlines, including evidence containing multiple dates.
- [x] AI extraction test suite: **21 passed**.
- [x] Full backend pytest suite: **107 passed**.
- [x] Python compilation check for the AI extraction service — PASSED.
- [x] `git diff --check` — PASSED.
- [x] Reviewed the final service and test diffs.
- [x] Manually tested a real assignment PDF through the frontend using local Ollama; title, due date, and requirements appeared correctly.
- [x] Confirmed extracted details could be reviewed and explicitly confirmed before saving.
- [x] Confirmed the assignment was saved and persisted after a browser refresh.

### Known limitations
- Evidence validation uses conservative normalized substring matching; some legitimate paraphrases or alternative date formats may be rejected.
- Automated evidence matching reduces unsupported suggestions but does not prove semantic correctness.
- Ollama remains optional; the core application must remain usable when it is unavailable.

### Git state
- The two Day 33 application files were committed as `7d32c29` — `feat: validate AI extraction evidence` — and pushed to `origin/master`.
- Final Git verification confirmed local `master` and `origin/master` synchronized at `7d32c29`.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.

### Next task
**Day 34 — File validation, error handling, and upload limits.**

## Day 34 — File Validation, Error Handling, and Upload Limits (5 November 2026)

**Status: IMPLEMENTED AND VERIFIED LOCALLY; NOT YET COMMITTED OR PUSHED.**

### Objectives
- [x] Verify the existing PDF upload validation and error-handling baseline.
- [x] Add regression coverage for encrypted PDF uploads.
- [x] Improve frontend state cleanup when selecting a new document.
- [x] Run backend and frontend regression checks.
- [x] Manually verify the document upload and preview workflow.

### Implementation
- [x] Added `test_reject_encrypted_pdf` to `backend/tests/test_pdf_upload.py`.
- [x] Verified the upload endpoint rejects an encrypted PDF with HTTP 400 and an encryption-related error message.
- [x] Updated `frontend/src/components/assignments/DocumentUploader.jsx` to clear previous AI suggestions, AI errors, save errors, preview data, and selected-file state when a new file is selected.
- [x] Preserved the existing review-and-confirm-before-save workflow; no automatic assignment saving was introduced.

### Files changed
- `backend/tests/test_pdf_upload.py`
- `frontend/src/components/assignments/DocumentUploader.jsx`

### Testing and verification
- [x] PDF upload test suite: **8 passed**.
- [x] Full backend pytest suite: **108 passed**.
- [x] Frontend ESLint: PASSED.
- [x] Frontend production build: PASSED; 2,105 modules transformed.
- [x] `git diff --check`: PASSED.
- [x] Manually tested valid PDF preview.
- [x] Manually tested non-PDF rejection.
- [x] Manually selected another PDF and confirmed previous AI suggestions and errors were cleared.
- [x] Reviewed both intended file diffs.

### Git state
- Day 34 changes are present locally in the two files listed above.
- Changes have not been staged, committed, or pushed.
- `backend/oop_practice.py` remains untracked, untouched, and intentionally excluded.
- The Day 34 status documentation is being recorded separately; it does not imply the application changes have been committed.

### Next task
**Day 35 — Measure extraction success, errors, and response time.**
