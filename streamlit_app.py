import streamlit as st
import re

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.markdown(
    """
    <style>
    html {
        scroll-behavior: smooth;
    }

    body {
        background:
            radial-gradient(circle at 15% 20%, rgba(56, 189, 248, 0.12), transparent 28%),
            radial-gradient(circle at 85% 18%, rgba(99, 102, 241, 0.14), transparent 30%),
            radial-gradient(circle at 50% 85%, rgba(34, 197, 94, 0.08), transparent 28%),
            linear-gradient(135deg, rgba(2, 6, 23, 1) 0%, rgba(10, 15, 35, 1) 45%, rgba(8, 20, 45, 1) 100%);
        background-attachment: fixed;
    }

    .stApp {
        background:
            radial-gradient(circle at 12% 22%, rgba(59, 130, 246, 0.14), transparent 24%),
            radial-gradient(circle at 88% 12%, rgba(14, 165, 233, 0.10), transparent 22%),
            radial-gradient(circle at 50% 100%, rgba(168, 85, 247, 0.08), transparent 26%),
            linear-gradient(135deg, rgba(2, 6, 23, 0.97), rgba(7, 12, 30, 0.98), rgba(4, 14, 35, 0.98));
        position: relative;
        overflow: hidden;
    }

    .stApp::before {
        content: "";
        position: fixed;
        inset: -20%;
        pointer-events: none;
        background:
            radial-gradient(circle, rgba(59, 130, 246, 0.12) 0%, transparent 18%),
            radial-gradient(circle, rgba(34, 211, 238, 0.10) 0%, transparent 16%),
            radial-gradient(circle, rgba(99, 102, 241, 0.08) 0%, transparent 20%);
        background-repeat: no-repeat;
        background-position: 12% 18%, 85% 24%, 50% 78%;
        filter: blur(28px);
        animation: ambientFloat 18s ease-in-out infinite alternate;
        z-index: 0;
    }

    .stApp::after {
        content: "";
        position: fixed;
        inset: 0;
        pointer-events: none;
        background: linear-gradient(
            120deg,
            transparent 0%,
            rgba(255, 255, 255, 0.025) 25%,
            transparent 50%,
            rgba(59, 130, 246, 0.035) 75%,
            transparent 100%
        );
        background-size: 220% 220%;
        animation: shimmerMove 12s linear infinite;
        z-index: 0;
        opacity: 0.8;
    }

    .main {
        animation: fadeInPage 0.8s ease-in-out;
        position: relative;
        z-index: 1;
    }

    .block-container {
        position: relative;
        z-index: 1;
    }

    @keyframes fadeInPage {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .fade-section {
        animation: fadeUp 0.7s ease both;
    }

    .fade-delay-1 {
        animation-delay: 0.08s;
    }

    .fade-delay-2 {
        animation-delay: 0.16s;
    }

    .fade-delay-3 {
        animation-delay: 0.24s;
    }

    .fade-delay-4 {
        animation-delay: 0.32s;
    }

    .fade-delay-5 {
        animation-delay: 0.4s;
    }

    @keyframes fadeUp {
        from {
            opacity: 0;
            transform: translateY(18px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes ambientFloat {
        0% {
            transform: translate3d(0px, 0px, 0) scale(1);
        }
        50% {
            transform: translate3d(18px, -14px, 0) scale(1.04);
        }
        100% {
            transform: translate3d(-12px, 16px, 0) scale(0.98);
        }
    }

    @keyframes shimmerMove {
        0% {
            background-position: 0% 50%;
        }
        100% {
            background-position: 100% 50%;
        }
    }

    h1, h2, h3 {
        text-shadow: 0 0 18px rgba(96, 165, 250, 0.10);
    }

    div[data-testid="stMetric"] {
        border: 1px solid rgba(148, 163, 184, 0.22);
        border-radius: 18px;
        padding: 14px 10px;
        box-shadow:
            0 8px 24px rgba(15, 23, 42, 0.18),
            0 0 0 rgba(59, 130, 246, 0);
        transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
        background: linear-gradient(
            135deg,
            rgba(255, 255, 255, 0.06),
            rgba(255, 255, 255, 0.025)
        );
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
    }

    div[data-testid="stMetric"]:hover {
        transform: translateY(-3px);
        border-color: rgba(96, 165, 250, 0.34);
        box-shadow:
            0 14px 32px rgba(15, 23, 42, 0.24),
            0 0 24px rgba(59, 130, 246, 0.12);
    }

    div.stButton > button {
        transition: all 0.28s ease;
        border-radius: 12px;
        border: 1px solid rgba(96, 165, 250, 0.22);
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.88), rgba(15, 23, 42, 0.92));
        box-shadow:
            0 8px 24px rgba(15, 23, 42, 0.20),
            0 0 18px rgba(59, 130, 246, 0.08);
        position: relative;
        overflow: hidden;
    }

    div.stButton > button:hover {
        transform: translateY(-2px);
        border-color: rgba(96, 165, 250, 0.45);
        box-shadow:
            0 10px 24px rgba(15, 23, 42, 0.24),
            0 0 28px rgba(59, 130, 246, 0.18),
            0 0 42px rgba(34, 211, 238, 0.10);
    }

    div.stButton > button:focus {
        outline: none;
        box-shadow:
            0 0 0 1px rgba(96, 165, 250, 0.35),
            0 0 26px rgba(59, 130, 246, 0.16);
    }

    div.stButton > button[kind="primary"] {
        animation: buttonGlowPulse 2.8s ease-in-out infinite;
    }

    @keyframes buttonGlowPulse {
        0% {
            box-shadow:
                0 8px 24px rgba(15, 23, 42, 0.20),
                0 0 10px rgba(59, 130, 246, 0.10);
        }
        50% {
            box-shadow:
                0 10px 28px rgba(15, 23, 42, 0.24),
                0 0 24px rgba(59, 130, 246, 0.18),
                0 0 34px rgba(34, 211, 238, 0.08);
        }
        100% {
            box-shadow:
                0 8px 24px rgba(15, 23, 42, 0.20),
                0 0 10px rgba(59, 130, 246, 0.10);
        }
    }

    div[data-testid="stTextArea"] textarea {
        transition: all 0.25s ease;
        border-radius: 12px;
        background: linear-gradient(
            135deg,
            rgba(255, 255, 255, 0.045),
            rgba(255, 255, 255, 0.02)
        );
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(148, 163, 184, 0.18);
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.14);
    }

    div[data-testid="stTextArea"] textarea:focus {
        box-shadow:
            0 0 0 1px rgba(100, 116, 139, 0.35),
            0 0 22px rgba(59, 130, 246, 0.12);
        border-color: rgba(96, 165, 250, 0.30);
    }

    div[data-testid="stProgressBar"] > div > div {
        transition: width 0.6s ease-in-out;
        box-shadow: 0 0 18px rgba(59, 130, 246, 0.35);
    }

    div[data-testid="stAlert"] {
        background: linear-gradient(
            135deg,
            rgba(255, 255, 255, 0.07),
            rgba(255, 255, 255, 0.03)
        );
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(148, 163, 184, 0.16);
        box-shadow: 0 10px 28px rgba(15, 23, 42, 0.14);
        border-radius: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

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

    score = min(95, 50 + len(matched) * 3 - len(missing) * 2)

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


st.markdown('<div class="fade-section fade-delay-1">', unsafe_allow_html=True)
st.title("AI Resume Analyzer")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="fade-section fade-delay-2">', unsafe_allow_html=True)
st.write("Upload your resume or paste text to analyze.")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="fade-section fade-delay-3">', unsafe_allow_html=True)
resume_text = st.text_area("Paste Resume Text")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="fade-section fade-delay-4">', unsafe_allow_html=True)
job_description = st.text_area(
    "Paste Job Description",
    value="Looking for AI/ML Engineer with Python, ML, SQL, FastAPI"
)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="fade-section fade-delay-5">', unsafe_allow_html=True)
analyze_clicked = st.button("Analyze Resume")
st.markdown('</div>', unsafe_allow_html=True)

if analyze_clicked:

    if not resume_text.strip():
        st.warning("Please paste resume text")
    else:
        score, matched, missing, strengths, improvements = analyze_resume(resume_text, job_description)

        st.markdown('<div class="fade-section">', unsafe_allow_html=True)
        st.subheader("Results")
        st.markdown('</div>', unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown('<div class="fade-section fade-delay-1">', unsafe_allow_html=True)
            st.metric("Score", f"{score}%")
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="fade-section fade-delay-2">', unsafe_allow_html=True)
            st.metric("Matched Skills", len(matched))
            st.markdown('</div>', unsafe_allow_html=True)

        with col3:
            st.markdown('<div class="fade-section fade-delay-3">', unsafe_allow_html=True)
            st.metric("Missing Skills", len(missing))
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="fade-section fade-delay-2">', unsafe_allow_html=True)
        st.progress(score / 100)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="fade-section fade-delay-2">', unsafe_allow_html=True)
        st.subheader("Matched Skills")
        st.write(matched)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="fade-section fade-delay-3">', unsafe_allow_html=True)
        st.subheader("Missing Skills")
        st.write(missing)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="fade-section fade-delay-4">', unsafe_allow_html=True)
        st.subheader("Strengths")
        for s in strengths:
            st.success(s)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="fade-section fade-delay-5">', unsafe_allow_html=True)
        st.subheader("Improvements")
        for i in improvements:
            st.warning(i)
        st.markdown('</div>', unsafe_allow_html=True)
