from collections import Counter

from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

from app.extraction import segment_contract
from app.classifier import classify_batch
from app.risk_engine import score_clause, score_contract
from app.file_reader import extract_text
from app.schemas import AnalyzeResponse, ClauseOut, FlagOut

app = FastAPI(
    title="Contract Risk Analyzer API",
    description="Extracts clauses from a contract, classifies each by type, "
                "and scores risk by comparing wording against a corpus of "
                "standard/fair reference clauses plus rule-based red flags.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def _analyze_text(text: str, filename: Optional[str]) -> AnalyzeResponse:
    raw_clauses = segment_contract(text)
    if not raw_clauses:
        raise HTTPException(status_code=400, detail="Could not extract any clauses from this document.")

    texts = [c.text for c in raw_clauses]
    predictions = classify_batch(texts)

    clause_outs: list[ClauseOut] = []
    category_counts: Counter = Counter()
    all_scores: list[float] = []

    for raw, (category, confidence) in zip(raw_clauses, predictions):
        risk = score_clause(raw.text, category)
        category_counts[category] += 1
        all_scores.append(risk.overall_score)

        clause_outs.append(ClauseOut(
            index=raw.index,
            heading=raw.heading,
            text=raw.text,
            category=category,
            category_confidence=round(confidence, 3),
            deviation_score=risk.deviation_score,
            red_flag_score=risk.red_flag_score,
            risk_score=risk.overall_score,
            risk_level=risk.level,
            flags=[FlagOut(phrase=f.phrase, severity=f.severity, explanation=f.explanation) for f in risk.flags],
            closest_reference=risk.closest_reference,
            similarity_to_closest=risk.similarity_to_closest,
        ))

    overall_score, overall_level = score_contract(all_scores)

    return AnalyzeResponse(
        filename=filename,
        overall_risk_score=overall_score,
        overall_risk_level=overall_level,
        clause_count=len(clause_outs),
        category_breakdown=dict(category_counts),
        clauses=clause_outs,
    )


@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze_file(file: UploadFile = File(...)):
    content = await file.read()
    try:
        text = extract_text(file.filename, content)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return _analyze_text(text, file.filename)


@app.post("/analyze-text", response_model=AnalyzeResponse)
async def analyze_text(payload: str = Form(...)):
    return _analyze_text(payload, filename=None)


@app.get("/health")
def health():
    return {"status": "ok"}
