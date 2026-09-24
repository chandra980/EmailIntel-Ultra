from __future__ import annotations

import html
import json
from pathlib import Path

from emailintel.core.models import FindingStatus, ScanResult


def esc(value) -> str:
    return html.escape(str(value), quote=True)


def write_html(result: ScanResult, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    positives = [
        item for item in result.evidence
        if item.status not in {
            FindingStatus.NOT_FOUND,
            FindingStatus.SKIPPED,
            FindingStatus.ERROR,
            FindingStatus.UNAVAILABLE,
        }
    ]
    families = len({
        item.family_id for item in positives if item.family_id
    })

    rows = []
    for item in result.evidence:
        link = (
            f"<a href='{esc(item.url)}' target='_blank' rel='noopener'>source</a>"
            if item.url else "—"
        )
        rows.append(
            "<tr>"
            f"<td><code>{esc(item.id)}</code></td>"
            f"<td>{esc(item.provider)}</td>"
            f"<td>{esc(item.status.value)}</td>"
            f"<td>{item.confidence:.2f}</td>"
            f"<td>{esc(item.freshness.value)}</td>"
            f"<td>{esc(item.title)}</td>"
            f"<td>{link}</td>"
            f"<td><code>{esc(item.family_id or '')}</code></td>"
            "</tr>"
        )

    plan_json = esc(json.dumps(result.plan.reasons, indent=2))
    page = f"""<!doctype html>
<html>
<head>
<meta charset='utf-8'>
<meta name='viewport' content='width=device-width,initial-scale=1'>
<title>EmailIntel Ultra — {esc(result.scan_id)}</title>
<style>
:root{{--bg:#0b1220;--panel:#111b2e;--text:#e8eefb;--muted:#9fb0cc;--line:#253553;--accent:#75a7ff}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--text);font-family:Inter,Segoe UI,Arial,sans-serif}}
main{{max-width:1280px;margin:auto;padding:32px}}
h1{{margin:0;font-size:34px}}
.sub{{color:var(--muted);margin:8px 0 24px}}
.cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;margin:24px 0}}
.card{{background:var(--panel);border:1px solid var(--line);padding:18px;border-radius:14px}}
.card b{{font-size:28px;display:block}}
.card span{{color:var(--muted)}}
.panel{{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:18px;margin-top:16px;overflow:auto}}
table{{width:100%;border-collapse:collapse;min-width:900px}}
th,td{{padding:12px;border-bottom:1px solid var(--line);text-align:left}}
th{{color:var(--muted)}}
a{{color:var(--accent)}}
code{{color:#b8d1ff}}
pre{{white-space:pre-wrap;color:#c9d6ec}}
.badge{{display:inline-block;padding:5px 9px;border:1px solid var(--line);border-radius:999px;color:var(--muted);margin-right:6px}}
</style>
</head>
<body>
<main>
<h1>EMAILINTEL ULTRA</h1>
<div class='sub'>Public Identity Intelligence Framework · Chandra Kumar Yadav</div>
<div>
  <span class='badge'>{esc(result.mode.upper())}</span>
  <span class='badge'>{esc(result.scan_id)}</span>
</div>
<div class='cards'>
  <div class='card'><b>{len(result.evidence)}</b><span>Providers completed</span></div>
  <div class='card'><b>{len(positives)}</b><span>Positive findings</span></div>
  <div class='card'><b>{families}</b><span>Evidence families</span></div>
  <div class='card'><b>{len(result.errors)}</b><span>Errors</span></div>
</div>
<div class='panel'>
  <h2>Investigation</h2>
  <p><b>Target:</b> {esc(result.target.normalized)}</p>
  <p><b>Target type:</b> {esc(result.plan.target_type)}</p>
  <p><b>Duration:</b> {result.duration_seconds}s</p>
</div>
<div class='panel'>
  <h2>Findings</h2>
  <table>
    <thead><tr>
      <th>Evidence</th><th>Provider</th><th>Status</th>
      <th>Confidence</th><th>Freshness</th><th>Finding</th>
      <th>Source</th><th>Family</th>
    </tr></thead>
    <tbody>{''.join(rows)}</tbody>
  </table>
</div>
<div class='panel'>
  <h2>Scan-plan rationale</h2>
  <pre>{plan_json}</pre>
</div>
<div class='panel'>
  <h2>Limitations</h2>
  <p>This report contains only public, anonymously accessible evidence returned by implemented providers. Absence of evidence is not proof of absence. Historical evidence does not prove current identity or affiliation.</p>
</div>
</main>
</body>
</html>"""
    path.write_text(page, encoding="utf-8")
    return path
