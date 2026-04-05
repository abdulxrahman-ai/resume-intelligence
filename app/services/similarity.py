from functools import lru_cache
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


@lru_cache(maxsize=1)
def get_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


def compute_semantic_similarity(resume_text: str, job_description: str) -> float:
    if not resume_text or not job_description:
        return 0.0

    model = get_model()
    embeddings = model.encode([resume_text, job_description])

    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return max(0.0, min(100.0, float(score) * 100))
