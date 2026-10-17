
from datetime import date
import pytest
from backend.app.services.assignment_service import calculate_days_remaining

from app.services.assignment_service import (
    calculate_days_remaining,
    validate_assignment_title,
)

def test_future_deadline():
    result = calculate_days_remaining(
        date(2026, 10, 20),
        date(2026, 10, 16),
    )
    assert result == 4


def test_overdue_assignment():
    result = calculate_days_remaining(
        date(2026, 10, 14),
        date(2026, 10, 16),
    )
    assert result == -2


def test_deadline_is_today():
    result = calculate_days_remaining(
        date(2026, 10, 16),
        date(2026, 10, 16),
    )
    assert result == 0

def test_title_is_trimmed():
    assert validate_assignment_title("  Finish project  ") == "Finish project"


def test_empty_title_is_rejected():
    with pytest.raises(ValueError, match="cannot be empty"):
        validate_assignment_title("")


def test_whitespace_title_is_rejected():
    with pytest.raises(ValueError, match="cannot be empty"):
        validate_assignment_title("   ")
