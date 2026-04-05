import re


def clean_text(text: str) -> str:
    """
    Clean text while preserving common technical terms.
    """
    if not text or not isinstance(text, str):
        return ""

    text = text.lower()
    text = text.replace("\u00a0", " ")
    text = re.sub(r"[\r\n\t]+", " ", text)

    # Keep letters, numbers, spaces, and some technical punctuation
    text = re.sub(r"[^a-z0-9\s\+\#\.\-/]", " ", text)

    # Normalize repeated spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


def tokenize_text(text: str) -> list[str]:
    """
    Simple tokenizer for keyword overlap.
    """
    cleaned = clean_text(text)
    if not cleaned:
        return []
    return cleaned.split()
