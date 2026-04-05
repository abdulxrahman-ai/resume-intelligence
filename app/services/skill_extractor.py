import json
import re
from typing import Dict, List, Set

from app.config import SKILLS_FILE, SKILL_ALIASES_FILE
from app.services.text_cleaner import clean_text


def load_skills() -> List[str]:
    with open(SKILLS_FILE, "r", encoding="utf-8") as file:
        skills = json.load(file)
    return sorted({skill.lower().strip() for skill in skills if skill.strip()})


def load_skill_aliases() -> Dict[str, str]:
    with open(SKILL_ALIASES_FILE, "r", encoding="utf-8") as file:
        aliases = json.load(file)
    return {k.lower().strip(): v.lower().strip() for k, v in aliases.items()}


def escape_skill_for_pattern(skill: str) -> str:
    """
    Escape skill for regex matching, allowing flexible whitespace.
    """
    escaped = re.escape(skill)
    escaped = escaped.replace(r"\ ", r"\s+")
    return escaped


def extract_skills(text: str) -> List[str]:
    """
    Extract normalized skills using:
    - canonical skills list
    - alias mapping
    - regex word-boundary matching
    """
    cleaned_text = clean_text(text)
    if not cleaned_text:
        return []

    skills = load_skills()
    aliases = load_skill_aliases()

    found_skills: Set[str] = set()

    # First, match canonical skills
    for skill in skills:
        pattern = rf"(?<!\w){escape_skill_for_pattern(skill)}(?!\w)"
        if re.search(pattern, cleaned_text, flags=re.IGNORECASE):
            found_skills.add(skill)

    # Then, match aliases and map them to canonical form
    for alias, canonical_skill in aliases.items():
        pattern = rf"(?<!\w){escape_skill_for_pattern(alias)}(?!\w)"
        if re.search(pattern, cleaned_text, flags=re.IGNORECASE):
            found_skills.add(canonical_skill)

    return sorted(found_skills)
