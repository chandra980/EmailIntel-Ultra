from __future__ import annotations

from abc import ABC, abstractmethod

from emailintel.core.models import Evidence, ScanPlan, TargetProfile


class BaseProvider(ABC):
    name = "base"
    category = "unknown"
    version = "1"
    parser_version = "1"
    requires_auth = False

    def eligible(self, target: TargetProfile, plan: ScanPlan) -> bool:
        return self.category in plan.selected_categories

    @abstractmethod
    async def query(self, target: TargetProfile, scan_id: str) -> Evidence:
        raise NotImplementedError
