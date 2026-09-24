from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from .models import ScanResult


SCHEMA = """
CREATE TABLE IF NOT EXISTS scans (
  scan_id TEXT PRIMARY KEY,
  target TEXT NOT NULL,
  started_at TEXT NOT NULL,
  finished_at TEXT NOT NULL,
  payload TEXT NOT NULL
);
"""


def init_db(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(path) as conn:
        conn.execute(SCHEMA)
        conn.commit()


def save_scan(path: Path, result: ScanResult) -> None:
    init_db(path)
    payload = json.dumps(result.to_dict(), ensure_ascii=False)
    with sqlite3.connect(path) as conn:
        conn.execute(
            "INSERT OR REPLACE INTO scans(scan_id,target,started_at,finished_at,payload) VALUES(?,?,?,?,?)",
            (
                result.scan_id,
                result.target.normalized,
                result.started_at,
                result.finished_at,
                payload,
            ),
        )
        conn.commit()


def load_scan(path: Path, scan_id: str) -> dict | None:
    if not path.exists():
        return None
    with sqlite3.connect(path) as conn:
        row = conn.execute(
            "SELECT payload FROM scans WHERE scan_id=?",
            (scan_id,),
        ).fetchone()
    return json.loads(row[0]) if row else None
