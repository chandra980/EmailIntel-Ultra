from emailintel.core.evidence import finalize_evidence
from emailintel.core.models import Evidence, FindingStatus


def test_hash_and_family_stable():
    first = Evidence(
        id="EVD-A", scan_id="S", provider="p", category="x",
        title="T", status=FindingStatus.FOUND, confidence=.8,
        url="https://example.com/a", details={"a": 1},
    )
    second = Evidence(
        id="EVD-B", scan_id="S2", provider="p", category="x",
        title="T", status=FindingStatus.FOUND, confidence=.8,
        url="https://example.com/a", details={"a": 1},
    )
    finalize_evidence(first)
    finalize_evidence(second)
    assert first.normalized_hash == second.normalized_hash
    assert first.family_id == second.family_id
