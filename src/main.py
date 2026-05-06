"""CLI entry point.

Usage:
    python -m src.main --resume <path> --jd <path>
    python -m src.main --resumes-dir data/resumes --jd <path> --top-k 10
"""

import argparse
from dataclasses import asdict
from pathlib import Path

from src.features import extract_features
from src.parser import parse_resume
from src.ranking import rank_candidates
from src.utils.io import read_text, save_json
from src.utils.logger import get_logger

log = get_logger(__name__)


def process_one(resume_path: str, jd_text: str) -> dict:
    log.info(f"Parsing {resume_path}")
    text = parse_resume(resume_path)
    profile = extract_features(text)
    return {"file": resume_path, "profile": asdict(profile)}


def main() -> None:
    parser = argparse.ArgumentParser(description="Resume parser & candidate ranker")
    parser.add_argument("--resume", help="Path to a single resume")
    parser.add_argument("--resumes-dir", help="Directory of resumes for batch ranking")
    parser.add_argument("--jd", required=True, help="Path to job description text file")
    parser.add_argument("--top-k", type=int, default=None)
    parser.add_argument("--output", default="data/processed/results.json")
    args = parser.parse_args()

    jd_text = read_text(args.jd)

    if args.resume:
        result = process_one(args.resume, jd_text)
        save_json(result, args.output)
        log.info(f"Wrote {args.output}")
        return

    if args.resumes_dir:
        files = [str(p) for p in Path(args.resumes_dir).glob("*") if p.is_file()]
        log.info(f"Found {len(files)} resumes")
        profiles = [extract_features(parse_resume(f)) for f in files]
        ranked = rank_candidates(profiles, jd_text, top_k=args.top_k)
        out = [
            {"rank": i + 1, "file": files[profiles.index(p)], "score": asdict(s)}
            for i, (p, s) in enumerate(ranked)
        ]
        save_json(out, args.output)
        log.info(f"Wrote ranked results to {args.output}")
        return

    parser.error("Provide either --resume or --resumes-dir")


if __name__ == "__main__":
    main()
