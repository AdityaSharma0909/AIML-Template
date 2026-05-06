"""Extract skills from resume text using a curated taxonomy + fuzzy matching."""

import json
from pathlib import Path

TAXONOMY_PATH = Path(__file__).parents[2] / "config" / "skills_taxonomy.json"


def load_taxonomy() -> dict[str, list[str]]:
    with open(TAXONOMY_PATH) as f:
        return json.load(f)


def extract_skills(text: str) -> list[str]:
    """Return a deduplicated list of skills found in the text.

    TODO:
        - Lowercase the text and tokenize
        - Match against the flattened taxonomy (substring + word boundary)
        - Add fuzzy matching (rapidfuzz) for misspellings
        - Optionally use spaCy PhraseMatcher for performance
    """
    taxonomy = load_taxonomy()
    all_skills = {s for group in taxonomy.values() for s in group}
    text_lower = text.lower()
    found = sorted({s for s in all_skills if s in text_lower})
    return found
