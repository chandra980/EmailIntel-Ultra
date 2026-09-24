from __future__ import annotations


def confidence_label(score: float) -> str:
    if score >= 0.95:
        return "VERIFIED"
    if score >= 0.80:
        return "HIGH"
    if score >= 0.50:
        return "MEDIUM"
    if score > 0:
        return "LOW"
    return "UNKNOWN"


def explain_confidence(
    score: float,
    *,
    direct_match: bool,
    direct_source: bool,
    independently_confirmed: bool,
    stale: bool,
) -> dict:
    factors: list[str] = []
    reducers: list[str] = []
    if direct_match:
        factors.append("Exact normalized email or domain match")
    if direct_source:
        factors.append("Direct public source")
    if independently_confirmed:
        factors.append("Independent confirmation available")
    if stale:
        reducers.append("Evidence is historical, reducing current relevance")
    return {
        "score": round(score, 3),
        "label": confidence_label(score),
        "supporting": factors,
        "reducing": reducers,
    }
