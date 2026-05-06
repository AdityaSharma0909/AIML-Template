"""Extract work-experience entries from resume text."""


def extract_experience(text: str) -> list[dict]:
    """Return a list of {company, role, start, end, description} dicts.

    TODO:
        - Section the resume into 'Experience' / 'Work History'
        - Use spaCy NER (ORG, DATE) plus regex for date ranges
        - Compute total years of experience
        - Handle 'Present' / 'Current' end dates
    """
    return []
