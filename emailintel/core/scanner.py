from __future__ import annotations

import asyncio
import time
from collections.abc import Callable
from datetime import datetime, timezone
from typing import Any

from emailintel.providers import providers
from .evidence import evidence_id, finalize_evidence, scan_id
from .models import Evidence, FindingStatus, ScanResult, TargetProfile
from .planner import build_plan

ProgressCallback = Callable[[dict[str, Any]], None]


def _emit(callback: ProgressCallback | None, event: dict[str, Any]) -> None:
    if callback is None:
        return
    try:
        callback(event)
    except Exception:
        # Terminal/UI rendering must never crash the investigation engine.
        pass


async def scan(
    target: TargetProfile,
    mode: str = "balanced",
    max_concurrency: int = 8,
    progress: ProgressCallback | None = None,
) -> ScanResult:
    sid = scan_id()
    started_dt = datetime.now(timezone.utc)
    started = time.perf_counter()
    plan = build_plan(target, mode)

    _emit(progress, {
        "event": "plan",
        "scan_id": sid,
        "target": target.normalized,
        "target_type": plan.target_type,
        "mode": mode,
        "selected_categories": plan.selected_categories,
    })

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
            "source": "Local deterministic validation",
        },
    ))
    _emit(progress, {
        "event": "result",
        "provider": validation.provider,
        "category": validation.category,
        "source_name": "Local deterministic validation",
        "source_homepage": "",
        "query_reference": "",
        "status": validation.status.value,
        "title": validation.title,
        "latency_ms": 0,
        "url": "",
        "evidence_id": validation.id,
    })

    selected = [provider for provider in providers() if provider.eligible(target, plan)]
    semaphore = asyncio.Semaphore(max(1, max_concurrency))

    _emit(progress, {
        "event": "provider_set",
        "count": len(selected),
        "providers": [provider.source_metadata(target) for provider in selected],
    })

    async def run(provider):
        meta = provider.source_metadata(target)
        _emit(progress, {"event": "start", **meta})
        async with semaphore:
            item = await provider.query(target, sid)
        _emit(progress, {
            "event": "result",
            **meta,
            "status": item.status.value,
            "title": item.title,
            "latency_ms": item.latency_ms or 0,
            "url": item.url or meta.get("query_reference", ""),
            "evidence_id": item.id,
        })
        return item

    queried = await asyncio.gather(*(run(provider) for provider in selected))
    evidence = [validation, *queried]
    errors = [
        f"{item.provider}: {item.error}"
        for item in evidence
        if item.status == FindingStatus.ERROR and item.error
    ]
    finished_dt = datetime.now(timezone.utc)

    result = ScanResult(
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
    _emit(progress, {
        "event": "complete",
        "scan_id": sid,
        "duration_seconds": result.duration_seconds,
        "providers_completed": len(evidence),
        "errors": len(errors),
    })
    return result
