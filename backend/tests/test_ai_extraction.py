import json
from datetime import date
from unittest.mock import MagicMock, patch
from urllib.error import URLError

import pytest
from app.database import create_tables
from app.main import app
from app.services.ai_extraction_service import (
    MAX_OLLAMA_RESPONSE_SIZE,
    AssignmentExtraction,
    extract_assignment_details,
)
from fastapi.testclient import TestClient


def mock_ollama_response(response_data):
    """Create a mocked Ollama HTTP response."""
    mock_response = MagicMock()
    mock_response.__enter__.return_value = mock_response
    mock_response.read.return_value = json.dumps(
        {"response": json.dumps(response_data)}
    ).encode("utf-8")

    return mock_response


def test_successful_assignment_extraction():
    response_data = {
        "title": "Database Management Systems",
        "due_date": "2026-11-20",
        "requirements": [
            "Design an ER diagram",
            "Create five SQL queries",
        ],
        "title_evidence": "Assignment: Database Management Systems",
        "due_date_evidence": "Due date: 20 November 2026",
        "requirement_evidence": [
            "Design an ER diagram",
            "Create five SQL queries",
        ],
    }

    with patch(
        "app.services.ai_extraction_service.urlopen",
        return_value=mock_ollama_response(response_data),
    ):
        result = extract_assignment_details(
            """
            Assignment: Database Management Systems.
            Due date: 20 November 2026.
            Design an ER diagram.
            Create five SQL queries.
            """
        )

    assert isinstance(result, AssignmentExtraction)
    assert result.title == "Database Management Systems"
    assert result.due_date == date(2026, 11, 20)
    assert result.requirements == [
        "Design an ER diagram",
        "Create five SQL queries",
    ]


def test_extraction_with_missing_due_date():
    response_data = {
        "title": "Introduction to Cybersecurity",
        "due_date": None,
        "requirements": ["Research network attacks"],
        "title_evidence": "Assignment: Introduction to Cybersecurity",
        "due_date_evidence": None,
        "requirement_evidence": ["Research network attacks"],
    }

    with patch(
        "app.services.ai_extraction_service.urlopen",
        return_value=mock_ollama_response(response_data),
    ):
        result = extract_assignment_details(
            """
            Assignment: Introduction to Cybersecurity.
            Research network attacks.
            """
        )

    assert result.due_date is None
    assert result.title == "Introduction to Cybersecurity"
    assert result.requirements == ["Research network attacks"]


def test_unsupported_due_date_is_discarded():
    response_data = {
        "title": "Database Management Systems",
        "due_date": "2026-11-20",
        "requirements": ["Create five SQL queries"],
        "title_evidence": "Assignment: Database Management Systems",
        "due_date_evidence": "Due date: 20 November 2026",
        "requirement_evidence": ["Create five SQL queries"],
    }

    with patch(
        "app.services.ai_extraction_service.urlopen",
        return_value=mock_ollama_response(response_data),
    ):
        result = extract_assignment_details(
            """
            Assignment: Database Management Systems.
            Create five SQL queries.
            Submission date will be announced later.
            """
        )

    assert result.title == "Database Management Systems"
    assert result.due_date is None
    assert result.requirements == ["Create five SQL queries"]


def test_unsupported_requirement_is_discarded():
    response_data = {
        "title": "Database Assignment",
        "due_date": None,
        "requirements": [
            "Create an ER diagram",
            "Build a mobile application",
        ],
        "title_evidence": "Assignment: Database Assignment",
        "due_date_evidence": None,
        "requirement_evidence": [
            "Create an ER diagram",
            "Submit a mobile application",
        ],
    }

    with patch(
        "app.services.ai_extraction_service.urlopen",
        return_value=mock_ollama_response(response_data),
    ):
        result = extract_assignment_details(
            """
            Assignment: Database Assignment.
            Create an ER diagram.
            """
        )

    assert result.requirements == ["Create an ER diagram"]


def test_unsupported_title_is_discarded():
    response_data = {
        "title": "Advanced Artificial Intelligence Project",
        "due_date": None,
        "requirements": [],
        "title_evidence": "Advanced Artificial Intelligence Project",
        "due_date_evidence": None,
        "requirement_evidence": [],
    }

    with patch(
        "app.services.ai_extraction_service.urlopen",
        return_value=mock_ollama_response(response_data),
    ):
        result = extract_assignment_details(
            "Please read the following course announcement."
        )

    assert result.title is None


def test_ambiguous_due_date_is_not_extracted():
    response_data = {
        "title": "Database Assignment",
        "due_date": None,
        "requirements": ["Create an ER diagram"],
        "title_evidence": "Assignment: Database Assignment",
        "due_date_evidence": None,
        "requirement_evidence": ["Create an ER diagram"],
    }

    with patch(
        "app.services.ai_extraction_service.urlopen",
        return_value=mock_ollama_response(response_data),
    ):
        result = extract_assignment_details(
            """
            Assignment: Database Assignment.
            Submit next Friday.
            Create an ER diagram.
            """
        )

    assert result.due_date is None


def test_empty_document_text():
    with pytest.raises(ValueError, match="cannot be empty"):
        extract_assignment_details("   ")


def test_invalid_json_response():
    mock_response = MagicMock()
    mock_response.__enter__.return_value = mock_response
    mock_response.read.return_value = b'{"response": "not valid json"}'

    with (
        patch(
            "app.services.ai_extraction_service.urlopen",
            return_value=mock_response,
        ),
        pytest.raises(ValueError, match="invalid JSON"),
    ):
        extract_assignment_details("Some assignment text")


def test_invalid_extracted_data():
    response_data = {
        "title": "Database Assignment",
        "due_date": "not-a-date",
        "requirements": [],
    }

    with (
        patch(
            "app.services.ai_extraction_service.urlopen",
            return_value=mock_ollama_response(response_data),
        ),
        pytest.raises(ValueError, match="failed validation"),
    ):
        extract_assignment_details("Some assignment text")


def test_ollama_connection_failure():
    with (
        patch(
            "app.services.ai_extraction_service.urlopen",
            side_effect=URLError("Connection refused"),
        ),
        pytest.raises(RuntimeError, match="communicate with Ollama"),
    ):
        extract_assignment_details("Some assignment text")


def test_ollama_response_exceeding_size_limit():
    mock_response = MagicMock()
    mock_response.__enter__.return_value = mock_response
    mock_response.read.return_value = b"x" * (MAX_OLLAMA_RESPONSE_SIZE + 1)

    with (
        patch(
            "app.services.ai_extraction_service.urlopen",
            return_value=mock_response,
        ),
        pytest.raises(
            RuntimeError,
            match="exceeded the 1 MB size limit",
        ),
    ):
        extract_assignment_details("Some assignment text")

    mock_response.read.assert_called_once_with(MAX_OLLAMA_RESPONSE_SIZE + 1)


def test_invalid_response_structure():
    response_data = {
        "title": "Database Assignment",
        "due_date": "2026-11-20",
        "requirements": [],
        "unexpected_field": "unexpected",
    }

    with (
        patch(
            "app.services.ai_extraction_service.urlopen",
            return_value=mock_ollama_response(response_data),
        ),
        pytest.raises(ValueError, match="failed validation"),
    ):
        extract_assignment_details("Some assignment text")


@pytest.fixture
def api_client(tmp_path, monkeypatch):
    from app import database

    test_db = tmp_path / "test_deadlineos.db"
    monkeypatch.setattr(database, "DATABASE_PATH", test_db)

    create_tables()

    with TestClient(app) as test_client:
        yield test_client


def test_extract_document_successfully(api_client, monkeypatch):
    result = AssignmentExtraction(
        title="Database Management Systems",
        due_date=date(2026, 11, 20),
        requirements=[
            "Design an ER diagram",
            "Create five SQL queries",
        ],
    )

    monkeypatch.setattr(
        "app.main.extract_assignment_details",
        lambda document_text: result,
    )

    response = api_client.post(
        "/documents/extract",
        json={"document_text": "Database assignment details"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "title": "Database Management Systems",
        "due_date": "2026-11-20",
        "requirements": [
            "Design an ER diagram",
            "Create five SQL queries",
        ],
    }

    # AI extraction must not save an assignment.
    assert api_client.get("/assignments").json() == []


def test_extract_document_without_due_date(api_client, monkeypatch):
    result = AssignmentExtraction(
        title="Introduction to Cybersecurity",
        due_date=None,
        requirements=["Research network attacks"],
    )

    monkeypatch.setattr(
        "app.main.extract_assignment_details",
        lambda document_text: result,
    )

    response = api_client.post(
        "/documents/extract",
        json={"document_text": "Cybersecurity assignment"},
    )

    assert response.status_code == 200
    assert response.json()["due_date"] is None


def test_extract_document_rejects_empty_text(api_client):
    response = api_client.post(
        "/documents/extract",
        json={"document_text": "   "},
    )

    assert response.status_code == 422


def test_extract_document_handles_invalid_ai_response(
    api_client,
    monkeypatch,
):
    def raise_validation_error(document_text):
        raise ValueError("Extracted assignment data failed validation.")

    monkeypatch.setattr(
        "app.main.extract_assignment_details",
        raise_validation_error,
    )

    response = api_client.post(
        "/documents/extract",
        json={"document_text": "Assignment details"},
    )

    assert response.status_code == 422


def test_extract_document_handles_ollama_unavailable(
    api_client,
    monkeypatch,
):
    def raise_connection_error(document_text):
        raise RuntimeError("Could not communicate with Ollama.")

    monkeypatch.setattr(
        "app.main.extract_assignment_details",
        raise_connection_error,
    )

    response = api_client.post(
        "/documents/extract",
        json={"document_text": "Assignment details"},
    )

    assert response.status_code == 503
    assert "Could not communicate with Ollama" in response.json()["detail"]


def test_requirement_with_unrelated_existing_evidence_is_discarded():
    response_data = {
        "title": "Database Assignment",
        "due_date": None,
        "requirements": ["Build a mobile application"],
        "title_evidence": "Assignment: Database Assignment",
        "due_date_evidence": None,
        "requirement_evidence": ["Create an ER diagram"],
    }

    with patch(
        "app.services.ai_extraction_service.urlopen",
        return_value=mock_ollama_response(response_data),
    ):
        result = extract_assignment_details(
            """
            Assignment: Database Assignment.
            Create an ER diagram.
            """
        )

    assert result.requirements == []


def test_unsupported_title_evidence_is_discarded():
    response_data = {
        "title": "Advanced Artificial Intelligence Project",
        "due_date": None,
        "requirements": [],
        "title_evidence": "Assignment: Database Management Systems",
        "due_date_evidence": None,
        "requirement_evidence": [],
    }

    with patch(
        "app.services.ai_extraction_service.urlopen",
        return_value=mock_ollama_response(response_data),
    ):
        result = extract_assignment_details("Assignment: Database Management Systems")

    assert result.title is None


def test_unsupported_due_date_evidence_is_discarded():
    response_data = {
        "title": "Database Assignment",
        "due_date": "2026-11-20",
        "requirements": [],
        "title_evidence": "Assignment: Database Assignment",
        "due_date_evidence": "Due date: 21 November 2026",
        "requirement_evidence": [],
    }

    with patch(
        "app.services.ai_extraction_service.urlopen",
        return_value=mock_ollama_response(response_data),
    ):
        result = extract_assignment_details(
            """
            Assignment: Database Assignment.
            Due date: 21 November 2026.
            """
        )

    assert result.due_date is None


def test_event_date_is_not_accepted_as_due_date():
    response_data = {
        "title": "Database Assignment",
        "due_date": "2025-12-25",
        "requirements": [],
        "title_evidence": "Assignment: Database Assignment",
        "due_date_evidence": "EVENT DATE: 25 December 2025",
        "requirement_evidence": [],
    }

    with patch(
        "app.services.ai_extraction_service.urlopen",
        return_value=mock_ollama_response(response_data),
    ):
        result = extract_assignment_details(
            """
            Assignment: Database Assignment.
            EVENT DATE: 25 December 2025.
            SUBMISSION DEADLINE: 31 December 2025.
            """
        )

    assert result.due_date is None


def test_event_date_is_rejected_when_evidence_contains_multiple_dates():
    response_data = {
        "title": "Database Assignment",
        "due_date": "2025-12-25",
        "requirements": [],
        "title_evidence": "Assignment: Database Assignment",
        "due_date_evidence": (
            "EVENT DATE: 25 December 2025.\nSUBMISSION DEADLINE: 31 December 2025."
        ),
        "requirement_evidence": [],
    }

    with patch(
        "app.services.ai_extraction_service.urlopen",
        return_value=mock_ollama_response(response_data),
    ):
        result = extract_assignment_details(
            """
            Assignment: Database Assignment.
            EVENT DATE: 25 December 2025.
            SUBMISSION DEADLINE: 31 December 2025.
            """
        )

    assert result.due_date is None
