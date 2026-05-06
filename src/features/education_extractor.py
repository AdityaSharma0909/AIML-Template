"""Extract education entries from resume text."""


def extract_education(text: str) -> list[dict]:
    """Return a list of {degree, institution, field, year} dicts.

    TODO:
        - Detect the 'Education' section
        - Match degree keywords (Bachelor, Master, PhD, B.Tech, M.Tech…)
        - Use spaCy NER for ORG (institutions) and DATE (graduation year)
    """
    return []
