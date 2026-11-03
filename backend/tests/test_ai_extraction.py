import json
from unittest.mock import MagicMock, patch
from urllib.error import URLError

import pytest

from datetime import date

from fastapi.testclient import TestClient

from app.database import create_tables
from app.main import app

from app.services.ai_extraction_service import (
    AssignmentExtraction,
    extract_assignment_details,
)


def mock_ollama_response(response_data):
    """Create a mocked Ollama HTTP response."""
    mock_response = MagicMock()
    mock_response.__enter__.return_value = mock_response
    mock_response.read.return_value = json.dumps({
        "response": json.dumps(response_data)
    }).encode("utf-8")

    return mock_response


def test_successful_assignment_extraction():
    response_data = {
        "title": "Database Management Systems",
        "due_date": "2026-11-20",
        "requirements": [
            "Design an ER diagram",
            "Create five SQL queries",
        ],
    }

    with patch(
        "app.services.ai_extraction_service.urlopen",
        return_value=mock_ollama_response(response_data),
    ):
        result = extract_assignment_details(
            "Assignment: Database Management Systems"
        )

    assert isinstance(result, AssignmentExtraction)
    assert result.title == "Database Management Systems"
    assert result.due_date.isoformat() == "2026-11-20"
    assert len(result.requirements) == 2


def test_extraction_with_missing_due_date():
    response_data = {
        "title": "Introduction to Cybersecurity",
        "due_date": None,
        "requirements": ["Research network attacks"],
    }

    with patch(
        "app.services.ai_extraction_service.urlopen",
        return_value=mock_ollama_response(response_data),
    ):
        result = extract_assignment_details(
            "Assignment: Introduction to Cybersecurity"
        )

    assert result.due_date is None
    assert result.title == "Introduction to Cybersecurity"


def test_empty_document_text():
    with pytest.raises(ValueError, match="cannot be empty"):
        extract_assignment_details("   ")


def test_invalid_json_response():
    mock_response = MagicMock()
    mock_response.__enter__.return_value = mock_response
    mock_response.read.return_value = b'{"response": "not valid json"}'

    with patch(
        "app.services.ai_extraction_service.urlopen",
        return_value=mock_response,
    ):
        with pytest.raises(ValueError, match="invalid JSON"):
            extract_assignment_details("Some assignment text")


def test_invalid_extracted_data():
    response_data = {
        "title": "Database Assignment",
        "due_date": "not-a-date",
        "requirements": [],
    }

    with patch(
        "app.services.ai_extraction_service.urlopen",
        return_value=mock_ollama_response(response_data),
    ):
        with pytest.raises(ValueError, match="failed validation"):
            extract_assignment_details("Some assignment text")


def test_ollama_connection_failure():
    with patch(
        "app.services.ai_extraction_service.urlopen",
        side_effect=URLError("Connection refused"),
    ):
        with pytest.raises(RuntimeError, match="communicate with Ollama"):
            extract_assignment_details("Some assignment text")


def test_invalid_response_structure():
    response_data = {
        "title": "Database Assignment",
        "due_date": "2026-11-20",
        "requirements": [],
        "unexpected_field": "unexpected",
    }

    with patch(
        "app.services.ai_extraction_service.urlopen",
        return_value=mock_ollama_response(response_data),
    ):
        with pytest.raises(ValueError, match="failed validation"):
            extract_assignment_details("Some assignment text")

@pytest.fixture
def api_client(tmp_path, monkeypatch):
    import app.database as database

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
