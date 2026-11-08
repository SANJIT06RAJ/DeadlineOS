from io import BytesIO

from pypdf import PdfReader
from pypdf.errors import PdfReadError

MAX_PDF_PAGES = 100
MAX_EXTRACTED_TEXT_CHARS = 200_000


def extract_pdf_text(pdf_bytes: bytes) -> str:
    """
    Extract readable text from PDF file bytes.

    Raises:
        ValueError: If the PDF is invalid, encrypted, empty,
                    or exceeds the processing limits.
    """
    if not pdf_bytes:
        raise ValueError("PDF file is empty.")

    try:
        reader = PdfReader(BytesIO(pdf_bytes), strict=True)

        if reader.is_encrypted:
            raise ValueError("Encrypted PDF files are not supported.")

        if len(reader.pages) > MAX_PDF_PAGES:
            raise ValueError(f"PDF exceeds the {MAX_PDF_PAGES}-page limit.")

        extracted_pages = []
        total_chars = 0

        for page in reader.pages:
            page_text = (page.extract_text() or "").strip()

            if page_text:
                separator_length = 2 if extracted_pages else 0
                total_chars += separator_length + len(page_text)

                if total_chars > MAX_EXTRACTED_TEXT_CHARS:
                    raise ValueError(
                        "PDF extracted text exceeds the "
                        f"{MAX_EXTRACTED_TEXT_CHARS}-character limit."
                    )

                extracted_pages.append(page_text)

    except PdfReadError as exc:
        raise ValueError("Invalid or malformed PDF file.") from exc
    except (EOFError, OSError) as exc:
        raise ValueError("Unable to read PDF file.") from exc

    extracted_text = "\n\n".join(extracted_pages).strip()

    if not extracted_text:
        raise ValueError("PDF contains no extractable text.")

    return extracted_text
