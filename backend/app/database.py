import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).resolve().parent.parent / "deadlineos.db"


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def create_tables() -> None:
    from contextlib import closing

    with closing(get_connection()) as connection:
        with connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS assignments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    due_date TEXT,
                    status TEXT NOT NULL DEFAULT 'pending'
                        CHECK (status IN ('pending', 'in_progress','completed')),
                    priority TEXT NOT NULL DEFAULT 'medium'
                        CHECK (priority IN ('low', 'medium', 'high')),
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # Safely migrate existing assignment databases.
            columns = {
                row["name"]
                for row in connection.execute(
                    "PRAGMA table_info(assignments)"
                ).fetchall()
            }

            if "priority" not in columns:
                connection.execute("""
                    ALTER TABLE assignments
                    ADD COLUMN priority TEXT NOT NULL DEFAULT 'medium'
                    CHECK (priority IN ('low', 'medium', 'high'))
                """)

            connection.execute("""
                CREATE TABLE IF NOT EXISTS subtasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    assignment_id INTEGER NOT NULL,
                    title TEXT NOT NULL,
                    is_completed INTEGER NOT NULL DEFAULT 0
                        CHECK (is_completed IN (0, 1)),
                    estimated_minutes INTEGER
                        CHECK (
                            estimated_minutes IS NULL
                            OR estimated_minutes > 0
                        ),
                    FOREIGN KEY (assignment_id)
                        REFERENCES assignments(id)
                        ON DELETE CASCADE
                )
            """)

            # Safely migrate existing subtask databases.
            subtask_columns = {
                row["name"]
                for row in connection.execute(
                    "PRAGMA table_info(subtasks)"
                ).fetchall()
            }

            if "estimated_minutes" not in subtask_columns:
                connection.execute("""
                    ALTER TABLE subtasks
                    ADD COLUMN estimated_minutes INTEGER
                    CHECK (
                        estimated_minutes IS NULL
                        OR estimated_minutes > 0
                    )
                """)
