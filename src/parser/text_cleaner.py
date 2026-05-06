"""Normalize extracted resume text."""

import re


def clean_text(text: str) -> str:
    """Strip control chars, collapse whitespace, normalize bullets.

    TODO (extend):
        - Remove headers/footers, page numbers
        - Fix hyphenation across line breaks
        - Normalize unicode (NFKC)
    """
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", " ", text)
    text = re.sub(r"[•·●◦▪]", "-", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()
