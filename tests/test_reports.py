from emailintel.core.models import Evidence, FindingStatus, ScanPlan, ScanResult, TargetProfile
from emailintel.reports import write_csv, write_html, write_json, write_text


def sample():
    target = TargetProfile(
        "a@example.com", "a@example.com", "a", "example.com",
        "custom-domain", False, False, False,
    )
    evidence = Evidence(
        id="EVD-1", scan_id="EI-1", provider="test",
        category="validation", title="Safe <title>",
        status=FindingStatus.VERIFIED, confidence=.99,
        url="https://example.com/?x=1&y=2",
        normalized_hash="abc", family_id="FAM-1",
    )
    plan = ScanPlan("custom-domain-email", ["validation"], [], {"validation": "test"}, "fast")
    return ScanResult(
        "EI-1", target, "fast",
        "2026-01-01T00:00:00+00:00", "2026-01-01T00:00:01+00:00",
        1.0, [evidence], [], plan,
    )


def test_all_reports(tmp_path):
    result = sample()
    html_path = write_html(result, tmp_path / "r.html")
    json_path = write_json(result, tmp_path / "r.json")
    csv_path = write_csv(result, tmp_path / "r.csv")
    text_path = write_text(result, tmp_path / "r.txt")
    assert "Safe &lt;title&gt;" in html_path.read_text(encoding="utf-8")
    assert json_path.exists() and csv_path.exists() and text_path.exists()
