from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compute_semantic_similarity(resume_text: str, job_description: str) -> float:
    if not resume_text or not job_description:
        return 0.0

    vectorizer = TfidfVectorizer(stop_words="english")

    vectors = vectorizer.fit_transform([resume_text, job_description])

    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    return max(0.0, min(100.0, float(score) * 100))
