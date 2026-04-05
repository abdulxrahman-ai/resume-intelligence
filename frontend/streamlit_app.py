import os
import requests
import streamlit as st

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/match")

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


def get_score_color(score: float) -> str:
    if score < 50:
        return "#ff4b4b"
    elif score < 75:
        return "#f0ad4e"
    return "#28a745"


def render_badges(items, color="#1f77b4"):
    if not items:
        st.write("None")
        return

    badge_html = ""
    for item in items:
        badge_html += f'''
        <span style="
            display:inline-block;
            background-color:{color};
            color:white;
            padding:6px 12px;
            margin:4px 6px 4px 0;
            border-radius:20px;
            font-size:14px;
        ">{item}</span>
        '''
    st.markdown(badge_html, unsafe_allow_html=True)


def render_score_card(title: str, value: float, subtitle: str = ""):
    color = get_score_color(value)
    st.markdown(
        f'''
        <div style="
            background-color:#111827;
            padding:18px;
            border-radius:16px;
            border-left:6px solid {color};
            box-shadow:0 2px 10px rgba(0,0,0,0.08);
            margin-bottom:12px;
        ">
            <h4 style="margin:0; color:white;">{title}</h4>
            <h2 style="margin:8px 0 6px 0; color:{color};">{value}%</h2>
            <p style="margin:0; color:#d1d5db;">{subtitle}</p>
        </div>
        ''',
        unsafe_allow_html=True,
    )


def render_info_card(title: str, content: str):
    st.markdown(
        f'''
        <div style="
            background-color:#111827;
            padding:18px;
            border-radius:16px;
            box-shadow:0 2px 10px rgba(0,0,0,0.08);
            margin-bottom:12px;
        ">
            <h4 style="margin-top:0; color:white;">{title}</h4>
            <p style="color:#d1d5db; margin-bottom:0;">{content}</p>
        </div>
        ''',
        unsafe_allow_html=True,
    )


st.title("📄 AI Resume Analyzer + Job Matcher")
st.caption("Analyze how well a resume matches a job description using NLP, skill extraction, and semantic similarity.")

with st.sidebar:
    st.header("Project Overview")
    st.write(
        '''
        This application evaluates:
        - skill overlap
        - semantic similarity
        - keyword relevance
        - missing skills
        - improvement suggestions
        '''
    )
    st.success("Best for AI/ML, Data Science, and Software job matching demos.")
    st.info("Tip: Use a resume with clear skills, project descriptions, and tools.")

left_col, right_col = st.columns([1.1, 0.9])

with left_col:
    st.subheader("Input")
    uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
    job_description = st.text_area("Paste Job Description", height=320, placeholder="Paste the full job description here...")
    analyze_clicked = st.button("Analyze Match", use_container_width=True)

with right_col:
    st.subheader("What you’ll see")
    render_info_card(
        "Analysis Output",
        "Get an overall match score, extracted skills, missing skills, and tailored suggestions to improve your resume for the target role."
    )
    render_info_card(
        "Use Cases",
        "Useful for job seekers, resume optimization, recruiter tools, and NLP-based document matching applications."
    )

if analyze_clicked:
    if uploaded_file is None:
        st.error("Please upload a PDF resume.")
    elif not job_description.strip():
        st.error("Please paste a job description.")
    else:
        with st.spinner("Analyzing resume against job description..."):
            try:
                files = {
                    "resume": (
                        uploaded_file.name,
                        uploaded_file.getvalue(),
                        "application/pdf",
                    )
                }
                data = {"job_description": job_description}
                response = requests.post(API_URL, files=files, data=data, timeout=120)

                if response.status_code != 200:
                    try:
                        error_detail = response.json().get("detail", response.text)
                    except Exception:
                        error_detail = response.text
                    st.error(f"API Error: {error_detail}")
                else:
                    result = response.json()

                    final_score = result["final_score"]
                    score_band = result["score_band"]
                    score_color = get_score_color(final_score)

                    st.divider()
                    st.subheader("Results")

                    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

                    with metric_col1:
                        render_score_card("Final Match Score", final_score, score_band)

                    with metric_col2:
                        render_score_card("Skill Match", result["skill_match_score"], "Skill overlap between resume and JD")

                    with metric_col3:
                        render_score_card("Semantic Score", result["semantic_similarity_score"], "Meaning-level similarity")

                    with metric_col4:
                        render_score_card("Keyword Score", result["keyword_score"], "Keyword relevance")

                    st.markdown(
                        f'''
                        <div style="
                            margin-top:10px;
                            margin-bottom:18px;
                            padding:14px;
                            border-radius:12px;
                            background-color:{score_color}22;
                            border:1px solid {score_color};
                        ">
                            <strong>Overall Assessment:</strong> {score_band}
                        </div>
                        ''',
                        unsafe_allow_html=True,
                    )

                    st.progress(min(int(final_score), 100))

                    results_col1, results_col2 = st.columns(2)

                    with results_col1:
                        st.subheader("Extracted Skills")

                        st.markdown("**Resume Skills**")
                        render_badges(result["resume_skills"], color="#2563eb")

                        st.markdown("**Job Description Skills**")
                        render_badges(result["jd_skills"], color="#7c3aed")

                    with results_col2:
                        st.subheader("Skill Gap Analysis")

                        st.markdown("**Missing Skills**")
                        if result["missing_skills"]:
                            render_badges(result["missing_skills"], color="#dc2626")
                        else:
                            st.success("No major missing skills detected.")

                        st.markdown("**Suggestions**")
                        for suggestion in result["suggestions"]:
                            st.markdown(
                                f'''
                                <div style="
                                    background-color:#111827;
                                    padding:12px 14px;
                                    border-radius:12px;
                                    margin-bottom:10px;
                                    border-left:4px solid #10b981;
                                    color:#d1d5db;
                                ">
                                    {suggestion}
                                </div>
                                ''',
                                unsafe_allow_html=True,
                            )

                    with st.expander("Why this score was given"):
                        st.write(
                            '''
                            The final score is based on:
                            - overlap between extracted resume skills and job description skills
                            - semantic similarity between the resume text and the job description
                            - keyword relevance between both documents
                            '''
                        )

            except requests.exceptions.RequestException as exc:
                st.error(f"Connection error: {exc}")
            except Exception as exc:
                st.error(f"Unexpected error: {exc}")
