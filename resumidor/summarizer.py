import re

_SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")


def summarize(text: str, max_sentences: int = 3) -> str:
    """Retorna um resumo com no máximo `max_sentences` frases."""
    cleaned = " ".join(text.split())
    if not cleaned:
        return ""

    sentences = [s.strip() for s in _SENTENCE_SPLIT.split(cleaned) if s.strip()]
    return " ".join(sentences[:max_sentences])
