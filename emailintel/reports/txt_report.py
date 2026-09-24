from __future__ import annotations

from pathlib import Path

from emailintel.core.models import ScanResult


def write_text(result: ScanResult, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "EMAILINTEL ULTRA",
        "================",
        f"Scan ID: {result.scan_id}",
        f"Target: {result.target.normalized}",
        f"Mode: {result.mode}",
        f"Duration: {result.duration_seconds}s",
        "",
        "FINDINGS",
        "--------",
    ]
    for item in result.evidence:
        lines += [
            f"[{item.status.value}] {item.title}",
            f"  Provider: {item.provider}",
            f"  Confidence: {item.confidence:.2f}",
            f"  Freshness: {item.freshness.value}",
            f"  Evidence ID: {item.id}",
            f"  URL: {item.url or '-'}",
            f"  Error: {item.error or '-'}",
            "",
        ]
    path.write_text("\n".join(lines), encoding="utf-8")
    return path
