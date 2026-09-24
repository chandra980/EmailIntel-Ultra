from __future__ import annotations

import csv
from pathlib import Path

from emailintel.core.models import ScanResult


def write_csv(result: ScanResult, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "evidence_id", "provider", "category", "status",
            "confidence", "freshness", "title", "url",
            "family_id", "hash", "error",
        ])
        for item in result.evidence:
            writer.writerow([
                item.id,
                item.provider,
                item.category,
                item.status.value,
                item.confidence,
                item.freshness.value,
                item.title,
                item.url or "",
                item.family_id or "",
                item.normalized_hash,
                item.error or "",
            ])
    return path
