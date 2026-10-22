
import sqlite3

import pytest

import app.database as database


@pytest.fixture
def test_db(tmp_path, monkeypatch):
    """Use a separate temporary database for each test."""
    db_path = tmp_path / "test_deadlineos.db"
    monkeypatch.setattr(database, "DATABASE_PATH", db_path)
    database.create_tables()
    return db_path


def test_tables_are_created(test_db):
    with database.get_connection() as connection:
        tables = {
            row["name"]
            for row in connection.execute(
                "SELECT name FROM sqlite_master "
                "WHERE type = 'table' AND name NOT LIKE 'sqlite_%'"
            )
        }

    assert "assignments" in tables
    assert "subtasks" in tables


def test_subtask_can_reference_assignment(test_db):
    with database.get_connection() as connection:
        cursor = connection.execute(
            "INSERT INTO assignments (title) VALUES (?)",
            ("Test Assignment",),
        )
        assignment_id = cursor.lastrowid

        connection.execute(
            "INSERT INTO subtasks (assignment_id, title) VALUES (?, ?)",
            (assignment_id, "Test Subtask"),
        )

        subtask = connection.execute(
            "SELECT title FROM subtasks WHERE assignment_id = ?",
            (assignment_id,),
        ).fetchone()

        assert subtask["title"] == "Test Subtask"


def test_invalid_assignment_id_is_rejected(test_db):
    with database.get_connection() as connection:
        with pytest.raises(sqlite3.IntegrityError):
            connection.execute(
                "INSERT INTO subtasks (assignment_id, title) VALUES (?, ?)",
                (-1, "Invalid Subtask"),
            )


def test_deleting_assignment_deletes_subtasks(test_db):
    with database.get_connection() as connection:
        cursor = connection.execute(
            "INSERT INTO assignments (title) VALUES (?)",
            ("Cascade Test",),
        )
        assignment_id = cursor.lastrowid

        connection.execute(
            "INSERT INTO subtasks (assignment_id, title) VALUES (?, ?)",
            (assignment_id, "Subtask to Delete"),
        )

        connection.execute(
            "DELETE FROM assignments WHERE id = ?",
            (assignment_id,),
        )

        remaining = connection.execute(
            "SELECT COUNT(*) FROM subtasks WHERE assignment_id = ?",
            (assignment_id,),
        ).fetchone()[0]

    assert remaining == 0
