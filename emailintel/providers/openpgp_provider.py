from __future__ import annotations

import time
from urllib.parse import quote

import httpx

from emailintel.core.evidence import evidence_id, finalize_evidence
from emailintel.core.models import Evidence, FindingStatus, TargetProfile
from .base import BaseProvider


class OpenPGPProvider(BaseProvider):
    name = "openpgp-public-key"
    category = "public-key"
    source_name = "keys.openpgp.org"
    source_homepage = "https://keys.openpgp.org/"
    description = "Checks the public OpenPGP key directory for an explicitly published email identity."

    def query_reference(self, target: TargetProfile) -> str:
        return "https://keys.openpgp.org/vks/v1/by-email/" + quote(target.normalized, safe="")

    async def query(self, target: TargetProfile, scan_id: str) -> Evidence:
        started = time.perf_counter()
        url = self.query_reference(target)
        try:
            async with httpx.AsyncClient(
                timeout=5.0,
                follow_redirects=True,
                headers={"User-Agent": "EmailIntel-Ultra/0.1"},
            ) as client:
                response = await client.get(url)
            if response.status_code == 200 and "BEGIN PGP PUBLIC KEY BLOCK" in response.text:
                status = FindingStatus.FOUND
                confidence = 0.9
                title = "Public OpenPGP key published for email"
                details = {"key_block_present": True, "bytes": len(response.content)}
                error = None
            elif response.status_code == 404:
                status = FindingStatus.NOT_FOUND
                confidence = 0.8
                title = "No public OpenPGP key returned"
                details = {"http_status": 404}
                error = None
            else:
                status = FindingStatus.UNAVAILABLE
                confidence = 0.0
                title = "OpenPGP source unavailable"
                details = {"http_status": response.status_code}
                error = f"HTTP {response.status_code}"
        except httpx.HTTPError as exc:
            status = FindingStatus.ERROR
            confidence = 0.0
            title = "OpenPGP lookup failed"
            details = {}
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
