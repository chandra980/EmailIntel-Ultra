from __future__ import annotations

import time
from urllib.parse import quote_plus

import httpx

from emailintel.core.evidence import evidence_id, finalize_evidence
from emailintel.core.models import Evidence, FindingStatus, TargetProfile
from .base import BaseProvider


class DNSProvider(BaseProvider):
    name = "dns-mail-intelligence"
    category = "dns"
    source_name = "Google Public DNS-over-HTTPS"
    source_homepage = "https://developers.google.com/speed/public-dns/docs/doh/json"
    description = (
        "Queries public DNS-over-HTTPS JSON records for MX, TXT, NS and DMARC. "
        "No mailbox probing is performed."
    )

    def query_reference(self, target: TargetProfile) -> str:
        return f"https://dns.google/resolve?name={quote_plus(target.domain)}&type=MX"

    async def _resolve(
        self,
        client: httpx.AsyncClient,
        name: str,
        record_type: str,
    ) -> dict:
        response = await client.get(
            "https://dns.google/resolve",
            params={"name": name, "type": record_type},
        )
        response.raise_for_status()
        payload = response.json()
        answers = payload.get("Answer") or []
        return {
            "status": payload.get("Status"),
            "answers": [
                {
                    "name": item.get("name"),
                    "type": item.get("type"),
                    "ttl": item.get("TTL"),
                    "data": item.get("data"),
                }
                for item in answers
            ],
        }

    async def query(self, target: TargetProfile, scan_id: str) -> Evidence:
        started = time.perf_counter()
        url = self.query_reference(target)
        details: dict[str, object] = {
            "domain": target.domain,
            "source": self.source_name,
            "queried_record_types": ["MX", "TXT", "NS", "_dmarc TXT"],
        }
        try:
            async with httpx.AsyncClient(
                timeout=6.0,
                follow_redirects=True,
                headers={"User-Agent": "EmailIntel-Ultra/0.1"},
            ) as client:
                details["mx"] = await self._resolve(client, target.domain, "MX")
                details["txt"] = await self._resolve(client, target.domain, "TXT")
                details["ns"] = await self._resolve(client, target.domain, "NS")
                details["dmarc"] = await self._resolve(
                    client,
                    f"_dmarc.{target.domain}",
                    "TXT",
                )

            mx_answers = details["mx"].get("answers", [])
            if mx_answers:
                status = FindingStatus.VERIFIED
                confidence = 0.99
                title = "Public mail-domain DNS records"
                error = None
                evidence_text = f"MX records resolved for {target.domain}"
            else:
                status = FindingStatus.NOT_FOUND
                confidence = 0.85
                title = "No MX records returned by public DNS source"
                error = None
                evidence_text = None
        except (httpx.HTTPError, ValueError) as exc:
            status = FindingStatus.ERROR
            confidence = 0.0
            title = "DNS-over-HTTPS lookup failed"
            error = str(exc)
            evidence_text = None

        evidence = Evidence(
            id=evidence_id(),
            scan_id=scan_id,
            provider=self.name,
            category=self.category,
            title=title,
            status=status,
            confidence=confidence,
            url=url,
            evidence=evidence_text,
            details=details,
            error=error,
            latency_ms=int((time.perf_counter() - started) * 1000),
            provider_version=self.version,
            parser_version=self.parser_version,
        )
        return finalize_evidence(evidence)
