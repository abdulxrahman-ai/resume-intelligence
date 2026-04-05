from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SKILLS_FILE = BASE_DIR / "data" / "skills" / "skills_list.json"
SKILL_ALIASES_FILE = BASE_DIR / "data" / "skills" / "skill_aliases.json"

SEMANTIC_MODEL_NAME = "all-MiniLM-L6-v2"

FINAL_SCORE_WEIGHTS = {
    "skill": 0.4,
    "semantic": 0.4,
    "keyword": 0.2,
}
