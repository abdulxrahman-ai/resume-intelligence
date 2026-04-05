from app.services.scorer import compute_skill_match_score


def test_compute_skill_match_score():
    resume_skills = ["python", "pytorch", "fastapi"]
    jd_skills = ["python", "docker", "fastapi"]

    score = compute_skill_match_score(resume_skills, jd_skills)

    assert score == 66.67
