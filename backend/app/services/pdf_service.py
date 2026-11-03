from io import BytesIO

from pypdf import PdfReader
from pypdf.errors import PdfReadError


def extract_pdf_text(pdf_bytes: bytes) -> str:
    """
    Extract readable text from PDF file bytes.

    Raises:
        ValueError: If the PDF is empty, malformed, encrypted,
                    or contains no extractable text.
    """
    if not pdf_bytes:
        raise ValueError("PDF file is empty.")

    try:
        reader = PdfReader(BytesIO(pdf_bytes), strict=True)

        if reader.is_encrypted:
            raise ValueError("Encrypted PDF files are not supported.")

        extracted_pages = []

        for page in reader.pages:
            page_text = page.extract_text() or ""

            if page_text.strip():
                extracted_pages.append(page_text.strip())

    except PdfReadError as exc:
        raise ValueError("Invalid or malformed PDF file.") from exc
    except (EOFError, OSError) as exc:
        raise ValueError("Unable to read PDF file.") from exc

    extracted_text = "\n\n".join(extracted_pages).strip()

    if not extracted_text:
        raise ValueError("PDF contains no extractable text.")

    return extracted_text
