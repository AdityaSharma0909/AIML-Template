"""Rank a batch of candidates against a single job description."""

from src.features import CandidateProfile
from src.ranking.scorer import ScoreBreakdown, score_candidate


def rank_candidates(
    profiles: list[CandidateProfile],
    jd_text: str,
    jd_required_skills: list[str] | None = None,
    top_k: int | None = None,
) -> list[tuple[CandidateProfile, ScoreBreakdown]]:
    """Score every candidate and return them sorted by total score (desc)."""
    scored = [(p, score_candidate(p, jd_text, jd_required_skills)) for p in profiles]
    scored.sort(key=lambda x: x[1].total, reverse=True)
    return scored[:top_k] if top_k else scored
