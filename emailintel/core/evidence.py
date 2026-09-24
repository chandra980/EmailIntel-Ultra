from __future__ import annotations

import hashlib
import json
import uuid
from datetime import datetime, timezone
from urllib.parse import urlparse

from .models import Evidence, Freshness


def evidence_id() -> str:
    return "EVD-" + uuid.uuid4().hex[:8].upper()


def scan_id() -> str:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d")
    return f"EI-{stamp}-{uuid.uuid4().hex[:6].upper()}"


def compute_hash(ev: Evidence) -> str:
    canonical = json.dumps(
        {
            "provider": ev.provider,
            "category": ev.category,
            "title": ev.title,
            "url": ev.url,
            "evidence": ev.evidence,
            "details": ev.details,
        },
        sort_keys=True,
        ensure_ascii=False,
        default=str,
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def assign_family(ev: Evidence) -> str:
    host = (urlparse(ev.url).hostname or "unknown").lower() if ev.url else ev.provider.lower()
    base = f"{host}|{ev.category}|{ev.title.strip().lower()}"
    return "FAM-" + hashlib.sha256(base.encode()).hexdigest()[:8].upper()


def infer_freshness(observed_at: str | None) -> Freshness:
    if not observed_at:
        return Freshness.UNKNOWN
    try:
        dt = datetime.fromisoformat(observed_at.replace("Z", "+00:00"))
        now = datetime.now(timezone.utc)
        days = max(0, (now - dt).days)
    except ValueError:
        return Freshness.UNKNOWN
    if days <= 30:
        return Freshness.CURRENT
    if days <= 365:
        return Freshness.RECENT
    if days <= 365 * 3:
        return Freshness.AGING
    return Freshness.HISTORICAL


def finalize_evidence(ev: Evidence) -> Evidence:
    ev.freshness = infer_freshness(ev.observed_at)
    ev.family_id = assign_family(ev)
    ev.normalized_hash = compute_hash(ev)
    return ev
