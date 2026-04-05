# AI Resume Analyzer + Job Matcher

An AI-powered web application that analyzes how well a resume matches a job description using NLP, regex-based skill extraction, semantic similarity, and keyword relevance scoring.

## Features

- Upload resume in PDF format
- Paste any job description
- Extract skills from both resume and job description
- Detect missing skills
- Compute:
  - skill match score
  - semantic similarity score
  - keyword relevance score
  - final weighted match score
- Generate tailored suggestions for resume improvement
- Clean and interactive Streamlit UI

## Tech Stack

- Python
- FastAPI
- Streamlit
- PyMuPDF
- sentence-transformers
- scikit-learn
- regex / rule-based NLP

## Run Locally

### 1. Create virtual environment
```bash
python -m venv venv
```

### 2. Activate environment
```bash
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run backend
```bash
uvicorn app.main:app --reload
```

### 5. Run frontend
```bash
streamlit run frontend/streamlit_app.py
```
