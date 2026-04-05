from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ❌ Disabled temporarily to fix deployment error
# from app.routes.match import router as match_router

app = FastAPI(
    title="AI Resume Analyzer + Job Matcher",
    version="3.0.0",
    description="Analyze resume-job fit using skill extraction, keyword overlap, and semantic similarity.",
)

# CORS (allow frontend to talk to backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ❌ Disabled temporarily
# app.include_router(match_router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Resume Job Matcher API is running."}

# Health check endpoint (important for Render)
@app.get("/healthz")
def healthz():
    return {"status": "ok"}
