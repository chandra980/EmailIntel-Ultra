from emailintel.core.database import load_scan, save_scan
from emailintel.core.models import ScanPlan, ScanResult, TargetProfile


def test_save_load(tmp_path):
    target = TargetProfile(
        "a@example.com", "a@example.com", "a", "example.com",
        "custom-domain", False, False, False,
    )
    plan = ScanPlan("custom-domain-email", [], [], {}, "fast")
    result = ScanResult("EI-X", target, "fast", "a", "b", 0.1, [], [], plan)
    db = tmp_path / "x.db"
    save_scan(db, result)
    loaded = load_scan(db, "EI-X")
    assert loaded and loaded["target"]["normalized"] == "a@example.com"
