
import re
from dataclasses import dataclass


HEADING_PATTERN = re.compile(
    r"""
    ^\s*
    (
        \d+(\.\d+)*\.?          # 1.  or 1.1  or 1.1.2
        |[A-Z]+\.               # A.  B.  C.
        |\([a-zA-Z0-9]+\)       # (a) (1) (iv)
        |ARTICLE\s+[IVXLC\d]+   # ARTICLE IV
        |SECTION\s+\d+          # SECTION 3
    )
    \s+
    """,
    re.VERBOSE | re.MULTILINE,
)

MIN_CLAUSE_LENGTH = 40  # characters; shorter fragments are treated as noise


@dataclass
class RawClause:
    index: int
    heading: str
    text: str


def _split_by_headings(text: str) -> list[str]:
    positions = [m.start() for m in HEADING_PATTERN.finditer(text)]
    if len(positions) < 2:
        return []
    positions.append(len(text))
    chunks = [text[positions[i]:positions[i + 1]].strip() for i in range(len(positions) - 1)]
    return [c for c in chunks if len(c) >= MIN_CLAUSE_LENGTH]


def _split_by_paragraphs(text: str) -> list[str]:
    chunks = re.split(r"\n\s*\n", text)
    return [c.strip() for c in chunks if len(c.strip()) >= MIN_CLAUSE_LENGTH]


def _heading_of(chunk: str) -> str:
    """Best-effort short label for display — first line or first ~8 words."""
    first_line = chunk.split("\n", 1)[0].strip()
    if len(first_line) <= 80:
        return first_line
    words = chunk.split()
    return " ".join(words[:8]) + "..."


def segment_contract(text: str) -> list[RawClause]:
    text = text.replace("\r\n", "\n")
    chunks = _split_by_headings(text)
    if not chunks:
        chunks = _split_by_paragraphs(text)
    if not chunks:
        chunks = [text.strip()] if text.strip() else []

    return [
        RawClause(index=i, heading=_heading_of(c), text=c)
        for i, c in enumerate(chunks)
    ]
