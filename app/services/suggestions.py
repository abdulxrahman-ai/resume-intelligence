from typing import List


def generate_suggestions(
    missing_skills: List[str],
    final_score: float,
    resume_skills: List[str],
    jd_skills: List[str]
) -> List[str]:
    suggestions: List[str] = []

    if missing_skills:
        top_missing = ", ".join(missing_skills[:5])
        suggestions.append(
            f"Highlight or add evidence of these relevant skills if you genuinely have them: {top_missing}."
        )

    if final_score < 50:
        suggestions.append(
            "Your resume is currently not well aligned with this role. Tailor your summary, projects, and skills section for this specific job."
        )
    elif final_score < 75:
        suggestions.append(
            "Your resume has partial alignment. Improve keyword coverage and make relevant project experience more explicit."
        )
    else:
        suggestions.append(
            "Your resume is strongly aligned. Improve it further by quantifying results and emphasizing business impact."
        )

    if "python" in jd_skills and "python" not in resume_skills:
        suggestions.append("Make Python experience easier to find in your resume if you have worked with it.")

    if "machine learning" in jd_skills and "machine learning" not in resume_skills:
        suggestions.append("Add a dedicated machine learning project or experience bullet if applicable.")

    if "docker" in jd_skills and "docker" not in resume_skills:
        suggestions.append("Mention deployment, containerization, or Docker-based work if you have it.")

    if "api development" in jd_skills and "api development" not in resume_skills:
        suggestions.append("Show API-building experience such as FastAPI or Flask projects.")

    suggestions.append(
        "Use action verbs and measurable outcomes, such as improved accuracy, reduced latency, or increased efficiency."
    )

    return suggestions[:6]
