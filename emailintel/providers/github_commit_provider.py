from __future__ import annotations

import time
from urllib.parse import quote_plus

import httpx

from emailintel.core.evidence import evidence_id, finalize_evidence
from emailintel.core.models import Evidence, FindingStatus, TargetProfile
from .base import BaseProvider


class GitHubCommitProvider(BaseProvider):
    name = "github-public-commit-search"
    category = "developer"
    source_name = "GitHub Public Commit Search"
    source_homepage = "https://github.com/search"
    description = (
        "Searches GitHub's public commit index for exact author-email references. "
        "No private repositories or authenticated endpoints are used."
    )

    def query_reference(self, target: TargetProfile) -> str:
        query = quote_plus(f"author-email:{target.normalized}")
        return f"https://api.github.com/search/commits?q={query}&per_page=10"

    async def query(self, target: TargetProfile, scan_id: str) -> Evidence:
        started = time.perf_counter()
        url = self.query_reference(target)
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "EmailIntel-Ultra/0.1",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        try:
            async with httpx.AsyncClient(
                timeout=6.0,
                follow_redirects=True,
                headers=headers,
            ) as client:
                response = await client.get(url)

            if response.status_code == 200:
                data = response.json()
                items = data.get("items", [])
                matches = []
                for item in items[:10]:
                    commit = item.get("commit") or {}
                    author = commit.get("author") or {}
                    if str(author.get("email", "")).lower() != target.normalized.lower():
                        continue
                    repo = item.get("repository") or {}
                    matches.append({
                        "repository": repo.get("full_name"),
                        "commit_sha": item.get("sha"),
                        "commit_url": item.get("html_url"),
                        "author_name": author.get("name"),
                        "author_date": author.get("date"),
                    })

                if matches:
                    status = FindingStatus.FOUND
                    confidence = 0.95
                    title = f"Exact public GitHub commit email reference(s): {len(matches)}"
                    error = None
                else:
                    status = FindingStatus.NOT_FOUND
                    confidence = 0.8
                    title = "No exact public GitHub commit email reference returned"
                    error = None
                details = {
                    "reported_total_count": data.get("total_count", 0),
                    "validated_exact_matches": matches,
                }
            elif response.status_code in {403, 429}:
                status = FindingStatus.RATE_LIMITED
                confidence = 0.0
                title = "GitHub public commit search rate limited"
                details = {"http_status": response.status_code}
                error = response.headers.get("x-ratelimit-remaining", "rate limited")
            else:
                status = FindingStatus.UNAVAILABLE
                confidence = 0.0
                title = "GitHub public commit search unavailable"
                details = {"http_status": response.status_code}
                error = f"HTTP {response.status_code}"
        except (httpx.HTTPError, ValueError) as exc:
            status = FindingStatus.ERROR
            confidence = 0.0
            title = "GitHub public commit search failed"
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
                f"Exact public commit metadata matched {target.normalized}"
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
