from emailintel.core.planner import build_plan
from emailintel.core.validator import validate_email


def profile(email: str):
    result = validate_email(email)
    assert result.profile
    return result.profile


def test_consumer_plan_skips_org():
    plan = build_plan(profile("person@gmail.com"), "balanced")
    assert plan.target_type == "consumer-email"
    assert "organization" in plan.excluded_categories
    assert "rdap" not in plan.selected_categories


def test_custom_plan_has_rdap():
    plan = build_plan(profile("person@example.com"), "deep")
    assert plan.target_type == "custom-domain-email"
    assert "rdap" in plan.selected_categories
