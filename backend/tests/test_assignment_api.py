
import pytest
from fastapi.testclient import TestClient

from app.database import create_tables, get_connection
from app.main import app


@pytest.fixture
def client(tmp_path, monkeypatch):
    # Give each test its own temporary SQLite database.
    import app.database as database

    test_db = tmp_path / "test_deadlineos.db"
    monkeypatch.setattr(database, "DATABASE_PATH", test_db)

    create_tables()

    with TestClient(app) as test_client:
        yield test_client


def test_create_assignment(client):
    response = client.post(
        "/assignments",
        json={
            "title": "  Database Assignment  ",
            "description": "Finish the SQL report",
            "due_date": "2026-10-30",
        },
    )

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Database Assignment"
    assert data["description"] == "Finish the SQL report"
    assert data["due_date"] == "2026-10-30"
    assert data["status"] == "pending"
    assert isinstance(data["id"], int)


def test_list_assignments(client):
    client.post("/assignments", json={"title": "Assignment A"})
    client.post("/assignments", json={"title": "Assignment B"})

    response = client.get("/assignments")

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_assignment(client):
    created = client.post(
        "/assignments",
        json={"title": "Find me"},
    ).json()

    response = client.get(f"/assignments/{created['id']}")

    assert response.status_code == 200
    assert response.json()["title"] == "Find me"


def test_get_missing_assignment_returns_404(client):
    response = client.get("/assignments/9999")

    assert response.status_code == 404


def test_update_assignment(client):
    created = client.post(
        "/assignments",
        json={"title": "Original title"},
    ).json()

    response = client.patch(
        f"/assignments/{created['id']}",
        json={"title": "Updated title", "status": "in_progress"},
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Updated title"
    assert response.json()["status"] == "in_progress"


def test_reject_empty_assignment_title(client):
    response = client.post(
        "/assignments",
        json={"title": "   "},
    )

    assert response.status_code == 422


def test_reject_invalid_assignment_status(client):
    response = client.post(
        "/assignments",
        json={"title": "Invalid status", "status": "started"},
    )

    assert response.status_code == 422


def test_delete_assignment(client):
    created = client.post(
        "/assignments",
        json={"title": "Delete me"},
    ).json()

    response = client.delete(f"/assignments/{created['id']}")

    assert response.status_code == 204
    assert client.get(f"/assignments/{created['id']}").status_code == 404


def test_delete_missing_assignment_returns_404(client):
    response = client.delete("/assignments/9999")

    assert response.status_code == 404


def test_update_rejects_null_title(client):
    created = client.post(
        "/assignments",
        json={"title": "Original title"},
    ).json()

    response = client.patch(
        f"/assignments/{created['id']}",
        json={"title": None},
    )

    assert response.status_code == 422


def test_update_can_clear_description(client):
    created = client.post(
        "/assignments",
        json={
            "title": "Assignment",
            "description": "Remove this description",
        },
    ).json()

    response = client.patch(
        f"/assignments/{created['id']}",
        json={"description": None},
    )

    assert response.status_code == 200
    assert response.json()["description"] is None


def test_create_subtask(client):
    assignment = client.post(
        "/assignments",
        json={"title": "Database Assignment"},
    ).json()

    response = client.post(
        f"/assignments/{assignment['id']}/subtasks",
        json={"title": "  Write SQL queries  "},
    )

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Write SQL queries"
    assert data["assignment_id"] == assignment["id"]
    assert data["is_completed"] is False


def test_list_subtasks(client):
    assignment = client.post(
        "/assignments",
        json={"title": "Database Assignment"},
    ).json()

    client.post(
        f"/assignments/{assignment['id']}/subtasks",
        json={"title": "Task A"},
    )
    client.post(
        f"/assignments/{assignment['id']}/subtasks",
        json={"title": "Task B"},
    )

    response = client.get(
        f"/assignments/{assignment['id']}/subtasks"
    )

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_create_subtask_for_missing_assignment_returns_404(client):
    response = client.post(
        "/assignments/9999/subtasks",
        json={"title": "Orphan task"},
    )

    assert response.status_code == 404


def test_update_subtask(client):
    assignment = client.post(
        "/assignments",
        json={"title": "Database Assignment"},
    ).json()

    subtask = client.post(
        f"/assignments/{assignment['id']}/subtasks",
        json={"title": "Original task"},
    ).json()

    response = client.patch(
        f"/subtasks/{subtask['id']}",
        json={"title": "Updated task", "is_completed": True},
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Updated task"
    assert response.json()["is_completed"] is True


def test_delete_subtask(client):
    assignment = client.post(
        "/assignments",
        json={"title": "Database Assignment"},
    ).json()

    subtask = client.post(
        f"/assignments/{assignment['id']}/subtasks",
        json={"title": "Remove this task"},
    ).json()

    response = client.delete(f"/subtasks/{subtask['id']}")

    assert response.status_code == 204

    remaining = client.get(
        f"/assignments/{assignment['id']}/subtasks"
    )
    assert remaining.json() == []


def test_reject_empty_subtask_title(client):
    assignment = client.post(
        "/assignments",
        json={"title": "Database Assignment"},
    ).json()

    response = client.post(
        f"/assignments/{assignment['id']}/subtasks",
        json={"title": "   "},
    )

    assert response.status_code == 422
