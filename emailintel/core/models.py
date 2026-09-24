from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any


class FindingStatus(str, Enum):
    VERIFIED = "VERIFIED"
    FOUND = "FOUND"
    HIGH_CONFIDENCE = "HIGH_CONFIDENCE"
    POSSIBLE = "POSSIBLE"
    UNVERIFIED = "UNVERIFIED"
    NOT_FOUND = "NOT_FOUND"
    UNKNOWN = "UNKNOWN"
    SKIPPED = "SKIPPED"
    RATE_LIMITED = "RATE_LIMITED"
    BLOCKED = "BLOCKED"
    UNAVAILABLE = "UNAVAILABLE"
    ERROR = "ERROR"


class Freshness(str, Enum):
    CURRENT = "CURRENT"
    RECENT = "RECENT"
    AGING = "AGING"
    HISTORICAL = "HISTORICAL"
    UNKNOWN = "UNKNOWN"


@dataclass(slots=True)
class Evidence:
    id: str
    scan_id: str
    provider: str
    category: str
    title: str
    status: FindingStatus
    confidence: float
    url: str | None = None
    evidence: str | None = None
    observed_at: str | None = None
    retrieved_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    freshness: Freshness = Freshness.UNKNOWN
    provider_version: str = "1"
    parser_version: str = "1"
    normalized_hash: str = ""
    family_id: str | None = None
    details: dict[str, Any] = field(default_factory=dict)
    error: str | None = None
    latency_ms: int | None = None

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["status"] = self.status.value
        data["freshness"] = self.freshness.value
        return data


@dataclass(slots=True)
class TargetProfile:
    original: str
    normalized: str
    local_part: str
    domain: str
    provider_type: str
    is_free_mail: bool
    is_role_based: bool
    is_disposable: bool


@dataclass(slots=True)
class ScanPlan:
    target_type: str
    selected_categories: list[str]
    excluded_categories: list[str]
    reasons: dict[str, str]
    mode: str


@dataclass(slots=True)
class ScanResult:
    scan_id: str
    target: TargetProfile
    mode: str
    started_at: str
    finished_at: str
    duration_seconds: float
    evidence: list[Evidence]
    errors: list[str]
    plan: ScanPlan

    def to_dict(self) -> dict[str, Any]:
        return {
            "scan": {
                "id": self.scan_id,
                "mode": self.mode,
                "started_at": self.started_at,
                "finished_at": self.finished_at,
                "duration_seconds": self.duration_seconds,
            },
            "target": asdict(self.target),
            "plan": asdict(self.plan),
            "summary": {
                "findings": len([
                    e for e in self.evidence
                    if e.status not in {
                        FindingStatus.NOT_FOUND,
                        FindingStatus.SKIPPED,
                        FindingStatus.ERROR,
                    }
                ]),
                "errors": len(self.errors),
                "providers_completed": len(self.evidence),
            },
            "evidence": [e.to_dict() for e in self.evidence],
            "errors": self.errors,
        }
