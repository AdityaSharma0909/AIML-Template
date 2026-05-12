"""PDF resume parser."""

import fitz


def parse_pdf(file_path: str) -> str:
    """Extract raw text from a PDF resume."""
    text_blocks: list[str] = []
    with fitz.open(file_path) as pdf:
        for page in pdf:
            page_text = page.get_text()
            if page_text:
                text_blocks.append(page_text)
    return "\n".join(text_blocks)
