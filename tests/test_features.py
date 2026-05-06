"""Tests for feature extractors."""

from src.features.contact_extractor import extract_contact
from src.features.skills_extractor import extract_skills


def test_extract_contact_finds_email():
    text = "Reach me at jane.doe@example.com for opportunities."
    assert extract_contact(text)["email"] == "jane.doe@example.com"


def test_extract_skills_finds_python():
    text = "5 years of Python and Django experience with PostgreSQL."
    skills = extract_skills(text)
    assert "python" in skills
    assert "django" in skills
    assert "postgresql" in skills


# TODO: tests for experience_extractor and education_extractor
