from datetime import date

import pytest

from app.services.assignment_service import (
    calculate_days_remaining,
    is_overdue,
    validate_assignment_title,
)


def test_future_deadline():
    assert calculate_days_remaining(
        date(2026, 10, 20),
        date(2026, 10, 16),
    ) == 4


def test_overdue_assignment():
    assert calculate_days_remaining(
        date(2026, 10, 14),
        date(2026, 10, 16),
    ) == -2


def test_deadline_is_today():
    assert calculate_days_remaining(
        date(2026, 10, 16),
        date(2026, 10, 16),
    ) == 0


def test_title_is_trimmed():
    assert validate_assignment_title("  Finish project  ") == "Finish project"


def test_empty_title_is_rejected():
    with pytest.raises(ValueError, match="cannot be empty"):
        validate_assignment_title("")


def test_whitespace_title_is_rejected():
    with pytest.raises(ValueError, match="cannot be empty"):
        validate_assignment_title("   ")


def test_pending_assignment_with_past_due_date_is_overdue():
    assert is_overdue(
        date(2026, 10, 14),
        "pending",
        date(2026, 10, 16),
    ) is True


def test_completed_assignment_is_not_overdue():
    assert is_overdue(
        date(2026, 10, 14),
        "completed",
        date(2026, 10, 16),
    ) is False


def test_assignment_without_due_date_is_not_overdue():
    assert is_overdue(
        None,
        "pending",
        date(2026, 10, 16),
    ) is False


def test_assignment_due_today_is_not_overdue():
    assert is_overdue(
        date(2026, 10, 16),
        "pending",
        date(2026, 10, 16),
    ) is False


def test_leap_year_deadline_calculation():
    assert calculate_days_remaining(
        date(2024, 3, 1),
        date(2024, 2, 28),
    ) == 2


def test_year_boundary_deadline_calculation():
    assert calculate_days_remaining(
        date(2027, 1, 1),
        date(2026, 12, 31),
    ) == 1


def test_in_progress_assignment_with_past_due_date_is_overdue():
    assert is_overdue(
        date(2026, 11, 5),
        "in_progress",
        date(2026, 11, 6),
    ) is True


def test_completed_assignment_due_today_is_not_overdue():
    assert is_overdue(
        date(2026, 11, 6),
        "completed",
        date(2026, 11, 6),
    ) is False
