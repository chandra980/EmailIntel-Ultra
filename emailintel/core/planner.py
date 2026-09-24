from __future__ import annotations

from .models import ScanPlan, TargetProfile


def build_plan(target: TargetProfile, mode: str = "balanced") -> ScanPlan:
    if target.is_free_mail:
        selected = [
            "validation",
            "dns",
            "developer",
            "public-profile",
            "public-key",
        ]
        excluded = [
            "rdap",
            "organization",
            "corporate-mail-posture",
            "certificate-transparency",
        ]
        reasons = {
            "validation": "Always validates syntax and provider characteristics.",
            "dns": "Confirms public mail-domain infrastructure without probing the mailbox.",
            "developer": "Exact public developer/commit references can apply to consumer email addresses.",
            "public-profile": "Checks anonymous public identity systems where exact email matching is supported.",
            "public-key": "Checks public-key directories for explicitly published email identities.",
            "rdap": "Shared consumer-mail domain registration describes the provider, not the individual.",
            "organization": "Shared consumer-mail domains do not describe the individual organization.",
            "corporate-mail-posture": "Shared-provider security posture is not attributed to the individual.",
            "certificate-transparency": "Certificates for a shared mail provider domain are not useful identity evidence.",
        }
        target_type = "consumer-email"
    else:
        selected = [
            "validation",
            "dns",
            "rdap",
            "developer",
            "organization",
            "corporate-mail-posture",
            "certificate-transparency",
            "public-profile",
            "public-key",
        ]
        excluded = []
        reasons = {
            "validation": "Always validates syntax and target characteristics.",
            "dns": "Custom domains provide useful mail and DNS infrastructure context.",
            "rdap": "Public RDAP can describe registration metadata for the custom domain.",
            "developer": "Exact public commit references may associate the address with open-source development.",
            "organization": "A custom domain can support evidence-backed organization context.",
            "corporate-mail-posture": "SPF/DMARC/MTA-STS/TLS-RPT posture is meaningful for custom domains.",
            "certificate-transparency": "Public certificate transparency can reveal domain certificate history and related hostnames.",
            "public-profile": "Anonymous public identity systems may expose exact public references.",
            "public-key": "Public-key directories may contain explicitly published email identities.",
        }
        target_type = "custom-domain-email"

    if mode == "fast":
        keep = {"validation", "dns", "developer", "public-profile"}
        selected = [item for item in selected if item in keep]

    return ScanPlan(target_type, selected, excluded, reasons, mode)
