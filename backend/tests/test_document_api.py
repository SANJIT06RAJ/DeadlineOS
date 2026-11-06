from io import BytesIO

from fastapi.testclient import TestClient
from pypdf import PdfWriter

from app.main import app


def create_text_pdf():
    """Generate a valid PDF containing extractable text."""
    writer = PdfWriter()
    writer.add_blank_page(width=612, height=792)

    output = BytesIO()
    writer.write(output)

    return output.getvalue()


def test_preview_rejects_missing_file():
    with TestClient(app) as client:
        response = client.post("/documents/preview")

    assert response.status_code == 422


def test_preview_rejects_non_pdf_file():
    with TestClient(app) as client:
        response = client.post(
            "/documents/preview",
            files={"file": ("document.txt", b"Not a PDF", "text/plain")},
        )

    assert response.status_code == 415


def test_preview_rejects_empty_file():
    with TestClient(app) as client:
        response = client.post(
            "/documents/preview",
            files={"file": ("empty.pdf", b"", "application/pdf")},
        )

    assert response.status_code == 400


def test_preview_rejects_invalid_pdf_signature():
    with TestClient(app) as client:
        response = client.post(
            "/documents/preview",
            files={
                "file": (
                    "invalid.pdf",
                    b"This is not a PDF",
                    "application/pdf",
                )
            },
        )

    assert response.status_code == 415


def test_preview_rejects_oversized_pdf():
    oversized_content = b"%PDF-" + (
        b"A" * (10 * 1024 * 1024)
    )

    with TestClient(app) as client:
        response = client.post(
            "/documents/preview",
            files={
                "file": (
                    "large.pdf",
                    oversized_content,
                    "application/pdf",
                )
            },
        )

    assert response.status_code == 413


def test_preview_rejects_pdf_without_extractable_text():
    pdf_bytes = create_text_pdf()

    with TestClient(app) as client:
        response = client.post(
            "/documents/preview",
            files={
                "file": (
                    "blank.pdf",
                    pdf_bytes,
                    "application/pdf",
                )
            },
        )

    assert response.status_code == 400


def test_preview_returns_extracted_text(monkeypatch):
    from app import main

    monkeypatch.setattr(
        main,
        "extract_pdf_text",
        lambda pdf_bytes: "Database assignment requirements",
    )

    pdf_bytes = b"%PDF-test-content"

    with TestClient(app) as client:
        response = client.post(
            "/documents/preview",
            files={
                "file": (
                    "assignment.pdf",
                    pdf_bytes,
                    "application/pdf",
                )
            },
        )

    assert response.status_code == 200

    data = response.json()

    assert data["filename"] == "assignment.pdf"
    assert data["text"] == "Database assignment requirements"
    assert data["character_count"] == len(
        "Database assignment requirements"
    )
