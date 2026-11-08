from datetime import date


def calculate_days_remaining(due_date: date, today: date) -> int:
    """Return the number of days until an assignment is due."""
    return (due_date - today).days


def is_overdue(
    due_date: date | None,
    status: str,
    today: date,
) -> bool:
    """Return whether an unfinished assignment is past its due date."""
    if due_date is None or status == "completed":
        return False

    return due_date < today


def validate_assignment_title(title: str) -> str:
    """Return a cleaned title or raise an error if it is empty."""
    cleaned_title = title.strip()

    if not cleaned_title:
        raise ValueError("Assignment title cannot be empty.")

    return cleaned_title
