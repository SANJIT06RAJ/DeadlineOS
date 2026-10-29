
from datetime import date, timedelta
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
    assert "days_remaining" in data
    assert "is_overdue" in data
    assert data["days_remaining"] is None or isinstance(
    data["days_remaining"], int
    )
    assert isinstance(data["is_overdue"], bool)


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

def test_assignment_response_includes_deadline_fields(client):
    response = client.post(
        "/assignments",
        json={
            "title": "Overdue API Test",
            "due_date": "2020-01-01",
            "status": "pending",
        },
    )

    assert response.status_code == 201
    data = response.json()

    assert data["days_remaining"] < 0
    assert data["is_overdue"] is True


def test_assignment_summary_counts_statuses(client):
    client.post(
        "/assignments",
        json={"title": "Pending task", "status": "pending"},
    )
    client.post(
        "/assignments",
        json={"title": "In progress task", "status": "in_progress"},
    )
    client.post(
        "/assignments",
        json={"title": "Completed task", "status": "completed"},
    )

    response = client.get("/assignments/summary")

    assert response.status_code == 200
    data = response.json()

    assert data["total_assignments"] == 3
    assert data["pending_assignments"] == 1
    assert data["in_progress_assignments"] == 1
    assert data["completed_assignments"] == 1
    assert data["overdue_assignments"] == 0
    assert data["due_today_assignments"] == 0
    assert data["upcoming_assignments"] == 0
    assert data["no_due_date_assignments"] == 3


def test_assignment_summary_counts_overdue_tasks(client):
    client.post(
        "/assignments",
        json={
            "title": "Overdue task",
            "due_date": "2020-01-01",
            "status": "pending",
        },
    )
    client.post(
        "/assignments",
        json={
            "title": "Completed old task",
            "due_date": "2020-01-01",
            "status": "completed",
        },
    )

    response = client.get("/assignments/summary")

    assert response.status_code == 200
    data = response.json()

    assert data["total_assignments"] == 2
    assert data["overdue_assignments"] == 1
    assert data["completed_assignments"] == 1



def test_list_assignments_sorts_by_due_date(client):
    client.post(
        "/assignments",
        json={"title": "No deadline"},
    )
    client.post(
        "/assignments",
        json={"title": "Later task", "due_date": "2099-12-31"},
    )
    client.post(
        "/assignments",
        json={"title": "Earlier task", "due_date": "2020-01-01"},
    )

    response = client.get("/assignments")

    assert response.status_code == 200
    assignments = response.json()

    assert [
        assignment["title"] for assignment in assignments
    ] == ["Earlier task", "Later task", "No deadline"]


def test_assignment_summary_counts_due_today_and_upcoming(client):
    today = date.today()
    tomorrow = today + timedelta(days=1)

    client.post(
        "/assignments",
        json={
            "title": "Due today",
            "due_date": today.isoformat(),
            "status": "pending",
        },
    )
    client.post(
        "/assignments",
        json={
            "title": "Due tomorrow",
            "due_date": tomorrow.isoformat(),
            "status": "in_progress",
        },
    )

    response = client.get("/assignments/summary")

    assert response.status_code == 200
    data = response.json()

    assert data["due_today_assignments"] == 1
    assert data["upcoming_assignments"] == 1


def test_update_missing_assignment_returns_404(client):
    response = client.patch(
        "/assignments/9999",
        json={"title": "Updated title"},
    )

    assert response.status_code == 404


def test_list_subtasks_for_missing_assignment_returns_404(client):
    response = client.get("/assignments/9999/subtasks")

    assert response.status_code == 404


def test_update_missing_subtask_returns_404(client):
    response = client.patch(
        "/subtasks/9999",
        json={"title": "Updated task"},
    )

    assert response.status_code == 404


def test_delete_missing_subtask_returns_404(client):
    response = client.delete("/subtasks/9999")

    assert response.status_code == 404


def test_update_assignment_with_empty_payload_returns_400(client):
    created = client.post(
        "/assignments",
        json={"title": "Assignment"},
    ).json()

    response = client.patch(f"/assignments/{created['id']}", json={})

    assert response.status_code == 400


def test_update_subtask_with_empty_payload_returns_400(client):
    assignment = client.post(
        "/assignments",
        json={"title": "Assignment"},
    ).json()

    subtask = client.post(
        f"/assignments/{assignment['id']}/subtasks",
        json={"title": "Subtask"},
    ).json()

    response = client.patch(f"/subtasks/{subtask['id']}", json={})

    assert response.status_code == 400


def test_list_assignments_filters_by_status(client):
    client.post(
        "/assignments",
        json={"title": "Pending task", "status": "pending"},
    )
    client.post(
        "/assignments",
        json={"title": "In progress task", "status": "in_progress"},
    )
    client.post(
        "/assignments",
        json={"title": "Completed task", "status": "completed"},
    )

    response = client.get("/assignments?status=pending")

    assert response.status_code == 200
    assignments = response.json()
    assert len(assignments) == 1
    assert assignments[0]["title"] == "Pending task"
    assert assignments[0]["status"] == "pending"


def test_list_assignments_supports_limit_and_offset(client):
    for index in range(3):
        client.post(
            "/assignments",
            json={
                "title": f"Assignment {index + 1}",
                "due_date": f"2026-11-{index + 1:02d}",
            },
        )

    response = client.get("/assignments?limit=1&offset=1")

    assert response.status_code == 200
    assignments = response.json()
    assert len(assignments) == 1
    assert assignments[0]["title"] == "Assignment 2"


def test_list_assignments_rejects_invalid_status_filter(client):
    response = client.get("/assignments?status=started")

    assert response.status_code == 422


def test_list_assignments_rejects_invalid_pagination(client):
    response = client.get("/assignments?limit=0")

    assert response.status_code == 422


def test_update_assignment_rejects_null_status(client):
    created = client.post(
        "/assignments",
        json={"title": "Assignment"},
    ).json()

    response = client.patch(
        f"/assignments/{created['id']}",
        json={"status": None},
    )

    assert response.status_code == 422


def test_update_subtask_rejects_mixed_valid_and_null_fields(client):
    assignment = client.post(
        "/assignments",
        json={"title": "Assignment"},
    ).json()

    subtask = client.post(
        f"/assignments/{assignment['id']}/subtasks",
        json={"title": "Original task"},
    ).json()

    response = client.patch(
        f"/subtasks/{subtask['id']}",
        json={
            "title": "Changed task",
            "is_completed": None,
        },
    )

    assert response.status_code == 422

    subtasks = client.get(
        f"/assignments/{assignment['id']}/subtasks"
    ).json()

    assert len(subtasks) == 1
    assert subtasks[0]["title"] == "Original task"
    assert subtasks[0]["is_completed"] is False


def test_create_assignment_rejects_invalid_due_date(client):
    response = client.post(
        "/assignments",
        json={
            "title": "Invalid date",
            "due_date": "not-a-date",
        },
    )

    assert response.status_code == 422


def test_update_assignment_rejects_invalid_due_date_without_partial_update(client):
    created = client.post(
        "/assignments",
        json={
            "title": "Original title",
            "due_date": "2026-11-15",
        },
    ).json()

    response = client.patch(
        f"/assignments/{created['id']}",
        json={
            "title": "Changed title",
            "due_date": "not-a-date",
        },
    )

    assert response.status_code == 422

    unchanged = client.get(f"/assignments/{created['id']}")
    assert unchanged.status_code == 200
    assert unchanged.json()["title"] == "Original title"
    assert unchanged.json()["due_date"] == "2026-11-15"


def test_create_assignment_rejects_missing_title(client):
    response = client.post(
        "/assignments",
        json={"description": "Title was omitted"},
    )

    assert response.status_code == 422


def test_update_assignment_rejects_mixed_valid_and_null_fields(client):
    created = client.post(
        "/assignments",
        json={"title": "Original title", "status": "pending"},
    ).json()

    response = client.patch(
        f"/assignments/{created['id']}",
        json={"title": "Changed title", "status": None},
    )

    assert response.status_code == 422

    unchanged = client.get(f"/assignments/{created['id']}")
    assert unchanged.status_code == 200
    assert unchanged.json()["title"] == "Original title"
    assert unchanged.json()["status"] == "pending"


def test_create_assignment_rejects_title_over_200_characters(client):
    response = client.post(
        "/assignments",
        json={"title": "A" * 201},
    )

    assert response.status_code == 422


def test_create_subtask_rejects_title_over_200_characters(client):
    assignment = client.post(
        "/assignments",
        json={"title": "Assignment"},
    ).json()

    response = client.post(
        f"/assignments/{assignment['id']}/subtasks",
        json={"title": "A" * 201},
    )

    assert response.status_code == 422


def test_update_assignment_rejects_overlong_title_without_partial_update(client):
    created = client.post(
        "/assignments",
        json={"title": "Original title"},
    ).json()

    response = client.patch(
        f"/assignments/{created['id']}",
        json={"title": "A" * 201},
    )

    assert response.status_code == 422

    unchanged = client.get(f"/assignments/{created['id']}")
    assert unchanged.status_code == 200
    assert unchanged.json()["title"] == "Original title"


def test_update_subtask_rejects_overlong_title_without_partial_update(client):
    assignment = client.post(
        "/assignments",
        json={"title": "Assignment"},
    ).json()

    subtask = client.post(
        f"/assignments/{assignment['id']}/subtasks",
        json={"title": "Original subtask"},
    ).json()

    response = client.patch(
        f"/subtasks/{subtask['id']}",
        json={"title": "A" * 201},
    )

    assert response.status_code == 422

    subtasks = client.get(
        f"/assignments/{assignment['id']}/subtasks"
    ).json()

    assert len(subtasks) == 1
    assert subtasks[0]["title"] == "Original subtask"
