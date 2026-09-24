from __future__ import annotations

import time

import httpx

from emailintel.core.evidence import evidence_id, finalize_evidence
from emailintel.core.models import Evidence, FindingStatus, TargetProfile
from .base import BaseProvider


class RDAPProvider(BaseProvider):
    name = "public-rdap"
    category = "rdap"

    async def query(self, target: TargetProfile, scan_id: str) -> Evidence:
        started = time.perf_counter()
        url = f"https://rdap.org/domain/{target.domain}"
        try:
            async with httpx.AsyncClient(
                timeout=5.0,
                follow_redirects=True,
                headers={"User-Agent": "EmailIntel-Ultra/0.1"},
            ) as client:
                response = await client.get(url)
            if response.status_code == 200:
                data = response.json()
                details = {
                    "ldhName": data.get("ldhName"),
                    "status": data.get("status", []),
                    "events": data.get("events", []),
                    "nameservers": [
                        item.get("ldhName")
                        for item in data.get("nameservers", [])
                        if item.get("ldhName")
                    ],
                }
                status = FindingStatus.VERIFIED
                confidence = 0.99
                title = "Public RDAP domain record"
                error = None
            elif response.status_code == 404:
                details = {"http_status": 404}
                status = FindingStatus.NOT_FOUND
                confidence = 0.95
                title = "No public RDAP domain record returned"
                error = None
            else:
                details = {"http_status": response.status_code}
                status = FindingStatus.UNAVAILABLE
                confidence = 0.0
                title = "RDAP source unavailable"
                error = f"HTTP {response.status_code}"
        except (httpx.HTTPError, ValueError) as exc:
            details = {}
            status = FindingStatus.ERROR
            confidence = 0.0
            title = "RDAP lookup failed"
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
