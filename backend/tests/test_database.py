import sqlite3

import pytest
from app import database


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
    with database.get_connection() as connection, pytest.raises(sqlite3.IntegrityError):
        connection.execute(
            "INSERT INTO subtasks (assignment_id, title) VALUES(?, ?)",
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


def test_database_schema_and_foreign_keys(test_db):
    with database.get_connection() as connection:
        assignment_columns = {
            row["name"] for row in connection.execute("PRAGMA table_info(assignments)")
        }

        subtask_columns = {
            row["name"] for row in connection.execute("PRAGMA table_info(subtasks)")
        }

        foreign_keys_enabled = connection.execute("PRAGMA foreign_keys").fetchone()[0]

        subtask_foreign_keys = connection.execute(
            "PRAGMA foreign_key_list(subtasks)"
        ).fetchall()

    assert {
        "id",
        "title",
        "description",
        "due_date",
        "status",
        "created_at",
    } <= assignment_columns

    assert {
        "id",
        "assignment_id",
        "title",
        "is_completed",
    } <= subtask_columns
    assert foreign_keys_enabled == 1
    assert any(
        row["table"] == "assignments"
        and row["from"] == "assignment_id"
        and row["to"] == "id"
        and row["on_delete"].upper() == "CASCADE"
        for row in subtask_foreign_keys
    )


def test_subtask_estimated_minutes_column_is_created(test_db):
    with database.get_connection() as connection:
        columns = {
            row["name"] for row in connection.execute("PRAGMA table_info(subtasks)")
        }

    assert "estimated_minutes" in columns


def test_existing_subtasks_survive_estimated_minutes_migration(tmp_path, monkeypatch):
    db_path = tmp_path / "legacy_deadlineos.db"
    monkeypatch.setattr(database, "DATABASE_PATH", db_path)

    # Simulate the older database schema before the migration.
    with sqlite3.connect(db_path) as connection:
        connection.execute("""
            CREATE TABLE assignments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                due_date TEXT,
                status TEXT NOT NULL DEFAULT 'pending',
                priority TEXT NOT NULL DEFAULT 'medium',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)

        connection.execute("""
            CREATE TABLE subtasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                assignment_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                is_completed INTEGER NOT NULL DEFAULT 0,
                FOREIGN KEY (assignment_id)
                    REFERENCES assignments(id)
                    ON DELETE CASCADE
            )
        """)

        cursor = connection.execute(
            "INSERT INTO assignments (title) VALUES (?)",
            ("Legacy Assignment",),
        )
        assignment_id = cursor.lastrowid

        connection.execute(
            """
            INSERT INTO subtasks (assignment_id, title)
            VALUES (?, ?)
            """,
            (assignment_id, "Existing Subtask"),
        )

    # Run the migration.
    database.create_tables()

    with database.get_connection() as connection:
        subtask = connection.execute(
            "SELECT * FROM subtasks WHERE assignment_id = ?",
            (assignment_id,),
        ).fetchone()

    assert subtask["title"] == "Existing Subtask"
    assert subtask["estimated_minutes"] is None


def test_database_rejects_non_positive_estimated_minutes(test_db):
    with database.get_connection() as connection:
        cursor = connection.execute(
            "INSERT INTO assignments (title) VALUES (?)",
            ("Estimate Test",),
        )
        assignment_id = cursor.lastrowid

        with pytest.raises(sqlite3.IntegrityError):
            connection.execute(
                """
                INSERT INTO subtasks (
                    assignment_id, title, estimated_minutes
                )
                VALUES (?, ?, ?)
                """,
                (assignment_id, "Invalid Estimate", 0),
            )
