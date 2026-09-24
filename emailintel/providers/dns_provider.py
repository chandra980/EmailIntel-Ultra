from __future__ import annotations

import time

import dns.asyncresolver
import dns.exception

from emailintel.core.evidence import evidence_id, finalize_evidence
from emailintel.core.models import Evidence, FindingStatus, TargetProfile
from .base import BaseProvider


class DNSProvider(BaseProvider):
    name = "dns-mail-intelligence"
    category = "dns"

    async def query(self, target: TargetProfile, scan_id: str) -> Evidence:
        started = time.perf_counter()
        details: dict[str, object] = {"domain": target.domain}
        try:
            resolver = dns.asyncresolver.Resolver()
            resolver.lifetime = 4.0
            mx = await resolver.resolve(target.domain, "MX")
            details["mx"] = sorted(
                [f"{r.preference} {str(r.exchange).rstrip('.')}" for r in mx]
            )
            for rtype, key in [("TXT", "txt"), ("NS", "ns")]:
                try:
                    answer = await resolver.resolve(target.domain, rtype)
                    details[key] = [str(item).strip('"') for item in answer]
                except Exception:
                    details[key] = []
            try:
                dmarc = await resolver.resolve(f"_dmarc.{target.domain}", "TXT")
                details["dmarc"] = [str(item).strip('"') for item in dmarc]
            except Exception:
                details["dmarc"] = []
            evidence = Evidence(
                id=evidence_id(),
                scan_id=scan_id,
                provider=self.name,
                category=self.category,
                title="Public mail-domain DNS records",
                status=FindingStatus.VERIFIED,
                confidence=0.99,
                evidence=f"MX records resolved for {target.domain}",
                details=details,
                latency_ms=int((time.perf_counter() - started) * 1000),
                provider_version=self.version,
                parser_version=self.parser_version,
            )
        except (dns.exception.DNSException, OSError) as exc:
            evidence = Evidence(
                id=evidence_id(),
                scan_id=scan_id,
                provider=self.name,
                category=self.category,
                title="DNS lookup unavailable",
                status=FindingStatus.ERROR,
                confidence=0.0,
                details=details,
                error=str(exc),
                latency_ms=int((time.perf_counter() - started) * 1000),
                provider_version=self.version,
                parser_version=self.parser_version,
            )
        return finalize_evidence(evidence)
