from __future__ import annotations

import hashlib
import time

import httpx

from emailintel.core.evidence import evidence_id, finalize_evidence
from emailintel.core.models import Evidence, FindingStatus, TargetProfile
from .base import BaseProvider


class GravatarProvider(BaseProvider):
    name = "gravatar-public-profile"
    category = "public-profile"

    async def query(self, target: TargetProfile, scan_id: str) -> Evidence:
        started = time.perf_counter()
        digest = hashlib.sha256(target.normalized.strip().lower().encode()).hexdigest()
        url = f"https://api.gravatar.com/v3/profiles/{digest}"
        try:
            async with httpx.AsyncClient(
                timeout=5.0,
                follow_redirects=True,
                headers={"User-Agent": "EmailIntel-Ultra/0.1"},
            ) as client:
                response = await client.get(url)
            if response.status_code == 200:
                data = response.json()
                safe_keys = [
                    "display_name", "profile_url", "avatar_url",
                    "location", "description",
                ]
                details = {
                    key: data.get(key)
                    for key in safe_keys
                    if data.get(key) is not None
                }
                status = FindingStatus.FOUND
                confidence = 0.88
                title = "Public Gravatar profile associated with normalized email hash"
                error = None
            elif response.status_code == 404:
                details = {"http_status": 404}
                status = FindingStatus.NOT_FOUND
                confidence = 0.8
                title = "No public Gravatar profile returned"
                error = None
            else:
                details = {"http_status": response.status_code}
                status = FindingStatus.UNAVAILABLE
                confidence = 0.0
                title = "Gravatar source unavailable"
                error = f"HTTP {response.status_code}"
        except (httpx.HTTPError, ValueError) as exc:
            details = {}
            status = FindingStatus.ERROR
            confidence = 0.0
            title = "Gravatar lookup failed"
            error = str(exc)
        evidence = Evidence(
            id=evidence_id(),
            scan_id=scan_id,
            provider=self.name,
            category=self.category,
            title=title,
            status=status,
            confidence=confidence,
            url=url,
            details=details,
            error=error,
            latency_ms=int((time.perf_counter() - started) * 1000),
            provider_version=self.version,
            parser_version=self.parser_version,
        )
        return finalize_evidence(evidence)
