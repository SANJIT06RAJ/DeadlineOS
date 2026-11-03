
from io import BytesIO

import pytest
from fastapi.testclient import TestClient
from pypdf import PdfWriter
from pypdf.generic import (
    DecodedStreamObject,
    DictionaryObject,
    NameObject,
)

from app.database import create_tables
from app.main import app


MAX_PDF_SIZE = 10 * 1024 * 1024


@pytest.fixture
def client(tmp_path, monkeypatch):
    import app.database as database

    test_db = tmp_path / "test_deadlineos.db"
    monkeypatch.setattr(database, "DATABASE_PATH", test_db)

    create_tables()

    with TestClient(app) as test_client:
        yield test_client


def create_text_pdf():
    """Generate a small PDF containing extractable text."""
    writer = PdfWriter()
    page = writer.add_blank_page(width=612, height=792)

    font = DictionaryObject({
        NameObject("/Type"): NameObject("/Font"),
        NameObject("/Subtype"): NameObject("/Type1"),
        NameObject("/BaseFont"): NameObject("/Helvetica"),
    })

    page[NameObject("/Resources")] = DictionaryObject({
        NameObject("/Font"): DictionaryObject({
            NameObject("/F1"): font,
        }),
    })

    content = DecodedStreamObject()
    content.set_data(
        b"BT /F1 12 Tf 72 720 Td (DeadlineOS PDF test) Tj ET"
    )
    page[NameObject("/Contents")] = content

    output = BytesIO()
    writer.write(output)

    return output.getvalue()


def test_preview_valid_pdf(client):
    pdf_bytes = create_text_pdf()

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
    assert "DeadlineOS PDF test" in data["text"]
    assert data["character_count"] == len(data["text"])

    # Previewing a PDF must not create an assignment.
    assert client.get("/assignments").json() == []


def test_reject_non_pdf_filename(client):
    response = client.post(
        "/documents/preview",
        files={
            "file": (
                "assignment.txt",
                b"%PDF-1.4 test",
                "application/pdf",
            )
        },
    )

    assert response.status_code == 415
    assert response.json()["detail"] == "Only PDF files are supported."


def test_reject_invalid_pdf_signature(client):
    response = client.post(
        "/documents/preview",
        files={
            "file": (
                "assignment.pdf",
                b"This is not a PDF",
                "application/pdf",
            )
        },
    )

    assert response.status_code == 415
    assert response.json()["detail"] == (
        "The uploaded file is not a valid PDF."
    )


def test_reject_empty_upload(client):
    response = client.post(
        "/documents/preview",
        files={
            "file": (
                "empty.pdf",
                b"",
                "application/pdf",
            )
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "The uploaded file is empty."


def test_reject_oversized_pdf(client):
    oversized_pdf = b"%PDF-" + b"A" * MAX_PDF_SIZE

    response = client.post(
        "/documents/preview",
        files={
            "file": (
                "large.pdf",
                oversized_pdf,
                "application/pdf",
            )
        },
    )

    assert response.status_code == 413
    assert response.json()["detail"] == (
        "PDF file exceeds the 10 MB size limit."
    )


def test_reject_malformed_pdf(client):
    response = client.post(
        "/documents/preview",
        files={
            "file": (
                "malformed.pdf",
                b"%PDF-this is malformed",
                "application/pdf",
            )
        },
    )

    assert response.status_code == 400


def test_reject_pdf_without_extractable_text(client):
    writer = PdfWriter()
    writer.add_blank_page(width=612, height=792)

    output = BytesIO()
    writer.write(output)

    response = client.post(
        "/documents/preview",
        files={
            "file": (
                "blank.pdf",
                output.getvalue(),
                "application/pdf",
            )
        },
    )

    assert response.status_code == 400
    assert "no extractable text" in response.json()["detail"]
