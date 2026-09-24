from __future__ import annotations

from abc import ABC, abstractmethod

from emailintel.core.models import Evidence, ScanPlan, TargetProfile


class BaseProvider(ABC):
    name = "base"
    category = "unknown"
    version = "1"
    parser_version = "1"
    requires_auth = False

    source_name = "Unknown public source"
    source_homepage = ""
    access_method = "anonymous-public"
    description = ""
    expected_seconds = 4.0

    def eligible(self, target: TargetProfile, plan: ScanPlan) -> bool:
        return self.category in plan.selected_categories

    def query_reference(self, target: TargetProfile) -> str:
        return self.source_homepage

    def source_metadata(self, target: TargetProfile) -> dict[str, object]:
        return {
            "provider": self.name,
            "category": self.category,
            "source_name": self.source_name,
            "source_homepage": self.source_homepage,
            "access_method": self.access_method,
            "description": self.description,
            "query_reference": self.query_reference(target),
            "expected_seconds": self.expected_seconds,
        }

    @abstractmethod
    async def query(self, target: TargetProfile, scan_id: str) -> Evidence:
        raise NotImplementedError
