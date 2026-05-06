"""PDF resume parser. TODO: implement using PyMuPDF or pdfplumber."""


def parse_pdf(file_path: str) -> str:
    """Extract raw text from a PDF resume.

    TODO:
        - Open the PDF with `fitz` (PyMuPDF)
        - Iterate pages, concatenate `page.get_text()`
        - Handle two-column layouts and tables
        - Return raw text (cleaning happens in `text_cleaner`)
    """
    raise NotImplementedError("Implement PDF parsing — see TODO in pdf_parser.py")
