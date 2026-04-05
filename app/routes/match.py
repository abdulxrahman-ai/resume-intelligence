from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from app.models.schemas import MatchResponse
from app.services.pdf_parser import extract_text_from_pdf
from app.services.scorer import (
    compute_final_score,
    compute_keyword_score,
    compute_missing_skills,
    compute_skill_match_score,
    get_score_band,
)
from app.services.similarity import compute_semantic_similarity
from app.services.skill_extractor import extract_skills
from app.services.suggestions import generate_suggestions
from app.services.text_cleaner import clean_text

router = APIRouter(tags=["Matching"])


@router.post("/match", response_model=MatchResponse)
async def match_resume_to_job(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
) -> MatchResponse:
    if not resume.filename:
        raise HTTPException(status_code=400, detail="Resume file is required.")

    if not resume.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Resume must be a PDF file.")

    if not job_description or not job_description.strip():
        raise HTTPException(status_code=400, detail="Job description cannot be empty.")

    file_bytes = await resume.read()
    if not file_bytes:
        raise HTTPException(status_code=400, detail="Uploaded PDF is empty.")

    try:
        resume_text = extract_text_from_pdf(file_bytes)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Unexpected PDF parsing error: {exc}") from exc

    cleaned_resume = clean_text(resume_text)
    cleaned_jd = clean_text(job_description)

    if not cleaned_resume:
        raise HTTPException(status_code=400, detail="Resume contains no usable text.")
    if not cleaned_jd:
        raise HTTPException(status_code=400, detail="Job description contains no usable text.")

    resume_skills = extract_skills(cleaned_resume)
    jd_skills = extract_skills(cleaned_jd)
    missing_skills = compute_missing_skills(resume_skills, jd_skills)

    skill_score = compute_skill_match_score(resume_skills, jd_skills)
    semantic_score = compute_semantic_similarity(cleaned_resume, cleaned_jd)
    keyword_score = compute_keyword_score(cleaned_resume, cleaned_jd)
    final_score = compute_final_score(skill_score, semantic_score, keyword_score)
    score_band = get_score_band(final_score)

    suggestions = generate_suggestions(
        missing_skills=missing_skills,
        final_score=final_score,
        resume_skills=resume_skills,
        jd_skills=jd_skills,
    )

    return MatchResponse(
        resume_skills=resume_skills,
        jd_skills=jd_skills,
        missing_skills=missing_skills,
        skill_match_score=skill_score,
        semantic_similarity_score=semantic_score,
        keyword_score=keyword_score,
        final_score=final_score,
        score_band=score_band,
        suggestions=suggestions,
    )
