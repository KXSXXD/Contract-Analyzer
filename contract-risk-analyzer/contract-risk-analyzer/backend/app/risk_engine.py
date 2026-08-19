

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

with open(DATA_DIR / "clause_corpus.json", encoding="utf-8") as f:
    CLAUSE_CORPUS: dict[str, list[str]] = json.load(f)

with open(DATA_DIR / "red_flags.json", encoding="utf-8") as f:
    RED_FLAGS = json.load(f)

# Fit one shared vectorizer over the entire reference corpus so clause text
# and reference text live in the same vector space.
_ALL_REFERENCE_TEXTS = [t for texts in CLAUSE_CORPUS.values() for t in texts]
_VECTORIZER = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
_REFERENCE_MATRIX = _VECTORIZER.fit_transform(_ALL_REFERENCE_TEXTS)

# Map from row index in _REFERENCE_MATRIX back to category
_REFERENCE_CATEGORY_BY_ROW = []
for cat, texts in CLAUSE_CORPUS.items():
    _REFERENCE_CATEGORY_BY_ROW.extend([cat] * len(texts))


@dataclass
class RiskFlag:
    phrase: str
    severity: int
    explanation: str


@dataclass
class ClauseRisk:
    deviation_score: float          # 0-100, higher = more unusual vs standard
    red_flag_score: float           # 0-100, higher = more red-flag phrases
    overall_score: float            # 0-100 combined
    level: str                      # "Low" | "Medium" | "High"
    flags: list[RiskFlag] = field(default_factory=list)
    closest_reference: str | None = None
    similarity_to_closest: float = 0.0


def _template_deviation(text: str, category: str) -> tuple[float, str | None, float]:
    """Returns (deviation_score_0_100, closest_reference_text, raw_similarity)."""
    if category not in CLAUSE_CORPUS:
        return 50.0, None, 0.0  # unknown category -> neutral/unknown risk

    clause_vec = _VECTORIZER.transform([text])
    sims = cosine_similarity(clause_vec, _REFERENCE_MATRIX)[0]

    # restrict to rows belonging to this category
    best_sim = 0.0
    best_ref = None
    for row_idx, cat in enumerate(_REFERENCE_CATEGORY_BY_ROW):
        if cat == category and sims[row_idx] > best_sim:
            best_sim = sims[row_idx]
            best_ref = _ALL_REFERENCE_TEXTS[row_idx]

    deviation = max(0.0, min(100.0, (1.0 - best_sim) * 100))
    return deviation, best_ref, best_sim


def _red_flag_matches(text: str, category: str) -> list[RiskFlag]:
    lowered = text.lower()
    matches: list[RiskFlag] = []

    for rule in RED_FLAGS.get("global", []):
        if re.search(re.escape(rule["pattern"]), lowered):
            matches.append(RiskFlag(rule["pattern"], rule["severity"], rule["explanation"]))

    for rule in RED_FLAGS.get("by_category", {}).get(category, []):
        if re.search(re.escape(rule["pattern"]), lowered):
            matches.append(RiskFlag(rule["pattern"], rule["severity"], rule["explanation"]))

    return matches


def _score_to_level(score: float) -> str:
    if score >= 66:
        return "High"
    if score >= 33:
        return "Medium"
    return "Low"


def score_clause(text: str, category: str) -> ClauseRisk:
    deviation, closest_ref, similarity = _template_deviation(text, category)
    flags = _red_flag_matches(text, category)

    # Each severity point ~ 12 risk points, capped at 100.
    red_flag_score = min(100.0, sum(f.severity for f in flags) * 12)

    # Weighted blend: red flags are more directly interpretable/reliable
    # signal than raw similarity, so weight them slightly higher.
    overall = round(0.45 * deviation + 0.55 * red_flag_score, 1) if flags else round(deviation, 1)
    # If there ARE red flags, floor the score so a single severe flag can't
    # be diluted away by a high similarity score.
    if flags:
        overall = max(overall, min(100.0, max(f.severity for f in flags) * 20))

    return ClauseRisk(
        deviation_score=round(deviation, 1),
        red_flag_score=round(red_flag_score, 1),
        overall_score=overall,
        level=_score_to_level(overall),
        flags=flags,
        closest_reference=closest_ref,
        similarity_to_closest=round(similarity, 3),
    )


def score_contract(clause_scores: list[float]) -> tuple[float, str]:
    """Overall contract risk: weighted toward the worst clauses, not just the
    average, because one brutal indemnity clause matters more than ten benign
    boilerplate ones."""
    if not clause_scores:
        return 0.0, "Low"
    sorted_scores = sorted(clause_scores, reverse=True)
    top_n = sorted_scores[: max(1, len(sorted_scores) // 3)]  # worst third
    weighted = 0.6 * (sum(top_n) / len(top_n)) + 0.4 * (sum(sorted_scores) / len(sorted_scores))
    weighted = round(min(100.0, weighted), 1)
    return weighted, _score_to_level(weighted)
