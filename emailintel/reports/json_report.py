from __future__ import annotations

import json
from pathlib import Path

from emailintel.core.models import ScanResult


def write_json(result: ScanResult, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(result.to_dict(), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return path
