from __future__ import annotations

from .models import ScanPlan, TargetProfile


def build_plan(target: TargetProfile, mode: str = "balanced") -> ScanPlan:
    if target.is_free_mail:
        selected = ["validation", "dns", "public-profile", "public-key"]
        excluded = ["organization", "corporate-mail-posture"]
        reasons = {
            "validation": "Always validates syntax and provider characteristics.",
            "dns": "Confirms public mail-domain infrastructure without probing the mailbox.",
            "public-profile": "Checks anonymous public identity systems where exact email matching is supported.",
            "public-key": "Checks public-key directories for published email identities.",
            "organization": "Shared consumer-mail domains do not describe the individual organization.",
            "corporate-mail-posture": "Shared-provider security posture is not attributed to the individual.",
        }
        target_type = "consumer-email"
    else:
        selected = [
            "validation", "dns", "rdap", "organization",
            "corporate-mail-posture", "public-profile", "public-key",
        ]
        excluded = []
        reasons = {
            "validation": "Always validates syntax and target characteristics.",
            "dns": "Custom domains provide useful mail and DNS infrastructure context.",
            "rdap": "Public RDAP can describe registration metadata for the custom domain.",
            "organization": "A custom domain can support evidence-backed organization context.",
            "corporate-mail-posture": "SPF/DMARC/MTA-STS/TLS-RPT posture is meaningful for custom domains.",
            "public-profile": "Anonymous public identity systems may expose exact public references.",
            "public-key": "Public-key directories may contain published email identities.",
        }
        target_type = "custom-domain-email"

    if mode == "fast":
        keep = {"validation", "dns", "public-profile"}
        selected = [item for item in selected if item in keep]

    return ScanPlan(target_type, selected, excluded, reasons, mode)
