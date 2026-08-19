from pathlib import Path

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

from data.training_data import TRAINING_DATA

MODEL_DIR = Path(__file__).resolve().parent / "model"
MODEL_DIR.mkdir(exist_ok=True)
MODEL_PATH = MODEL_DIR / "clause_classifier.joblib"


def main():
    texts = [t for t, _ in TRAINING_DATA]
    labels = [l for _, l in TRAINING_DATA]

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(stop_words="english", ngram_range=(1, 2), min_df=1)),
        ("clf", LogisticRegression(max_iter=2000, class_weight="balanced")),
    ])

    # Leave-one-out-ish cross-validation report so we have an honest accuracy
    # number to quote in the report/viva instead of just "it works on my demo".
    label_counts = {l: labels.count(l) for l in set(labels)}
    min_class_count = min(label_counts.values())
    n_splits = min(3, min_class_count)

    if n_splits >= 2:
        skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
        preds = cross_val_predict(pipeline, texts, labels, cv=skf)
        print("=== Cross-validated classification report ===")
        print(classification_report(labels, preds, zero_division=0))
    else:
        print("Not enough examples per class for cross-validation; skipping report.")

    # Fit final model on ALL data for actual use
    pipeline.fit(texts, labels)
    joblib.dump(pipeline, MODEL_PATH)
    print(f"\nSaved trained model to {MODEL_PATH}")
    print(f"Trained on {len(texts)} labeled clauses across {len(set(labels))} categories:")
    for label, count in sorted(label_counts.items()):
        print(f"  - {label}: {count}")


if __name__ == "__main__":
    main()
