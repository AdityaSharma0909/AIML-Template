"""Extract contact information (email, phone, LinkedIn, name)."""

import re

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
PHONE_RE = re.compile(r"(?:\+?\d{1,3}[\s-]?)?\(?\d{3,4}\)?[\s-]?\d{3,4}[\s-]?\d{3,4}")
LINKEDIN_RE = re.compile(r"linkedin\.com/in/[a-zA-Z0-9_-]+", re.IGNORECASE)


def extract_contact(text: str) -> dict:
    """Return {name, email, phone, linkedin}.

    TODO: extract `name` using spaCy NER (PERSON) on the first ~5 lines.
    """
    email = EMAIL_RE.search(text)
    phone = PHONE_RE.search(text)
    linkedin = LINKEDIN_RE.search(text)
    return {
        "name": None,
        "email": email.group(0) if email else None,
        "phone": phone.group(0) if phone else None,
        "linkedin": linkedin.group(0) if linkedin else None,
    }
