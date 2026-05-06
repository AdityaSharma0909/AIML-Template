"""Combine TF-IDF (lexical) and embedding (semantic) similarity."""

from src.similarity.embedding_matcher import embedding_similarity
from src.similarity.tfidf_matcher import tfidf_similarity


def hybrid_similarity(
    resume_text: str,
    jd_text: str,
    tfidf_weight: float = 0.4,
    embedding_weight: float = 0.6,
) -> float:
    """Weighted combination of lexical + semantic similarity."""
    lex = tfidf_similarity(resume_text, jd_text)
    sem = embedding_similarity(resume_text, jd_text)
    return tfidf_weight * lex + embedding_weight * sem
