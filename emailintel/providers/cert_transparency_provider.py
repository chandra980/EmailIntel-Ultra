from __future__ import annotations

import time
from urllib.parse import quote_plus

import httpx

from emailintel.core.evidence import evidence_id, finalize_evidence
from emailintel.core.models import Evidence, FindingStatus, TargetProfile
from .base import BaseProvider


class CertificateTransparencyProvider(BaseProvider):
    name = "crtsh-certificate-transparency"
    category = "certificate-transparency"
    source_name = "crt.sh Certificate Transparency"
    source_homepage = "https://crt.sh/"
    description = "Queries public certificate-transparency records for custom email domains."

    def query_reference(self, target: TargetProfile) -> str:
        return f"https://crt.sh/?q={quote_plus('%.' + target.domain)}&output=json"

    async def query(self, target: TargetProfile, scan_id: str) -> Evidence:
        started = time.perf_counter()
        url = self.query_reference(target)
        try:
            async with httpx.AsyncClient(
                timeout=8.0,
                follow_redirects=True,
                headers={"User-Agent": "EmailIntel-Ultra/0.1"},
            ) as client:
                response = await client.get(url)

            if response.status_code == 200:
                data = response.json()
                names: set[str] = set()
                for row in data[:1000]:
                    value = row.get("name_value") or ""
                    for name in str(value).splitlines():
                        clean = name.strip().lower()
                        if clean.endswith(target.domain.lower()):
                            names.add(clean)
                details = {
                    "certificate_rows": len(data),
                    "unique_related_names": sorted(names)[:100],
                    "result_truncated": len(names) > 100,
                }
                status = FindingStatus.FOUND if names else FindingStatus.NOT_FOUND
                confidence = 0.95 if names else 0.8
                title = (
                    f"Public certificate-transparency names found: {len(names)}"
                    if names
                    else "No related certificate-transparency names returned"
                )
                error = None
            elif response.status_code == 429:
                status = FindingStatus.RATE_LIMITED
                confidence = 0.0
                title = "Certificate-transparency source rate limited"
                details = {"http_status": 429}
                error = "HTTP 429"
            else:
                status = FindingStatus.UNAVAILABLE
                confidence = 0.0
                title = "Certificate-transparency source unavailable"
                details = {"http_status": response.status_code}
                error = f"HTTP {response.status_code}"
        except (httpx.HTTPError, ValueError) as exc:
            status = FindingStatus.ERROR
            confidence = 0.0
            title = "Certificate-transparency lookup failed"
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
            evidence=(
                f"Public certificate records were returned for {target.domain}"
                if status == FindingStatus.FOUND
                else None
            ),
            details=details,
            error=error,
            latency_ms=int((time.perf_counter() - started) * 1000),
            provider_version=self.version,
            parser_version=self.parser_version,
        )
        return finalize_evidence(evidence)
