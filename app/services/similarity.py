from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from app.config import SEMANTIC_MODEL_NAME

model = SentenceTransformer(SEMANTIC_MODEL_NAME)


def compute_semantic_similarity(text1: str, text2: str) -> float:
    """
    Return semantic similarity as percentage.
    """
    if not text1.strip() or not text2.strip():
        return 0.0

    embeddings = model.encode([text1, text2], normalize_embeddings=True)
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]

    similarity = max(0.0, min(float(similarity), 1.0))
    return round(similarity * 100, 2)
