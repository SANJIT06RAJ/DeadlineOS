from contextlib import asynccontextmanager
from datetime import date

from fastapi import (
    FastAPI,
    File,
    HTTPException,
    Query,
    Response,
    UploadFile,
    status,
)

from app.database import create_tables, get_connection
from app.schemas import (
    AssignmentCreate,
    AssignmentExtractionRequest,
    AssignmentResponse,
    AssignmentStatus,
    AssignmentSummary,
    AssignmentUpdate,
    SubtaskCreate,
    SubtaskResponse,
    SubtaskUpdate,
)
from app.services.ai_extraction_service import extract_assignment_details
from app.services.assignment_service import (
    calculate_days_remaining,
    is_overdue,
)
from app.services.pdf_service import extract_pdf_text


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI(
    title="DeadlineOS API",
    description="Academic Task & Deadline Intelligence",
    version="0.1.0",
    lifespan=lifespan,
)


def serialize_assignment(row):
    data = dict(row)

    due_date_value = date.fromisoformat(data["due_date"]) if data["due_date"] else None
    today = date.today()

    data["days_remaining"] = (
        calculate_days_remaining(due_date_value, today)
        if due_date_value is not None
        else None
    )
    data["is_overdue"] = is_overdue(
        due_date_value,
        data["status"],
        today,
    )

    return data


@app.get("/")
def home():
    return {
        "message": "Welcome to DeadlineOS",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


MAX_PDF_SIZE = 10 * 1024 * 1024  # 10 MB


@app.post("/documents/preview")
async def preview_document(file: UploadFile = File(...)):
    """
    Upload a PDF and return its extracted text for preview.

    This endpoint does not create or save an assignment.
    """

    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=415,
            detail="Only PDF files are supported.",
        )

    try:
        pdf_bytes = await file.read(MAX_PDF_SIZE + 1)

        if not pdf_bytes:
            raise HTTPException(
                status_code=400,
                detail="The uploaded file is empty.",
            )

        if len(pdf_bytes) > MAX_PDF_SIZE:
            raise HTTPException(
                status_code=413,
                detail="PDF file exceeds the 10 MB size limit.",
            )

        if not pdf_bytes.startswith(b"%PDF-"):
            raise HTTPException(
                status_code=415,
                detail="The uploaded file is not a valid PDF.",
            )

        try:
            extracted_text = extract_pdf_text(pdf_bytes)
        except ValueError as exc:
            raise HTTPException(
                status_code=400,
                detail=str(exc),
            ) from exc

        return {
            "filename": file.filename,
            "text": extracted_text,
            "character_count": len(extracted_text),
        }

    finally:
        await file.close()


@app.post("/documents/extract")
def extract_document_details(
    request: AssignmentExtractionRequest,
):
    """
    Extract assignment details from PDF text using a local AI model.

    This endpoint does not create or save an assignment.
    """

    try:
        result = extract_assignment_details(request.document_text)

        return {
            "title": result.title,
            "due_date": (result.due_date.isoformat() if result.due_date else None),
            "requirements": result.requirements,
        }

    except ValueError as exc:
        raise HTTPException(
            status_code=422,
            detail=str(exc),
        ) from exc

    except RuntimeError as exc:
        raise HTTPException(
            status_code=503,
            detail=str(exc),
        ) from exc


@app.get("/assignments", response_model=list[AssignmentResponse])
def list_assignments(
    status_filter: AssignmentStatus | None = Query(
        default=None,
        alias="status",
        description="Filter assignments by status",
    ),
    limit: int = Query(default=100, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
):
    query = "SELECT * FROM assignments"
    parameters = []

    if status_filter is not None:
        query += " WHERE status = ?"
        parameters.append(status_filter)

    query += " ORDER BY id DESC"
    query += " LIMIT ? OFFSET ?"
    parameters.extend([limit, offset])

    with get_connection() as connection:
        rows = connection.execute(
            query,
            parameters,
        ).fetchall()

    return [serialize_assignment(row) for row in rows]


@app.post(
    "/assignments",
    response_model=AssignmentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_assignment(assignment: AssignmentCreate):
    data = assignment.model_dump()

    with get_connection() as connection:
        cursor = connection.execute(
            """
            INSERT INTO assignments (
                title,
                description,
                due_date,
                status,
                priority
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                data["title"],
                data["description"],
                data["due_date"].isoformat() if data["due_date"] else None,
                data["status"],
                data["priority"],
            ),
        )

        row = connection.execute(
            "SELECT * FROM assignments WHERE id = ?",
            (cursor.lastrowid,),
        ).fetchone()

    return serialize_assignment(row)


@app.get("/assignments/summary", response_model=AssignmentSummary)
def get_assignment_summary():
    with get_connection() as connection:
        rows = connection.execute("SELECT due_date, status FROM assignments").fetchall()

    today = date.today()

    total = len(rows)
    pending = sum(row["status"] == "pending" for row in rows)
    in_progress = sum(row["status"] == "in_progress" for row in rows)
    completed = sum(row["status"] == "completed" for row in rows)

    overdue = 0
    due_today = 0
    upcoming = 0
    no_due_date = 0

    for row in rows:
        due_date_value = (
            date.fromisoformat(row["due_date"]) if row["due_date"] else None
        )

        if due_date_value is None:
            no_due_date += 1
            continue

        if row["status"] == "completed":
            continue

        if due_date_value < today:
            overdue += 1
        elif due_date_value == today:
            due_today += 1
        else:
            upcoming += 1

    return {
        "total_assignments": total,
        "pending_assignments": pending,
        "in_progress_assignments": in_progress,
        "completed_assignments": completed,
        "overdue_assignments": overdue,
        "due_today_assignments": due_today,
        "upcoming_assignments": upcoming,
        "no_due_date_assignments": no_due_date,
    }


@app.get(
    "/assignments/{assignment_id}",
    response_model=AssignmentResponse,
    responses={404: {"description": "Assignment not found"}},
)
def get_assignment(assignment_id: int):
    with get_connection() as connection:
        row = connection.execute(
            "SELECT * FROM assignments WHERE id = ?",
            (assignment_id,),
        ).fetchone()

    if row is None:
        raise HTTPException(status_code=404, detail="Assignment not found")

    return serialize_assignment(row)


@app.patch(
    "/assignments/{assignment_id}",
    response_model=AssignmentResponse,
    responses={404: {"description": "Assignment not found"}},
)
def update_assignment(assignment_id: int, assignment: AssignmentUpdate):
    changes = assignment.model_dump(exclude_unset=True)

    if not changes:
        raise HTTPException(
            status_code=400,
            detail="No fields provided to update",
        )

    if any(
        value is None and key not in {"description", "due_date"}
        for key, value in changes.items()
    ):
        raise HTTPException(
            status_code=422,
            detail="Title, status and priority cannot be null",
        )

    if "due_date" in changes and changes["due_date"] is not None:
        changes["due_date"] = changes["due_date"].isoformat()

    columns = {
        "title": "title",
        "description": "description",
        "due_date": "due_date",
        "status": "status",
        "priority": "priority",
    }

    assignments_sql = ", ".join(f"{columns[key]} = ?" for key in changes)
    values = list(changes.values())

    with get_connection() as connection:
        existing = connection.execute(
            "SELECT id FROM assignments WHERE id = ?",
            (assignment_id,),
        ).fetchone()

        if existing is None:
            raise HTTPException(status_code=404, detail="Assignment not found")

        connection.execute(
            f"UPDATE assignments SET {assignments_sql} WHERE id = ?",
            (*values, assignment_id),
        )

        row = connection.execute(
            "SELECT * FROM assignments WHERE id = ?",
            (assignment_id,),
        ).fetchone()

    return serialize_assignment(row)


@app.delete(
    "/assignments/{assignment_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"description": "Assignment not found"}},
)
def delete_assignment(assignment_id: int):
    with get_connection() as connection:
        cursor = connection.execute(
            "DELETE FROM assignments WHERE id = ?",
            (assignment_id,),
        )

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Assignment not found")

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.get(
    "/assignments/{assignment_id}/subtasks",
    response_model=list[SubtaskResponse],
    responses={404: {"description": "Assignment not found"}},
)
def list_subtasks(assignment_id: int):
    with get_connection() as connection:
        assignment = connection.execute(
            "SELECT id FROM assignments WHERE id = ?",
            (assignment_id,),
        ).fetchone()

        if assignment is None:
            raise HTTPException(status_code=404, detail="Assignment not found")

        rows = connection.execute(
            "SELECT * FROM subtasks WHERE assignment_id = ? ORDER BY id",
            (assignment_id,),
        ).fetchall()

    return [{**dict(row), "is_completed": bool(row["is_completed"])} for row in rows]


@app.post(
    "/assignments/{assignment_id}/subtasks",
    response_model=SubtaskResponse,
    status_code=status.HTTP_201_CREATED,
    responses={404: {"description": "Assignment not found"}},
)
def create_subtask(assignment_id: int, subtask: SubtaskCreate):
    with get_connection() as connection:
        assignment = connection.execute(
            "SELECT id FROM assignments WHERE id = ?",
            (assignment_id,),
        ).fetchone()

        if assignment is None:
            raise HTTPException(status_code=404, detail="Assignment not found")

        cursor = connection.execute(
            """
            INSERT INTO subtasks (
                assignment_id,
                title,
                estimated_minutes
            )
            VALUES (?, ?, ?)
            """,
            (
                assignment_id,
                subtask.title,
                subtask.estimated_minutes,
            ),
        )

        row = connection.execute(
            "SELECT * FROM subtasks WHERE id = ?",
            (cursor.lastrowid,),
        ).fetchone()

    return {**dict(row), "is_completed": bool(row["is_completed"])}


@app.patch(
    "/subtasks/{subtask_id}",
    response_model=SubtaskResponse,
    responses={404: {"description": "Subtask not found"}},
)
def update_subtask(subtask_id: int, subtask: SubtaskUpdate):
    changes = subtask.model_dump(exclude_unset=True)

    if not changes:
        raise HTTPException(
            status_code=400,
            detail="No fields provided to update",
        )

    if any(
        value is None and key != "estimated_minutes" for key, value in changes.items()
    ):
        raise HTTPException(
            status_code=422,
            detail="Subtask title and completion state cannot be null",
        )

    if "is_completed" in changes:
        changes["is_completed"] = int(changes["is_completed"])

    columns = {
        "title": "title",
        "is_completed": "is_completed",
        "estimated_minutes": "estimated_minutes",
    }

    assignments_sql = ", ".join(f"{columns[key]} = ?" for key in changes)

    with get_connection() as connection:
        existing = connection.execute(
            "SELECT id FROM subtasks WHERE id = ?",
            (subtask_id,),
        ).fetchone()

        if existing is None:
            raise HTTPException(status_code=404, detail="Subtask not found")

        connection.execute(
            f"UPDATE subtasks SET {assignments_sql} WHERE id = ?",
            (*changes.values(), subtask_id),
        )

        row = connection.execute(
            "SELECT * FROM subtasks WHERE id = ?",
            (subtask_id,),
        ).fetchone()

    return {**dict(row), "is_completed": bool(row["is_completed"])}


@app.delete(
    "/subtasks/{subtask_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"description": "Subtask not found"}},
)
def delete_subtask(subtask_id: int):
    with get_connection() as connection:
        cursor = connection.execute(
            "DELETE FROM subtasks WHERE id = ?",
            (subtask_id,),
        )

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Subtask not found")

    return Response(status_code=status.HTTP_204_NO_CONTENT)
