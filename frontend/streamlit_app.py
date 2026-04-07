import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8501/match"

st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root{
    --bg:#f7f9fc;
    --surface:#ffffff;
    --text:#0f172a;
    --muted:#64748b;
    --line:#e2e8f0;
    --line-strong:#dbe4f0;
    --primary:#2563eb;
    --primary-hover:#1d4ed8;
    --primary-soft:#eff6ff;
    --success:#10b981;
    --warning:#f59e0b;
    --danger:#ef4444;
    --purple:#8b5cf6;
    --shadow:0 10px 30px rgba(15,23,42,0.06);
    --shadow-hover:0 16px 40px rgba(15,23,42,0.10);
}

/* Hide Streamlit chrome */
header[data-testid="stHeader"] {display:none !important;}
[data-testid="stToolbar"] {display:none !important;}
[data-testid="stDecoration"] {display:none !important;}
[data-testid="collapsedControl"] {display:none !important;}
section[data-testid="stSidebar"] {display:none !important;}
#MainMenu {visibility:hidden !important;}
footer {visibility:hidden !important;}

html, body, [class*="css"]{
    font-family:'Inter',sans-serif;
}

.stApp{
    background: linear-gradient(180deg, #ffffff 0%, var(--bg) 100%);
    color: var(--text);
}

.block-container{
    max-width: 1360px;
    padding-top: 1.2rem;
    padding-bottom: 2rem;
}

h1,h2,h3,h4,h5,h6,p,label,div,span{
    color: var(--text);
}

h1{font-size:34px !important; line-height:1.1; font-weight:800 !important; letter-spacing:-0.03em;}
h2{font-size:26px !important; line-height:1.2; font-weight:800 !important; letter-spacing:-0.02em;}
h3{font-size:20px !important; line-height:1.25; font-weight:700 !important;}
p, div, label{font-size:15px; line-height:1.7;}

*:focus-visible{
    outline:3px solid rgba(37,99,235,0.22) !important;
    outline-offset:2px !important;
    border-radius:10px !important;
}

div[data-testid="stFileUploader"] > section{
    background:var(--surface) !important;
    border:1px solid var(--line-strong) !important;
    border-radius:18px !important;
    transition: box-shadow 0.2s ease, border-color 0.2s ease, transform 0.2s ease;
    box-shadow: var(--shadow);
}

div[data-testid="stFileUploader"] > section:hover{
    border-color:#bfdbfe !important;
    box-shadow: var(--shadow-hover);
    transform: translateY(-1px);
}

div[data-baseweb="textarea"] textarea{
    background:var(--surface) !important;
    color:var(--text) !important;
    border-radius:16px !important;
    border:1px solid var(--line-strong) !important;
    transition: box-shadow 0.2s ease, border-color 0.2s ease;
    box-shadow: var(--shadow);
}

div[data-baseweb="textarea"] textarea:focus{
    border-color:#93c5fd !important;
    box-shadow: 0 0 0 3px rgba(37,99,235,0.10) !important;
}

div.stButton > button{
    min-height:48px;
    border:none;
    border-radius:14px;
    padding:0.95rem 1.2rem;
    font-weight:700;
    font-size:15px;
    color:#ffffff;
    background:linear-gradient(90deg, var(--primary), #0ea5e9);
    box-shadow:0 12px 24px rgba(37,99,235,0.18);
    transition:transform 0.18s ease, box-shadow 0.18s ease, background 0.18s ease;
}

div.stButton > button:hover{
    background:linear-gradient(90deg, var(--primary-hover), #0284c7);
    transform:translateY(-1px);
    box-shadow:0 16px 30px rgba(37,99,235,0.22);
}

.header-row-title{
    font-size:22px;
    font-weight:800;
    letter-spacing:-0.02em;
    color:var(--text);
    margin-bottom:18px;
    margin-top:2px;
}

.hero-wrap{
    display:grid;
    grid-template-columns: 1.2fr 0.8fr;
    gap:18px;
    margin-bottom:24px;
}

.hero-main{
    background:linear-gradient(180deg, #ffffff 0%, #fbfdff 100%);
    border:1px solid var(--line);
    border-radius:28px;
    padding:30px;
    box-shadow:var(--shadow);
    position:relative;
    overflow:hidden;
}

.hero-main::after{
    content:"";
    position:absolute;
    top:-40px;
    right:-50px;
    width:220px;
    height:220px;
    background:radial-gradient(circle, rgba(37,99,235,0.10), transparent 70%);
    pointer-events:none;
}

.hero-chip{
    display:inline-block;
    background:var(--primary-soft);
    color:var(--primary);
    border:1px solid #bfdbfe;
    border-radius:999px;
    padding:8px 12px;
    font-size:12px;
    font-weight:700;
    margin-bottom:18px;
}

.hero-title{
    font-size:42px;
    font-weight:800;
    line-height:1.05;
    letter-spacing:-0.04em;
    margin-bottom:12px;
    max-width:760px;
}

.hero-text{
    color:#475569;
    font-size:15px;
    line-height:1.8;
    max-width:760px;
    margin-bottom:22px;
}

.hero-actions{
    display:flex;
    gap:12px;
    flex-wrap:wrap;
    margin-top:14px;
}

.hero-action-secondary{
    display:inline-flex;
    align-items:center;
    justify-content:center;
    min-height:46px;
    padding:0 16px;
    border-radius:14px;
    background:#ffffff;
    border:1px solid var(--line-strong);
    color:var(--text);
    font-weight:700;
    font-size:14px;
    box-shadow:var(--shadow);
}

.hero-side{
    background:linear-gradient(180deg, #ffffff 0%, #fbfdff 100%);
    border:1px solid var(--line);
    border-radius:28px;
    padding:26px;
    box-shadow:var(--shadow);
}

.side-title{
    font-size:18px;
    font-weight:800;
    margin-bottom:10px;
    letter-spacing:-0.02em;
}

.side-text{
    color:#475569;
    font-size:14px;
    line-height:1.8;
    margin-bottom:14px;
}

.side-list{
    display:grid;
    gap:12px;
}

.side-list-item{
    background:#f8fbff;
    border:1px solid var(--line);
    border-radius:16px;
    padding:14px;
    transition: box-shadow 0.18s ease, transform 0.18s ease;
}

.side-list-item:hover{
    transform:translateY(-1px);
    box-shadow:var(--shadow);
}

.side-list-title{
    font-size:14px;
    font-weight:700;
    margin-bottom:4px;
}

.side-list-text{
    color:var(--muted);
    font-size:13px;
    line-height:1.65;
}

.digest-grid{
    display:grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap:16px;
    margin-bottom:24px;
}

.digest-card{
    background:#ffffff;
    border:1px solid var(--line);
    border-radius:20px;
    padding:18px;
    box-shadow:var(--shadow);
    transition: transform 0.18s ease, box-shadow 0.18s ease;
}

.digest-card:hover{
    transform:translateY(-2px);
    box-shadow:var(--shadow-hover);
}

.digest-kicker{
    color:var(--muted);
    font-size:12px;
    font-weight:700;
    text-transform:uppercase;
    letter-spacing:0.05em;
    margin-bottom:8px;
}

.digest-title{
    font-size:18px;
    font-weight:800;
    letter-spacing:-0.02em;
    margin-bottom:8px;
}

.digest-text{
    color:#475569;
    font-size:14px;
    line-height:1.75;
}

.section-title{
    font-size:20px;
    font-weight:800;
    letter-spacing:-0.02em;
    margin-bottom:6px;
}

.section-sub{
    color:var(--muted);
    font-size:14px;
    line-height:1.75;
    margin-bottom:10px;
}

.metric-card{
    background:#ffffff;
    border:1px solid var(--line);
    border-radius:22px;
    padding:18px;
    min-height:270px;
    box-shadow:var(--shadow);
    transition:transform 0.18s ease, box-shadow 0.18s ease;
    display:flex;
    flex-direction:column;
}

.metric-card:hover{
    transform:translateY(-2px);
    box-shadow:var(--shadow-hover);
}

.metric-title{
    font-size:15px;
    font-weight:700;
    margin-bottom:12px;
}

.metric-sub{
    color:var(--muted);
    font-size:13px;
    line-height:1.65;
    margin-top:auto;
    text-align:center;
}

.circle-wrap{
    display:flex;
    justify-content:center;
    align-items:center;
    margin:4px 0 8px 0;
    min-height:170px;
}

.circle-value{
    font-size:28px;
    font-weight:800;
    fill:var(--text);
}

.circle-label{
    font-size:12px;
    font-weight:600;
    fill:var(--muted);
}

.assessment{
    background:linear-gradient(90deg, #eff6ff, #f8fbff);
    border:1px solid #bfdbfe;
    border-radius:14px;
    padding:14px 16px;
    margin:14px 0 18px 0;
    font-size:17px;
    font-weight:700;
    color:var(--primary);
}

.group-card{
    background:#ffffff;
    border:1px solid var(--line);
    border-radius:22px;
    padding:18px;
    box-shadow:var(--shadow);
    min-height:320px;
    display:flex;
    flex-direction:column;
}

.card-title{
    font-size:16px;
    font-weight:800;
    margin-bottom:6px;
    letter-spacing:-0.01em;
}

.card-sub{
    color:var(--muted);
    font-size:13px;
    line-height:1.7;
    margin-bottom:12px;
}

.skill-chip-row{
    display:flex;
    flex-wrap:wrap;
    gap:10px;
    margin-top:8px;
    align-content:flex-start;
}

.skill-chip{
    display:inline-flex;
    align-items:center;
    min-height:38px;
    color:white;
    padding:8px 14px;
    border-radius:999px;
    font-size:13px;
    font-weight:700;
    white-space:nowrap;
    box-shadow:0 8px 18px rgba(15,23,42,0.08);
    transition:transform 0.16s ease, box-shadow 0.16s ease;
}

.skill-chip:hover{
    transform:translateY(-1px);
    box-shadow:0 12px 22px rgba(15,23,42,0.12);
}

.live-grid{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:16px;
}

.live-card{
    background:#ffffff;
    border:1px solid var(--line);
    border-radius:22px;
    padding:18px;
    box-shadow:var(--shadow);
    min-height:250px;
}

.live-card-title{
    font-size:16px;
    font-weight:800;
    margin-bottom:12px;
}

.live-item{
    background:#f8fbff;
    border:1px solid var(--line);
    border-left:4px solid var(--primary);
    border-radius:14px;
    padding:14px;
    margin-bottom:10px;
    transition: box-shadow 0.16s ease, transform 0.16s ease;
}

.live-item:hover{
    transform:translateY(-1px);
    box-shadow:var(--shadow);
}

.live-title{
    font-size:14px;
    font-weight:700;
    margin-bottom:4px;
}

.live-text{
    font-size:14px;
    color:#475569;
    line-height:1.75;
}

.improve-wrap{
    background:#ffffff;
    border:1px solid var(--line);
    border-radius:22px;
    padding:18px;
    box-shadow:var(--shadow);
}

.improve-item{
    background:#fbfdff;
    border:1px solid var(--line);
    border-left:4px solid var(--success);
    border-radius:16px;
    padding:14px 16px;
    margin-bottom:12px;
}

.improve-item:last-child{
    margin-bottom:0;
}

.improve-title{
    font-size:15px;
    font-weight:700;
    margin-bottom:6px;
}

.improve-text{
    font-size:14px;
    color:#475569;
    line-height:1.8;
}

.contact-wrap{
    background:#ffffff;
    border:1px solid var(--line);
    border-radius:22px;
    padding:22px;
    box-shadow:var(--shadow);
    margin-top:28px;
}

.contact-grid{
    display:grid;
    grid-template-columns:repeat(3, minmax(0, 1fr));
    gap:14px;
    margin-top:12px;
}

.contact-card{
    background:#f8fbff;
    border:1px solid var(--line);
    border-radius:16px;
    padding:16px;
}

.contact-label{
    font-size:12px;
    font-weight:700;
    color:var(--muted);
    text-transform:uppercase;
    letter-spacing:0.05em;
    margin-bottom:6px;
}

.contact-value{
    font-size:15px;
    font-weight:600;
    color:var(--text);
    word-break:break-word;
}

.contact-value a{
    color:var(--primary);
    text-decoration:none;
    font-weight:700;
}

.contact-value a:hover{
    text-decoration:underline;
}

.footer-note{
    text-align:center;
    color:var(--muted);
    font-size:14px;
    font-weight:700;
    margin-top:18px;
    padding-bottom:10px;
}

.small-note{
    color:var(--muted);
    font-size:13px;
    line-height:1.7;
}

hr{
    border:none;
    border-top:1px solid var(--line);
    margin:24px 0;
}

@media (max-width: 1100px){
    .hero-wrap,
    .digest-grid,
    .live-grid{
        grid-template-columns:1fr 1fr !important;
    }
    .contact-grid{
        grid-template-columns:1fr !important;
    }
}

@media (max-width: 900px){
    .hero-wrap,
    .digest-grid,
    .live-grid{
        grid-template-columns:1fr !important;
    }
    .hero-title{
        font-size:34px;
    }
    .contact-grid{
        grid-template-columns:1fr !important;
    }
}

@media (prefers-reduced-motion: reduce){
    *{
        transition:none !important;
        animation:none !important;
        scroll-behavior:auto !important;
    }
}
</style>
""", unsafe_allow_html=True)


def clamp_score(value):
    try:
        value = float(value)
    except Exception:
        value = 0.0
    return max(0.0, min(100.0, value))


def get_score_label(score):
    score = clamp_score(score)
    if score < 45:
        return "Low Match"
    if score < 70:
        return "Moderate Match"
    return "Strong Match"


def get_score_color(score):
    score = clamp_score(score)
    if score < 45:
        return "#ef4444"
    if score < 70:
        return "#f59e0b"
    return "#10b981"


def circular_progress_svg(percent, color):
    percent = clamp_score(percent)
    radius = 54
    circumference = 2 * 3.14159 * radius
    progress = circumference - (percent / 100.0) * circumference
    return f"""<svg width="150" height="150" viewBox="0 0 150 150" aria-label="Score ring">
<circle cx="75" cy="75" r="{radius}" stroke="#e5e7eb" stroke-width="10" fill="none"></circle>
<circle cx="75" cy="75" r="{radius}" stroke="{color}" stroke-width="10" fill="none"
stroke-linecap="round"
stroke-dasharray="{circumference}"
stroke-dashoffset="{progress}"
transform="rotate(-90 75 75)"></circle>
<text x="75" y="72" text-anchor="middle" class="circle-value">{percent:.0f}%</text>
<text x="75" y="92" text-anchor="middle" class="circle-label">Match</text>
</svg>"""


def render_score_card(title, value, subtitle=""):
    value = clamp_score(value)
    color = get_score_color(value)
    st.markdown(
        f"""<div class="metric-card">
<div class="metric-title">{title}</div>
<div class="circle-wrap">{circular_progress_svg(value, color)}</div>
<div class="metric-sub">{subtitle}</div>
</div>""",
        unsafe_allow_html=True,
    )


def render_skill_card(title, subtitle, items, color):
    chips = (
        "".join(
            f"<span class='skill-chip' style='background:{color};'>{str(item).strip()}</span>"
            for item in items if str(item).strip()
        )
        if items
        else "<div class='small-note'>None</div>"
    )
    st.markdown(
        f"""<div class="group-card">
<div class="card-title">{title}</div>
<div class="card-sub">{subtitle}</div>
<div class="skill-chip-row">{chips}</div>
</div>""",
        unsafe_allow_html=True,
    )


def render_live_card(card_title, items):
    inner = ""
    for title, text, color in items:
        inner += f"""<div class="live-item" style="border-left-color:{color};">
<div class="live-title">{title}</div>
<div class="live-text">{text}</div>
</div>"""
    st.markdown(
        f"""<div class="live-card">
<div class="live-card-title">{card_title}</div>
{inner}
</div>""",
        unsafe_allow_html=True,
    )


def render_improvements_card(suggestions):
    if not suggestions:
        body = "<div class='small-note'>No recommendations available.</div>"
    else:
        body = "".join(
            f"""<div class="improve-item">
<div class="improve-title">Improvement {idx}</div>
<div class="improve-text">{suggestion}</div>
</div>"""
            for idx, suggestion in enumerate(suggestions, start=1)
        )
    st.markdown(
        f"""<div class="improve-wrap">{body}</div>""",
        unsafe_allow_html=True,
    )


def build_live_updates(missing_skills, keyword_score, final_score, semantic_similarity_score):
    updates = []

    if missing_skills:
        updates.append(
            (
                "Update needed",
                "Add stronger proof-based bullets to show practical exposure in the main missing areas.",
                "#ef4444",
            )
        )
    if keyword_score < 50:
        updates.append(
            (
                "Keyword alignment",
                "Rewrite your summary and top projects using more role-specific wording from the job description.",
                "#f59e0b",
            )
        )
    if semantic_similarity_score < 65:
        updates.append(
            (
                "Project framing",
                "Describe the problem, approach, tools, and outcomes more clearly to improve meaning-level fit.",
                "#2563eb",
            )
        )
    if final_score < 70:
        updates.append(
            (
                "Impact visibility",
                "Add measurable outcomes such as accuracy, efficiency, speed, or deployment impact.",
                "#10b981",
            )
        )
    if not updates:
        updates.append(
            (
                "Current status",
                "The resume is already fairly aligned. Focus on stronger project framing and clearer impact statements.",
                "#10b981",
            )
        )
    return updates[:4]


header_left, header_right = st.columns([0.82, 0.18])

with header_left:
    st.markdown("<div class='header-row-title'>AI Resume Analyzer</div>", unsafe_allow_html=True)

with header_right:
    with st.popover("About", use_container_width=True):
        st.markdown("### Project Overview")
        st.write(
            "This project analyzes how well a resume matches a job description and provides practical guidance to improve resume quality for technical roles."
        )

        st.markdown("### How it works")
        st.write(
            "The application accepts a PDF resume and a job description, extracts relevant skills, compares the content semantically, evaluates keyword relevance, and produces fit scores with resume improvement recommendations."
        )

        st.markdown("### Skills used to build this project")
        st.write(
            """
- Python
- FastAPI
- Streamlit
- NLP-based skill extraction
- Sentence Transformers
- Semantic similarity
- Resume parsing
- Dashboard UI/UX design
- Product-style workflow thinking
"""
        )

st.markdown(
    """<div class="hero-wrap">
<div class="hero-main">
<div class="hero-chip">Resume review workflow</div>
<div class="hero-title">Faster resume reviews with actionable insights</div>
<div class="hero-text">
Upload a resume, compare it against a target role, and review fit, score breakdowns,
missing signals, and concrete updates that can improve the quality of the resume.
</div>
<div class="hero-actions">
<div class="hero-action-secondary">Review Resume</div>
<div class="hero-action-secondary">Get Insights</div>
</div>
</div>
<div class="hero-side">
<div class="side-title">What you will get</div>
<div class="side-text">
A concise overview, circular metrics, separate skill cards, live update guidance,
and structured recommendations that help improve alignment for the target role.
</div>
<div class="side-list">
<div class="side-list-item">
<div class="side-list-title">Circular metrics</div>
<div class="side-list-text">Final score, skill fit, semantic fit, and keyword match percentages.</div>
</div>
<div class="side-list-item">
<div class="side-list-title">Hiring-focused review</div>
<div class="side-list-text">A cleaner interpretation of strengths, gaps, and likely improvement areas.</div>
</div>
<div class="side-list-item">
<div class="side-list-title">Valuable updates</div>
<div class="side-list-text">High-signal next steps that improve the resume beyond simple keyword stuffing.</div>
</div>
</div>
</div>
</div>""",
    unsafe_allow_html=True,
)

st.markdown(
    """<div class="digest-grid">
<div class="digest-card">
<div class="digest-kicker">Overview</div>
<div class="digest-title">Structured score breakdown</div>
<div class="digest-text">See a professional, quick-read summary before diving into detailed recommendations.</div>
</div>
<div class="digest-card">
<div class="digest-kicker">Skills</div>
<div class="digest-title">Separate skill cards</div>
<div class="digest-text">Review current skills, role skills, and missing areas in clearly separated zones.</div>
</div>
<div class="digest-card">
<div class="digest-kicker">Activity</div>
<div class="digest-title">Live update guidance</div>
<div class="digest-text">Identify what needs to change now to improve the current resume for this role.</div>
</div>
<div class="digest-card">
<div class="digest-kicker">Next step</div>
<div class="digest-title">Action-oriented improvements</div>
<div class="digest-text">Turn the output into concrete edits for summary, projects, language, and impact statements.</div>
</div>
</div>""",
    unsafe_allow_html=True,
)

st.markdown("<div class='section-title'>Input</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='section-sub'>Upload a resume and paste a job description to generate a fit analysis.</div>",
    unsafe_allow_html=True,
)

resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd = st.text_area("Paste Job Description", height=220)
analyze = st.button("Review Resume")

if analyze:
    if not resume or not jd:
        st.error("Please upload a resume and paste a job description.")
    else:
        with st.spinner("Reviewing resume fit and generating insights..."):
            try:
                files = {"resume": resume}
                data = {"job_description": jd}
                response = requests.post(BACKEND_URL, files=files, data=data, timeout=120)

                if response.status_code != 200:
                    st.error(f"API Error: {response.text}")
                else:
                    result = response.json()

                    final_score = clamp_score(result.get("final_score", 0))
                    skill_match_score = clamp_score(result.get("skill_match_score", 0))
                    semantic_similarity_score = clamp_score(result.get("semantic_similarity_score", 0))
                    keyword_score = clamp_score(result.get("keyword_score", 0))

                    resume_skills = result.get("resume_skills", [])
                    jd_skills = result.get("jd_skills", [])
                    missing_skills = result.get("missing_skills", [])
                    suggestions = result.get("suggestions", [])

                    st.markdown("<hr>", unsafe_allow_html=True)
                    st.markdown("<div class='section-title'>Results</div>", unsafe_allow_html=True)
                    st.markdown(
                        "<div class='section-sub'>Review the high-level summary first, then move into live activity, skill cards, and improvement guidance.</div>",
                        unsafe_allow_html=True,
                    )

                    m1, m2, m3, m4 = st.columns(4)
                    with m1:
                        render_score_card("Final Match Score", final_score, "Overall role fit")
                    with m2:
                        render_score_card("Skill Match", skill_match_score, "Resume vs role skills")
                    with m3:
                        render_score_card("Semantic Score", semantic_similarity_score, "Meaning-level alignment")
                    with m4:
                        render_score_card("Keyword Score", keyword_score, "Keyword relevance")

                    st.markdown(
                        f"<div class='assessment'>Overall Assessment: {result.get('score_band', get_score_label(final_score))}</div>",
                        unsafe_allow_html=True,
                    )

                    st.markdown("<div class='section-title'>Live activity</div>", unsafe_allow_html=True)
                    st.markdown(
                        "<div class='section-sub'>These are the most important updates currently needed to make the resume stronger for this role.</div>",
                        unsafe_allow_html=True,
                    )

                    updates = build_live_updates(
                        missing_skills,
                        keyword_score,
                        final_score,
                        semantic_similarity_score,
                    )

                    left_updates = updates[:2]
                    right_updates = updates[2:]

                    left_col, right_col = st.columns(2)
                    with left_col:
                        render_live_card("Priority updates", left_updates)
                    with right_col:
                        render_live_card("Recommended focus", right_updates if right_updates else left_updates)

                    st.markdown("<div class='section-title'>Skill cards</div>", unsafe_allow_html=True)
                    st.markdown(
                        "<div class='section-sub'>Each skill group sits in its own card so the review is easier to scan and compare.</div>",
                        unsafe_allow_html=True,
                    )

                    c1, c2, c3 = st.columns(3)
                    with c1:
                        render_skill_card(
                            "Resume Skills",
                            "Skills currently found in the resume.",
                            resume_skills,
                            "#3b82f6",
                        )
                    with c2:
                        render_skill_card(
                            "Skills to Add / Highlight",
                            "The main missing or underrepresented signals for the role.",
                            missing_skills,
                            "#ef4444",
                        )
                    with c3:
                        render_skill_card(
                            "Job Description Skills",
                            "Important skills detected from the target role.",
                            jd_skills,
                            "#8b5cf6",
                        )

                    st.markdown("<div class='section-title'>Resume improvements</div>", unsafe_allow_html=True)
                    st.markdown(
                        "<div class='section-sub'>Use these recommendations as the next editing pass for summary, project bullets, evidence, and positioning.</div>",
                        unsafe_allow_html=True,
                    )

                    render_improvements_card(suggestions)

            except Exception as e:
                st.error(f"Error: {str(e)}")

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>Contact</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='section-sub'>Get in touch for collaboration, project discussions, or portfolio opportunities.</div>",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="contact-wrap">
    <div class="contact-grid">
        <div class="contact-card">
            <div class="contact-label">Email</div>
            <div class="contact-value">abdulxrahman.ai@gmail.com</div>
        </div>
        <div class="contact-card">
            <div class="contact-label">Phone</div>
            <div class="contact-value">+1 (773) 996-2993</div>
        </div>
        <div class="contact-card">
            <div class="contact-label">GitHub</div>
            <div class="contact-value">
                <a href="https://github.com/abdulxrahman-ai" target="_blank">github.com/abdulxrahman-ai</a>
            </div>
        </div>
    </div>
</div>
<div class="footer-note">By Abdul Rahman</div>
""",
    unsafe_allow_html=True,
)
