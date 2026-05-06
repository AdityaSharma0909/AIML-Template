"""Tests for resume parsers."""

from src.parser.text_cleaner import clean_text


def test_clean_text_collapses_whitespace():
    assert clean_text("hello    world") == "hello world"


def test_clean_text_normalizes_bullets():
    assert "-" in clean_text("• item one")


# TODO: add tests for parse_pdf, parse_docx using sample fixtures
