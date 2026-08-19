

from pathlib import Path
import joblib

MODEL_PATH = Path(__file__).resolve().parent.parent / "model" / "clause_classifier.joblib"

_pipeline = None


def _load():
    global _pipeline
    if _pipeline is None:
        if not MODEL_PATH.exists():
            raise RuntimeError(
                f"Model not found at {MODEL_PATH}. Run `python train_classifier.py` first."
            )
        _pipeline = joblib.load(MODEL_PATH)
    return _pipeline


def classify_clause(text: str) -> tuple[str, float]:
    """Returns (predicted_label, confidence 0-1)."""
    pipeline = _load()
    proba = pipeline.predict_proba([text])[0]
    classes = pipeline.classes_
    best_idx = proba.argmax()
    return classes[best_idx], float(proba[best_idx])


def classify_batch(texts: list[str]) -> list[tuple[str, float]]:
    pipeline = _load()
    probas = pipeline.predict_proba(texts)
    classes = pipeline.classes_
    results = []
    for row in probas:
        best_idx = row.argmax()
        results.append((classes[best_idx], float(row[best_idx])))
    return results
