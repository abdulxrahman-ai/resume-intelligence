from pydantic import BaseModel, Field
from typing import List


class MatchResponse(BaseModel):
    resume_skills: List[str] = Field(default_factory=list)
    jd_skills: List[str] = Field(default_factory=list)
    missing_skills: List[str] = Field(default_factory=list)
    skill_match_score: float
    semantic_similarity_score: float
    keyword_score: float
    final_score: float
    score_band: str
    suggestions: List[str] = Field(default_factory=list)
