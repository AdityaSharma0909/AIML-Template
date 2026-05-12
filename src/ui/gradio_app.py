import os
import re

import gradio as gr
import pandas as pd

from src.parser import parse_resume
from src.parser.text_cleaner import clean_text
from src.similarity.embedding_matcher import embedding_similarity
from src.similarity.tfidf_matcher import tfidf_similarity
from src.ranking.scorer import score_candidate
from src.features import extract_features

programming_languages = [
    "python", "java", "c", "c++", "javascript", "html", "css",
    "sql", "php", "ruby", "go", "kotlin", "swift"
]

skills = [
    "machine learning", "deep learning", "nlp", "natural language processing",
    "data analysis", "pandas", "numpy", "scikit-learn", "tensorflow",
    "pytorch", "fastapi", "flask", "django", "react", "node.js",
    "git", "docker", "aws", "mysql", "postgresql", "mongodb",
    "power bi", "tableau", "excel"
]


def extract_items(text: str, items: list[str]) -> list[str]:
    found = []
    for item in items:
        pattern = r"\b" + re.escape(item) + r"\b"
        if re.search(pattern, text):
            found.append(item)
    return found


def overlap_score(resume_items: list[str], jd_items: list[str]) -> float:
    if len(jd_items) == 0:
        return 0.0
    return len(set(resume_items) & set(jd_items)) / len(set(jd_items))


def extract_experience_score(text: str) -> float:
    patterns = [
        r"(\d+)\+?\s*years",
        r"(\d+)\+?\s*year",
        r"(\d+)\+?\s*yrs",
    ]

    years: list[int] = []
    for pattern in patterns:
        for match in re.findall(pattern, text):
            years.append(int(match))

    if not years:
        return 0.3

    max_years = max(years)
    if max_years >= 5:
        return 1.0
    if max_years >= 3:
        return 0.8
    if max_years >= 1:
        return 0.6
    return 0.3


def rank_bulk_resumes(resume_files, job_description: str):
    if not resume_files:
        return pd.DataFrame({"Error": ["Please upload at least one resume."]})

    if not job_description.strip():
        return pd.DataFrame({"Error": ["Please enter a job description."]})

    clean_jd = clean_text(job_description)
    jd_skills = extract_items(clean_jd, skills)
    jd_languages = extract_items(clean_jd, programming_languages)

    resume_data: list[dict] = []
    for file in resume_files:
        file_path = file.name
        raw_text = parse_resume(file_path)
        clean_resume = clean_text(raw_text)
        if not clean_resume:
            continue

        profile = extract_features(clean_resume)
        resume_skills = extract_items(clean_resume, skills)
        resume_languages = extract_items(clean_resume, programming_languages)

        skill_score = overlap_score(resume_skills, jd_skills)
        language_score = overlap_score(resume_languages, jd_languages)
        experience_score = extract_experience_score(clean_resume)
        keyword_score = tfidf_similarity(clean_resume, clean_jd)
        semantic_score = embedding_similarity(clean_resume, clean_jd)
        scored = score_candidate(profile, clean_jd)

        final_score = (
            0.25 * skill_score
            + 0.25 * language_score
            + 0.20 * semantic_score
            + 0.15 * keyword_score
            + 0.15 * experience_score
        )

        if final_score >= 0.85:
            recommendation = "Excellent Match"
        elif final_score >= 0.70:
            recommendation = "Good Match"
        elif final_score >= 0.50:
            recommendation = "Moderate Match"
        else:
            recommendation = "Low Match"

        resume_data.append({
            "Resume Name": os.path.basename(file_path),
            "Final Score (%)": round(final_score * 100, 2),
            "Skill Score (%)": round(skill_score * 100, 2),
            "Language Score (%)": round(language_score * 100, 2),
            "Semantic Score (%)": round(semantic_score * 100, 2),
            "Keyword Score (%)": round(keyword_score * 100, 2),
            "Experience Score (%)": round(experience_score * 100, 2),
            "Extracted Skills": ", ".join(sorted(profile.skills)),
            "Recommendation": recommendation,
            "Candidate Score": round(scored.total * 100, 2),
        })

    if not resume_data:
        return pd.DataFrame({"Error": ["No valid resume text found."]})

    return pd.DataFrame(resume_data)


if __name__ == "__main__":
    print("Run this file from a wrapper that initializes Gradio UI.")
