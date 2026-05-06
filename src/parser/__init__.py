from src.parser.pdf_parser import parse_pdf
from src.parser.docx_parser import parse_docx
from src.parser.text_cleaner import clean_text

__all__ = ["parse_pdf", "parse_docx", "clean_text", "parse_resume"]


def parse_resume(file_path: str) -> str:
    """Dispatch to the right parser based on file extension."""
    path = file_path.lower()
    if path.endswith(".pdf"):
        return clean_text(parse_pdf(file_path))
    if path.endswith(".docx"):
        return clean_text(parse_docx(file_path))
    if path.endswith(".txt"):
        with open(file_path, encoding="utf-8") as f:
            return clean_text(f.read())
    raise ValueError(f"Unsupported file format: {file_path}")
