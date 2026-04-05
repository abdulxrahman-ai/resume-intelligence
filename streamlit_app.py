import streamlit as st
import re

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

SKILLS = [
    "python", "sql", "machine learning", "deep learning", "nlp",
    "pandas", "numpy", "tensorflow", "pytorch", "fastapi",
    "streamlit", "data analysis", "power bi", "tableau",
    "excel", "aws", "docker", "git", "api"
]

def analyze_resume(resume, jd):
    resume = resume.lower()
    jd = jd.lower()

    matched = [s for s in SKILLS if s in resume]
    missing = [s for s in SKILLS if s in jd and s not in resume]

    score = min(95, 50 + len(matched)*3 - len(missing)*2)

    strengths = []
    improvements = []

    if matched:
        strengths.append(f"Strong skills detected: {', '.join(matched[:5])}")

    if "project" in resume:
        strengths.append("Projects section detected — good for technical roles")

    if not strengths:
        strengths.append("Basic resume structure present")

    if missing:
        improvements.append(f"Add these skills: {', '.join(missing[:5])}")

    improvements.append("Add measurable achievements (%, numbers)")
    improvements.append("Use more action verbs (built, developed, created)")

    return score, matched, missing, strengths, improvements


st.title("AI Resume Analyzer")

st.write("Upload your resume or paste text to analyze.")

resume_text = st.text_area("Paste Resume Text")

job_description = st.text_area(
    "Paste Job Description",
    value="Looking for AI/ML Engineer with Python, ML, SQL, FastAPI"
)

if st.button("Analyze Resume"):

    if not resume_text.strip():
        st.warning("Please paste resume text")
    else:
        score, matched, missing, strengths, improvements = analyze_resume(resume_text, job_description)

        st.subheader("Results")

        col1, col2, col3 = st.columns(3)

        col1.metric("Score", f"{score}%")
        col2.metric("Matched Skills", len(matched))
        col3.metric("Missing Skills", len(missing))

        st.progress(score / 100)

        st.subheader("Matched Skills")
        st.write(matched)

        st.subheader("Missing Skills")
        st.write(missing)

        st.subheader("Strengths")
        for s in strengths:
            st.success(s)

        st.subheader("Improvements")
        for i in improvements:
            st.warning(i)
