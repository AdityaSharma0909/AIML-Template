"""Composite candidate-vs-JD scorer."""

from dataclasses import dataclass

from src.features import CandidateProfile


@dataclass
class ScoreBreakdown:
    skills: float
    experience: float
    education: float
    semantic: float
    total: float


DEFAULT_WEIGHTS = {
    "skills": 0.45,
    "experience": 0.30,
    "education": 0.15,
    "semantic": 0.10,
}


def score_candidate(
    profile: CandidateProfile,
    jd_text: str,
    jd_required_skills: list[str] | None = None,
    weights: dict[str, float] | None = None,
) -> ScoreBreakdown:
    """Compute a composite score in [0, 1].

    TODO:
        - skills: jaccard / weighted overlap between profile.skills and jd_required_skills
        - experience: bucketize total_experience_years vs JD requirement
        - education: degree-level match (Bachelor/Master/PhD ladder)
        - semantic: hybrid_similarity(profile.raw_text, jd_text)
        - total: weighted sum, clipped to [0, 1]
    """
    raise NotImplementedError("Implement score_candidate")
