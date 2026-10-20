
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Response, status

from app.database import create_tables, get_connection
from app.schemas import (
    AssignmentCreate,
    AssignmentResponse,
    AssignmentUpdate,
    SubtaskCreate,
    SubtaskResponse,
    SubtaskUpdate,
)

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



@app.get("/")
def home():
    return {
        "message": "Welcome to DeadlineOS",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/assignments", response_model=list[AssignmentResponse])
def list_assignments():
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT * FROM assignments ORDER BY due_date IS NULL, due_date, id"
        ).fetchall()

    return [dict(row) for row in rows]


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
            INSERT INTO assignments (title, description, due_date, status)
            VALUES (?, ?, ?, ?)
            """,
            (
                data["title"],
                data["description"],
                data["due_date"].isoformat() if data["due_date"] else None,
                data["status"],
            ),
        )
        row = connection.execute(
            "SELECT * FROM assignments WHERE id = ?",
            (cursor.lastrowid,),
        ).fetchone()

    return dict(row)


@app.get("/assignments/{assignment_id}", response_model=AssignmentResponse)
def get_assignment(assignment_id: int):
    with get_connection() as connection:
        row = connection.execute(
            "SELECT * FROM assignments WHERE id = ?",
            (assignment_id,),
        ).fetchone()

    if row is None:
        raise HTTPException(status_code=404, detail="Assignment not found")

    return dict(row)


@app.patch("/assignments/{assignment_id}", response_model=AssignmentResponse)
def update_assignment(assignment_id: int, assignment: AssignmentUpdate):
    changes = assignment.model_dump(exclude_unset=True)

    if not changes:
        raise HTTPException(status_code=400, detail="No fields provided to update")

    if any(
        value is None and key not in {"description", "due_date"}
        for key, value in changes.items()
    ):
        raise HTTPException(
            status_code=422,
            detail="Title and status cannot be null",
        )

    if "due_date" in changes and changes["due_date"] is not None:
        changes["due_date"] = changes["due_date"].isoformat()

    columns = {
        "title": "title",
        "description": "description",
        "due_date": "due_date",
        "status": "status",
    }
    assignments_sql = ", ".join(
        f"{columns[key]} = ?" for key in changes
    )
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

    return dict(row)


@app.delete("/assignments/{assignment_id}", status_code=status.HTTP_204_NO_CONTENT)
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

    return [
        {**dict(row), "is_completed": bool(row["is_completed"])}
        for row in rows
    ]


@app.post(
    "/assignments/{assignment_id}/subtasks",
    response_model=SubtaskResponse,
    status_code=status.HTTP_201_CREATED,
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
            INSERT INTO subtasks (assignment_id, title)
            VALUES (?, ?)
            """,
            (assignment_id, subtask.title),
        )

        row = connection.execute(
            "SELECT * FROM subtasks WHERE id = ?",
            (cursor.lastrowid,),
        ).fetchone()

    return {**dict(row), "is_completed": bool(row["is_completed"])}


@app.patch("/subtasks/{subtask_id}", response_model=SubtaskResponse)
def update_subtask(subtask_id: int, subtask: SubtaskUpdate):
    changes = subtask.model_dump(exclude_unset=True)

    if not changes:
        raise HTTPException(status_code=400, detail="No fields provided to update")

    if any(value is None for value in changes.values()):
        raise HTTPException(
            status_code=422,
            detail="Subtask title and completion state cannot be null",
        )

    if "is_completed" in changes:
        changes["is_completed"] = int(changes["is_completed"])

    columns = {"title": "title", "is_completed": "is_completed"}
    assignments_sql = ", ".join(
        f"{columns[key]} = ?" for key in changes
    )

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


@app.delete("/subtasks/{subtask_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_subtask(subtask_id: int):
    with get_connection() as connection:
        cursor = connection.execute(
            "DELETE FROM subtasks WHERE id = ?",
            (subtask_id,),
        )

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Subtask not found")

    return Response(status_code=status.HTTP_204_NO_CONTENT)
