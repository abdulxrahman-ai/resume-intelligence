import fitz


def extract_text_from_pdf(file_bytes: bytes) -> str:
    """
    Extract text from a PDF file.
    """
    if not file_bytes:
        raise ValueError("Empty PDF file received.")

    text_parts = []

    try:
        pdf_document = fitz.open(stream=file_bytes, filetype="pdf")
        for page in pdf_document:
            page_text = page.get_text("text")
            if page_text:
                text_parts.append(page_text)
        pdf_document.close()
    except Exception as exc:
        raise ValueError(f"Unable to read PDF file: {exc}") from exc

    extracted_text = "\n".join(text_parts).strip()

    if not extracted_text:
        raise ValueError("No readable text found in the PDF.")

    return extracted_text
