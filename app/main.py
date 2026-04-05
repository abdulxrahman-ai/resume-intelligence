from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.match import router as match_router

app = FastAPI(
    title="AI Resume Analyzer + Job Matcher",
    version="3.0.0",
    description="Analyze resume-job fit using skill extraction, keyword overlap, and semantic similarity.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(match_router)

@app.get("/")
def root():
    return {"message": "Resume Job Matcher API is running."}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/healthz")
def healthz():
    return {"status": "ok"}
