from io import BytesIO

import pytest
from pypdf import PdfWriter
from pypdf.generic import (
    DecodedStreamObject,
    DictionaryObject,
    NameObject,
)

import app.services.pdf_service as pdf_service
from app.services.pdf_service import extract_pdf_text


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


def create_blank_pdf():
    """Generate a valid PDF without extractable text."""
    writer = PdfWriter()
    writer.add_blank_page(width=612, height=792)

    output = BytesIO()
    writer.write(output)

    return output.getvalue()


def test_extracts_text_from_valid_pdf():
    pdf_bytes = create_text_pdf()

    result = extract_pdf_text(pdf_bytes)

    assert "DeadlineOS PDF test" in result


def test_rejects_empty_pdf_bytes():
    with pytest.raises(ValueError, match="PDF file is empty"):
        extract_pdf_text(b"")


def test_rejects_malformed_pdf():
    with pytest.raises(ValueError, match="Invalid or malformed PDF"):
        extract_pdf_text(b"This is not a PDF file")


def test_rejects_pdf_without_extractable_text():
    pdf_bytes = create_blank_pdf()

    with pytest.raises(ValueError, match="no extractable text"):
        extract_pdf_text(pdf_bytes)


def test_rejects_encrypted_pdf():
    writer = PdfWriter()
    writer.add_blank_page(width=612, height=792)
    writer.encrypt("test-password")

    output = BytesIO()
    writer.write(output)

    with pytest.raises(ValueError, match="Encrypted PDF"):
        extract_pdf_text(output.getvalue())


def test_rejects_pdf_exceeding_page_limit():
    writer = PdfWriter()

    for _ in range(pdf_service.MAX_PDF_PAGES + 1):
        writer.add_blank_page(width=612, height=792)

    output = BytesIO()
    writer.write(output)

    with pytest.raises(ValueError, match="page limit"):
        extract_pdf_text(output.getvalue())


def test_rejects_pdf_exceeding_extracted_text_limit(monkeypatch):
    class FakePage:
        def extract_text(self):
            return "A" * (pdf_service.MAX_EXTRACTED_TEXT_CHARS + 1)

    class FakeReader:
        is_encrypted = False
        pages = [FakePage()]

    monkeypatch.setattr(
        pdf_service,
        "PdfReader",
        lambda *args, **kwargs: FakeReader(),
    )

    with pytest.raises(ValueError, match="character limit"):
        extract_pdf_text(b"%PDF-test")
