# AI Resume Parser & Candidate Ranking System

> Starter template for an automated resume screening pipeline — built as part of the AI/ML track for **[hireai.rooman.com](https://hireai.rooman.com)**, Rooman's AI recruitment platform.

A system that automatically parses resumes, extracts structured features (skills, experience, education), and ranks candidates against a job description using NLP-based similarity metrics and machine-learning scoring.

---

## Project Goal

Build a pipeline that:

1. **Ingests** resumes in PDF / DOCX / TXT formats.
2. **Parses & extracts** structured features:
   - Skills (technical + soft)
   - Work experience (roles, durations, companies)
   - Education (degrees, institutions, fields)
   - Certifications, projects, contact info
3. **Computes similarity** between candidate profiles and a job description using NLP embeddings (TF-IDF, BERT, Sentence-Transformers).
4. **Ranks candidates** using a weighted ML scoring model.
5. **Exposes results** via REST API + CLI for downstream consumption.

---

## Architecture

```
┌──────────────┐    ┌──────────────┐    ┌────────────────┐    ┌──────────────┐
│   Resumes    │───▶│   Parser     │───▶│   Feature      │───▶│  Similarity  │
│  (PDF/DOCX)  │    │ (PyMuPDF/    │    │  Extraction    │    │   Scoring    │
└──────────────┘    │  python-docx)│    │ (spaCy NER +   │    │ (BERT/TF-IDF)│
                    └──────────────┘    │  Skill Matcher)│    └──────┬───────┘
                                        └────────────────┘           │
┌──────────────┐                                                     ▼
│ Job Desc.    │──────────────────────────────────────────▶  ┌──────────────┐
└──────────────┘                                             │   Ranking    │
                                                             │   Engine     │
                                                             └──────┬───────┘
                                                                    │
                                                                    ▼
                                                             ┌──────────────┐
                                                             │  REST API +  │
                                                             │     CLI      │
                                                             └──────────────┘
```

---

## Repository Structure

```
AIML-Template/
├── README.md                     # You are here
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment variable template
├── .gitignore
├── pyproject.toml                # Build config + linter settings
├── Makefile                      # Common commands (run, test, lint)
│
├── config/
│   ├── config.yaml               # App configuration
│   └── skills_taxonomy.json      # Curated skills dictionary
│
├── data/
│   ├── resumes/                  # Drop sample resumes here
│   ├── job_descriptions/         # Sample JDs
│   └── processed/                # Parsed JSON outputs
│
├── src/
│   ├── __init__.py
│   ├── main.py                   # CLI entry point
│   ├── api.py                    # FastAPI REST server
│   │
│   ├── parser/                   # Resume parsing
│   │   ├── __init__.py
│   │   ├── pdf_parser.py
│   │   ├── docx_parser.py
│   │   └── text_cleaner.py
│   │
│   ├── features/                 # Feature extraction
│   │   ├── __init__.py
│   │   ├── skills_extractor.py
│   │   ├── experience_extractor.py
│   │   ├── education_extractor.py
│   │   └── contact_extractor.py
│   │
│   ├── similarity/               # NLP similarity metrics
│   │   ├── __init__.py
│   │   ├── tfidf_matcher.py
│   │   ├── embedding_matcher.py  # BERT / Sentence-Transformers
│   │   └── hybrid_scorer.py
│   │
│   ├── ranking/                  # Candidate ranking
│   │   ├── __init__.py
│   │   ├── scorer.py             # ML scoring model
│   │   └── ranker.py             # Final sort + tie-breaks
│   │
│   └── utils/
│       ├── __init__.py
│       ├── logger.py
│       └── io.py
│
├── notebooks/                    # Exploration & EDA
│   └── 01_explore_parsing.ipynb
│
└── tests/
    ├── __init__.py
    ├── test_parser.py
    ├── test_features.py
    └── test_similarity.py
```

---

## Quick Start

```bash
# 1. Clone & set up
git clone <fork-url> && cd AIML-Template
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm

# 2. Configure
cp .env.example .env

# 3. Run on a single resume
python -m src.main --resume data/resumes/sample.pdf \
                   --jd data/job_descriptions/sample_jd.txt

# 4. Start the REST API
uvicorn src.api:app --reload --port 8000

# 5. Run tests
pytest tests/
```

---

## Suggested Tech Stack

| Layer            | Choices                                              |
| ---------------- | ---------------------------------------------------- |
| Parsing          | `PyMuPDF`, `pdfplumber`, `python-docx`               |
| NLP              | `spaCy`, `nltk`, `transformers`                      |
| Embeddings       | `sentence-transformers` (`all-MiniLM-L6-v2`)         |
| Similarity       | Cosine, BM25, hybrid                                 |
| ML Scoring       | `scikit-learn` (LogReg / GradientBoosting / XGBoost) |
| API              | `FastAPI` + `uvicorn`                                |
| Storage          | SQLite (dev) → Postgres (prod)                       |

---

## Team Workflow

1. **Fork** this repo and create a feature branch: `git checkout -b feat/<your-module>`.
2. Pick a module from the structure above (parser / features / similarity / ranking).
3. Implement against the stub interfaces — every module ships with a TODO scaffold.
4. Add unit tests in `tests/` (target ≥ 80% coverage).
5. Open a PR; CI runs lint + tests automatically.

### Module owners (fill in)

| Module        | Owner | Status      |
| ------------- | ----- | ----------- |
| `parser/`     | TBD   | scaffolded  |
| `features/`   | TBD   | scaffolded  |
| `similarity/` | TBD   | scaffolded  |
| `ranking/`    | TBD   | scaffolded  |
| `api.py`      | TBD   | scaffolded  |

---

## Context

This project is part of the AI/ML track for **[hireai.rooman.com](https://hireai.rooman.com)**, Rooman's AI recruitment platform. The goal is to build a standalone resume-screening engine that demonstrates end-to-end NLP and ML skills (parsing, feature extraction, similarity scoring, ranking). No external integration with the HireAI platform is in scope for this assignment — output is exposed via the local REST API and CLI.

---

## License

MIT — see `LICENSE`.
