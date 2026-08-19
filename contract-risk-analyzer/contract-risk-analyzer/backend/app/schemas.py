from pydantic import BaseModel


class FlagOut(BaseModel):
    phrase: str
    severity: int
    explanation: str


class ClauseOut(BaseModel):
    index: int
    heading: str
    text: str
    category: str
    category_confidence: float
    deviation_score: float
    red_flag_score: float
    risk_score: float
    risk_level: str
    flags: list[FlagOut]
    closest_reference: str | None
    similarity_to_closest: float


class AnalyzeResponse(BaseModel):
    filename: str | None
    overall_risk_score: float
    overall_risk_level: str
    clause_count: int
    category_breakdown: dict[str, int]
    clauses: list[ClauseOut]
