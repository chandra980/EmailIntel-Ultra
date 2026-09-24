from __future__ import annotations

import re
from dataclasses import dataclass

from .models import TargetProfile

EMAIL_RE = re.compile(
    r"^(?=.{3,254}$)([A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+)@([A-Za-z0-9.-]+\.[A-Za-z]{2,63})$"
)
FREE_MAIL = {
    "gmail.com", "googlemail.com", "outlook.com", "hotmail.com", "live.com",
    "yahoo.com", "proton.me", "protonmail.com", "icloud.com", "me.com",
}
ROLE_PREFIXES = {
    "admin", "administrator", "support", "security", "info", "contact",
    "sales", "billing", "abuse", "postmaster", "webmaster",
}
DISPOSABLE_HINTS = {
    "mailinator.com", "guerrillamail.com", "10minutemail.com", "tempmail.com",
}


@dataclass(slots=True)
class ValidationResult:
    valid: bool
    reason: str
    profile: TargetProfile | None = None


def validate_email(value: str) -> ValidationResult:
    raw = value.strip()
    match = EMAIL_RE.match(raw)
    if not match:
        return ValidationResult(False, "Email syntax is invalid")
    local, domain = match.group(1), match.group(2).lower().rstrip(".")
    normalized = f"{local}@{domain}"
    provider_type = "free-mail" if domain in FREE_MAIL else "custom-domain"
    profile = TargetProfile(
        original=raw,
        normalized=normalized,
        local_part=local,
        domain=domain,
        provider_type=provider_type,
        is_free_mail=domain in FREE_MAIL,
        is_role_based=local.lower() in ROLE_PREFIXES,
        is_disposable=domain in DISPOSABLE_HINTS,
    )
    return ValidationResult(True, "valid", profile)
