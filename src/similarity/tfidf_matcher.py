"""TF-IDF cosine similarity between a resume and a job description."""


def tfidf_similarity(resume_text: str, jd_text: str) -> float:
    """Return a cosine-similarity score in [0, 1].

    TODO:
        - Fit a TfidfVectorizer on [resume_text, jd_text]
        - Compute cosine_similarity between the two vectors
        - Consider using ngram_range=(1, 2) and stop_words="english"
    """
    raise NotImplementedError("Implement TF-IDF similarity")
