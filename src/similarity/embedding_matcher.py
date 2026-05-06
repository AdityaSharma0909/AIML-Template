"""Sentence-transformer based semantic similarity."""


def embedding_similarity(resume_text: str, jd_text: str, model_name: str | None = None) -> float:
    """Return semantic similarity in [0, 1] using sentence embeddings.

    TODO:
        - Lazy-load SentenceTransformer (default: all-MiniLM-L6-v2)
        - Encode both texts (truncate / chunk long resumes)
        - Compute cosine similarity
        - Cache the model at module level
    """
    raise NotImplementedError("Implement embedding similarity")
