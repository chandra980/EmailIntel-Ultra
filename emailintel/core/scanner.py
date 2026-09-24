from __future__ import annotations

import asyncio
import time
from datetime import datetime, timezone

from emailintel.providers import providers
from .evidence import evidence_id, finalize_evidence, scan_id
from .models import Evidence, FindingStatus, ScanResult, TargetProfile
from .planner import build_plan


async def scan(
    target: TargetProfile,
    mode: str = "balanced",
    max_concurrency: int = 8,
) -> ScanResult:
    sid = scan_id()
    started_dt = datetime.now(timezone.utc)
    started = time.perf_counter()
    plan = build_plan(target, mode)

    validation = finalize_evidence(Evidence(
        id=evidence_id(),
        scan_id=sid,
        provider="email-validator",
        category="validation",
        title="Email syntax and target classification",
        status=FindingStatus.VERIFIED,
        confidence=0.99,
        evidence=f"Normalized as {target.normalized}",
        details={
            "local_part": target.local_part,
            "domain": target.domain,
            "provider_type": target.provider_type,
            "is_free_mail": target.is_free_mail,
            "is_role_based": target.is_role_based,
            "is_disposable": target.is_disposable,
        },
    ))

    selected = [provider for provider in providers() if provider.eligible(target, plan)]
    semaphore = asyncio.Semaphore(max(1, max_concurrency))

    async def run(provider):
        async with semaphore:
            return await provider.query(target, sid)

    queried = await asyncio.gather(*(run(provider) for provider in selected))
    evidence = [validation, *queried]
    errors = [
        f"{item.provider}: {item.error}"
        for item in evidence
        if item.status == FindingStatus.ERROR and item.error
    ]
    finished_dt = datetime.now(timezone.utc)

    return ScanResult(
        scan_id=sid,
        target=target,
        mode=mode,
        started_at=started_dt.isoformat(),
        finished_at=finished_dt.isoformat(),
        duration_seconds=round(time.perf_counter() - started, 3),
        evidence=list(evidence),
        errors=errors,
        plan=plan,
    )
