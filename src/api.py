"""FastAPI REST server.

Run:
    uvicorn src.api:app --reload --port 8000
"""

import shutil
import tempfile
from dataclasses import asdict
from pathlib import Path

from fastapi import FastAPI, File, Form, UploadFile
from pydantic import BaseModel

from src.features import extract_features
from src.parser import parse_resume
from src.ranking import score_candidate

app = FastAPI(
    title="Resume Ranker API",
    description="Parse resumes, extract features, score against job descriptions.",
    version="0.1.0",
)


class ScoreResponse(BaseModel):
    profile: dict
    score: dict


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/parse", summary="Parse a single resume into structured features")
async def parse_endpoint(file: UploadFile = File(...)) -> dict:
    suffix = Path(file.filename or "").suffix
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name
    text = parse_resume(tmp_path)
    profile = extract_features(text)
    return asdict(profile)


@app.post("/score", response_model=ScoreResponse, summary="Score a resume against a JD")
async def score_endpoint(
    file: UploadFile = File(...),
    jd_text: str = Form(...),
) -> ScoreResponse:
    suffix = Path(file.filename or "").suffix
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name
    profile = extract_features(parse_resume(tmp_path))
    score = score_candidate(profile, jd_text)
    return ScoreResponse(profile=asdict(profile), score=asdict(score))
