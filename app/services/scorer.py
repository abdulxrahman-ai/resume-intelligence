from collections import Counter
from typing import List

from app.config import FINAL_SCORE_WEIGHTS
from app.services.text_cleaner import tokenize_text


def compute_skill_match_score(resume_skills: List[str], jd_skills: List[str]) -> float:
    if not jd_skills:
        return 0.0

    resume_set = set(resume_skills)
    jd_set = set(jd_skills)
    matched_count = len(resume_set.intersection(jd_set))

    return round((matched_count / len(jd_set)) * 100, 2)


def compute_keyword_score(resume_text: str, jd_text: str) -> float:
    """
    Weighted keyword overlap based on job description terms.
    """
    resume_tokens = tokenize_text(resume_text)
    jd_tokens = tokenize_text(jd_text)

    if not jd_tokens:
        return 0.0

    resume_counter = Counter(resume_tokens)
    jd_counter = Counter(jd_tokens)

    jd_unique_tokens = {
        token for token in jd_counter
        if len(token) > 2 and not token.isdigit()
    }

    if not jd_unique_tokens:
        return 0.0

    matched_tokens = sum(1 for token in jd_unique_tokens if token in resume_counter)
    score = (matched_tokens / len(jd_unique_tokens)) * 100

    return round(score, 2)


def compute_missing_skills(resume_skills: List[str], jd_skills: List[str]) -> List[str]:
    return sorted(list(set(jd_skills) - set(resume_skills)))


def compute_final_score(skill_score: float, semantic_score: float, keyword_score: float) -> float:
    final_score = (
        FINAL_SCORE_WEIGHTS["skill"] * skill_score
        + FINAL_SCORE_WEIGHTS["semantic"] * semantic_score
        + FINAL_SCORE_WEIGHTS["keyword"] * keyword_score
    )
    return round(final_score, 2)


def get_score_band(score: float) -> str:
    if score < 50:
        return "Weak Match"
    if score < 75:
        return "Moderate Match"
    return "Strong Match"


def get_score_explanation(score: float) -> str:
    if score < 50:
        return "The resume is currently weakly aligned with the target job description."
    if score < 75:
        return "The resume has moderate alignment but could be improved with stronger keyword and skill coverage."
    return "The resume is strongly aligned with the target role."
