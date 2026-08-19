

import io


def extract_text(filename: str, content: bytes) -> str:
    lower = filename.lower()

    if lower.endswith(".txt"):
        return content.decode("utf-8", errors="ignore")

    if lower.endswith(".pdf"):
        import pdfplumber
        text_parts = []
        with pdfplumber.open(io.BytesIO(content)) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text() or ""
                text_parts.append(page_text)
        return "\n\n".join(text_parts)

    if lower.endswith(".docx"):
        import docx
        document = docx.Document(io.BytesIO(content))
        return "\n\n".join(p.text for p in document.paragraphs if p.text.strip())

    raise ValueError(f"Unsupported file type: {filename}. Use .txt, .pdf, or .docx")
