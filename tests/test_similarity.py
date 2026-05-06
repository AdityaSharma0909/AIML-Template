"""Tests for similarity scorers.

TODO: implement once tfidf_similarity and embedding_similarity are wired up.
"""

import pytest


@pytest.mark.skip("Implement after similarity module is filled in")
def test_tfidf_identical_text_is_one():
    from src.similarity import tfidf_similarity

    text = "python developer with django experience"
    assert tfidf_similarity(text, text) == pytest.approx(1.0)
