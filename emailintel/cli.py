from __future__ import annotations

import asyncio
import json
import os
import platform
import socket
from pathlib import Path

import typer
from rich import box
from rich.console import Console
from rich.markup import escape
from rich.panel import Panel
from rich.table import Table

from emailintel import __version__
from emailintel.core.confidence import explain_confidence
from emailintel.core.database import init_db, load_scan, save_scan
from emailintel.core.models import FindingStatus
from emailintel.core.planner import build_plan
from emailintel.core.scanner import scan as run_scan
from emailintel.core.validator import validate_email
from emailintel.providers import providers as provider_registry
from emailintel.reports import write_csv, write_html, write_json, write_text

app = typer.Typer(
    no_args_is_help=True,
    add_completion=False,
    help="EmailIntel Ultra — passive public email OSINT",
)
console = Console(highlight=False)
DATA_DIR = Path(os.getenv("EMAILINTEL_HOME", Path.home() / ".emailintel-ultra"))
DB_PATH = DATA_DIR / "emailintel.db"
REPORT_ROOT = Path("reports")


def banner() -> None:
    console.print(Panel.fit(
        "[bold]EMAILINTEL ULTRA[/bold]\n"
        "[dim]Public Identity Intelligence Framework[/dim]\n"
        "Chandra Kumar Yadav",
        border_style="blue",
    ))


def mask_email(email: str) -> str:
    local, domain = email.split("@", 1)
    shown = local[:2] if len(local) > 2 else local[:1]
    return f"{shown}{'*' * max(3, len(local) - len(shown))}@{domain}"


def get_stored(scan_id: str) -> dict:
    data = load_scan(DB_PATH, scan_id)
    if not data:
        raise typer.BadParameter(
            f"Scan {scan_id} was not found in the local database"
        )
    return data


def _status_style(status: str) -> str:
    if status in {"VERIFIED", "FOUND", "HIGH_CONFIDENCE"}:
        return "bold green"
    if status in {"NOT_FOUND", "SKIPPED", "UNKNOWN"}:
        return "yellow"
    if status in {"RATE_LIMITED", "BLOCKED", "UNAVAILABLE"}:
        return "bold yellow"
    if status == "ERROR":
        return "bold red"
    return "white"


class TerminalProgress:
    def __init__(self) -> None:
        self.started = 0
        self.finished = 0
        self.total = 0

    def __call__(self, event: dict) -> None:
        kind = event.get("event")
        if kind == "plan":
            console.print()
            console.print(
                f"[bold cyan]SCAN PLAN[/bold cyan]  "
                f"{escape(str(event.get('target_type', 'unknown')))}  "
                f"mode={escape(str(event.get('mode', 'balanced')).upper())}"
            )
            console.print(
                "[dim]Selected categories:[/dim] "
                + ", ".join(event.get("selected_categories", []))
            )
        elif kind == "provider_set":
            providers = event.get("providers", [])
            self.total = len(providers)
            table = Table(
                title=f"Public Sources Selected ({self.total})",
                box=box.ROUNDED,
                show_lines=False,
            )
            table.add_column("#", justify="right", style="dim")
            table.add_column("Provider", style="bold")
            table.add_column("Source")
            table.add_column("Category")
            table.add_column("Query / Reference", overflow="fold")
            for index, item in enumerate(providers, start=1):
                ref = str(item.get("query_reference") or item.get("source_homepage") or "-")
                table.add_row(
                    str(index),
                    str(item.get("provider", "")),
                    str(item.get("source_name", "")),
                    str(item.get("category", "")),
                    ref,
                )
            console.print(table)
            console.print(
                "[dim]The scanner queries only these currently implemented "
                "public/anonymous sources for this target.[/dim]\n"
            )
        elif kind == "start":
            self.started += 1
            ref = str(event.get("query_reference") or event.get("source_homepage") or "-")
            console.print(
                f"[cyan]QUERYING[/cyan] [{self.started}/{self.total or '?'}] "
                f"[bold]{escape(str(event.get('source_name', event.get('provider', 'source'))))}[/bold]\n"
                f"          provider: {escape(str(event.get('provider', '')))}\n"
                f"          source:   {escape(ref)}"
            )
        elif kind == "result":
            self.finished += 1
            status = str(event.get("status", "UNKNOWN"))
            style = _status_style(status)
            latency = int(event.get("latency_ms") or 0)
            url = str(event.get("url") or event.get("query_reference") or "")
            console.print(
                f"[{style}]RESULT {status}[/{style}] "
                f"[{self.finished}/{self.total + 1 if self.total else '?'}] "
                f"{escape(str(event.get('provider', '')))} — "
                f"{escape(str(event.get('title', '')))} "
                f"[dim]({latency} ms)[/dim]"
            )
            if url:
                console.print(f"          [link={url}]{escape(url)}[/link]")
        elif kind == "complete":
            console.print(
                f"\n[bold green]NETWORK CHECKS FINISHED[/bold green]  "
                f"{event.get('duration_seconds', 0)}s · "
                f"{event.get('providers_completed', 0)} evidence records · "
                f"{event.get('errors', 0)} errors"
            )


def _print_final_result(result) -> None:
    positive_states = {
        FindingStatus.VERIFIED,
        FindingStatus.FOUND,
        FindingStatus.HIGH_CONFIDENCE,
        FindingStatus.POSSIBLE,
    }
    positives = [item for item in result.evidence if item.status in positive_states]
    source_urls = [item for item in result.evidence if item.url]

    console.print()
    console.print(Panel(
        f"[bold]Target:[/bold] {escape(result.target.normalized)}\n"
        f"[bold]Scan ID:[/bold] {result.scan_id}\n"
        f"[bold]Mode:[/bold] {result.mode.upper()}\n"
        f"[bold]Elapsed:[/bold] {result.duration_seconds}s\n"
        f"[bold]Evidence records:[/bold] {len(result.evidence)}\n"
        f"[bold]Positive findings:[/bold] {len(positives)}\n"
        f"[bold]Source URLs:[/bold] {len(source_urls)}",
        title="FINAL INVESTIGATION SUMMARY",
        border_style="green",
    ))

    table = Table(
        title="Complete Terminal Results",
        box=box.ROUNDED,
        show_lines=True,
    )
    table.add_column("#", justify="right", style="dim")
    table.add_column("Status")
    table.add_column("Source / Provider", style="bold")
    table.add_column("Finding", overflow="fold")
    table.add_column("Confidence", justify="right")
    table.add_column("Time", justify="right")
    table.add_column("Evidence ID")
    for index, item in enumerate(result.evidence, start=1):
        status = item.status.value
        table.add_row(
            str(index),
            f"[{_status_style(status)}]{status}[/{_status_style(status)}]",
            item.provider,
            item.title,
            f"{item.confidence:.2f}",
            f"{item.latency_ms or 0} ms",
            item.id,
        )
    console.print(table)

    console.print("\n[bold cyan]SOURCE LINKS / WHERE THE DATA CAME FROM[/bold cyan]")
    link_table = Table(box=box.SIMPLE, show_header=True)
    link_table.add_column("#", justify="right")
    link_table.add_column("Provider")
    link_table.add_column("Status")
    link_table.add_column("Direct Source / Query URL", overflow="fold")
    row = 0
    for item in result.evidence:
        if not item.url:
            continue
        row += 1
        link_table.add_row(
            str(row),
            item.provider,
            item.status.value,
            f"[link={item.url}]{item.url}[/link]",
        )
    if row:
        console.print(link_table)
    else:
        console.print("[dim]No HTTP source URLs were produced in this scan.[/dim]")

    console.print("\n[bold]Evidence details[/bold]")
    for item in result.evidence:
        console.print(
            Panel(
                f"[bold]Finding:[/bold] {escape(item.title)}\n"
                f"[bold]Status:[/bold] {item.status.value}\n"
                f"[bold]Provider:[/bold] {escape(item.provider)}\n"
                f"[bold]Category:[/bold] {escape(item.category)}\n"
                f"[bold]Confidence:[/bold] {item.confidence:.2f}\n"
                f"[bold]Freshness:[/bold] {item.freshness.value}\n"
                f"[bold]Evidence ID:[/bold] {item.id}\n"
                f"[bold]Evidence Family:[/bold] {item.family_id or '-'}\n"
                f"[bold]Source URL:[/bold] {escape(item.url or '-')}\n"
                f"[bold]Observed Evidence:[/bold] {escape(item.evidence or '-')}\n"
                f"[bold]Details:[/bold]\n{escape(json.dumps(item.details, indent=2, ensure_ascii=False, default=str))}\n"
                f"[bold]Error:[/bold] {escape(item.error or '-')}",
                border_style="blue" if item.status in positive_states else "dim",
            )
        )


@app.command()
def version() -> None:
    """Show version and platform information."""
    console.print(f"EmailIntel Ultra {__version__}")
    console.print(f"Python: {platform.python_version()}")
    console.print(f"Platform: {platform.system()} {platform.release()}")
    console.print("Owner: Chandra Kumar Yadav")


@app.command()
def plan(
    email: str,
    mode: str = typer.Option("balanced", help="fast, balanced, or deep"),
) -> None:
    """Explain which provider categories would be selected and why."""
    checked = validate_email(email)
    if not checked.valid or not checked.profile:
        console.print(f"[red]{checked.reason}[/red]")
        raise typer.Exit(1)
    scan_plan = build_plan(checked.profile, mode)
    banner()
    console.print(f"[bold]Target type:[/bold] {scan_plan.target_type}")
    table = Table(box=box.SIMPLE_HEAVY)
    table.add_column("Category")
    table.add_column("Selected")
    table.add_column("Reason")
    for category in sorted(
        set(scan_plan.selected_categories + scan_plan.excluded_categories)
    ):
        table.add_row(
            category,
            "YES" if category in scan_plan.selected_categories else "NO",
            scan_plan.reasons.get(category, ""),
        )
    console.print(table)


@app.command("providers")
def providers_cmd() -> None:
    """List implemented providers, public sources and access methods."""
    table = Table(title="Implemented Public Sources", box=box.ROUNDED)
    table.add_column("Provider")
    table.add_column("Source")
    table.add_column("Category")
    table.add_column("Access")
    table.add_column("Homepage", overflow="fold")
    table.add_row(
        "email-validator",
        "Local deterministic validation",
        "validation",
        "local",
        "-",
    )
    for provider in provider_registry():
        table.add_row(
            provider.name,
            provider.source_name,
            provider.category,
            provider.access_method,
            provider.source_homepage,
        )
    console.print(table)
    console.print(
        "[dim]Runtime availability can vary. Providers are shown here only when "
        "code is actually implemented in the repository.[/dim]"
    )


@app.command()
def coverage() -> None:
    """Show current implemented category coverage without inflated source counts."""
    counts: dict[str, int] = {"validation": 1}
    for provider in provider_registry():
        counts[provider.category] = counts.get(provider.category, 0) + 1
    table = Table(title="Source Coverage Matrix", box=box.SIMPLE_HEAVY)
    table.add_column("Category")
    table.add_column("Implemented", justify="right")
    table.add_column("Status")
    for category, count in sorted(counts.items()):
        table.add_row(category, str(count), "AVAILABLE")
    console.print(table)
    console.print(f"Total implemented checks: {sum(counts.values())}")


@app.command()
def doctor() -> None:
    """Run local installation and connectivity diagnostics."""
    checks: list[tuple[str, bool, str]] = []
    checks.append((
        "Python >= 3.11",
        tuple(map(int, platform.python_version_tuple()[:2])) >= (3, 11),
        platform.python_version(),
    ))
    try:
        init_db(DB_PATH)
        checks.append(("SQLite", True, str(DB_PATH)))
    except Exception as exc:
        checks.append(("SQLite", False, str(exc)))
    try:
        socket.getaddrinfo("rdap.org", 443)
        checks.append(("DNS resolver", True, "rdap.org resolved"))
    except OSError as exc:
        checks.append(("DNS resolver", False, str(exc)))
    checks.append((
        "Provider registry",
        len(provider_registry()) >= 1,
        f"{len(provider_registry())} network providers",
    ))

    table = Table(title="EmailIntel Doctor", box=box.SIMPLE_HEAVY)
    table.add_column("Check")
    table.add_column("Result")
    table.add_column("Detail")
    failed = False
    for name, ok, detail in checks:
        failed |= not ok
        table.add_row(
            name,
            "[green]OK[/green]" if ok else "[red]FAIL[/red]",
            detail,
        )
    console.print(table)
    raise typer.Exit(1 if failed else 0)


@app.command("scan")
def scan_cmd(
    email: str,
    mode: str = typer.Option(
        "balanced",
        "--mode",
        help="fast, balanced, or deep",
    ),
    fast: bool = typer.Option(False, "--fast", help="Shortcut for --mode fast"),
    deep: bool = typer.Option(False, "--deep", help="Shortcut for --mode deep"),
    max_concurrency: int = typer.Option(8, min=1, max=32),
    report_format: str = typer.Option(
        "all",
        "--format",
        help="all, html, json, csv, or txt",
    ),
    no_history: bool = typer.Option(
        False,
        help="Do not save scan to local SQLite history",
    ),
    redact: bool = typer.Option(
        False,
        help="Redact email in terminal summary",
    ),
    quiet: bool = typer.Option(
        False,
        "--quiet",
        help="Suppress live provider trace; final formatted results still print",
    ),
) -> None:
    """Scan one email and show full live source trace + formatted terminal results."""
    if fast:
        mode = "fast"
    if deep:
        mode = "deep"
    if mode not in {"fast", "balanced", "deep"}:
        raise typer.BadParameter("mode must be fast, balanced, or deep")

    checked = validate_email(email)
    if not checked.valid or not checked.profile:
        console.print(f"[red]{checked.reason}[/red]")
        raise typer.Exit(1)

    banner()
    shown = mask_email(checked.profile.normalized) if redact else checked.profile.normalized
    console.print(f"[bold]Target:[/bold] {shown}")
    console.print(f"[bold]Mode:[/bold] {mode.upper()}")
    console.print(
        "[dim]Live trace is enabled. Every implemented public source selected "
        "for this scan will be shown below before and after its query.[/dim]"
    )

    progress = None if quiet else TerminalProgress()
    result = asyncio.run(
        run_scan(
            checked.profile,
            mode,
            max_concurrency=max_concurrency,
            progress=progress,
        )
    )

    _print_final_result(result)

    output_dir = REPORT_ROOT / result.scan_id
    formats = (
        {"html", "json", "csv", "txt"}
        if report_format == "all"
        else {report_format}
    )
    generated: list[Path] = []
    if "html" in formats:
        generated.append(write_html(result, output_dir / "report.html"))
    if "json" in formats:
        generated.append(write_json(result, output_dir / "report.json"))
    if "csv" in formats:
        generated.append(write_csv(result, output_dir / "findings.csv"))
    if "txt" in formats:
        generated.append(write_text(result, output_dir / "summary.txt"))

    unknown = formats - {"html", "json", "csv", "txt"}
    if unknown:
        console.print(
            f"[yellow]Unknown report format(s): "
            f"{', '.join(sorted(unknown))}[/yellow]"
        )

    if not no_history:
        save_scan(DB_PATH, result)

    console.print("\n[bold cyan]SAVED REPORTS[/bold cyan]")
    for path in generated:
        console.print(f"  {path.resolve()}")

    if result.errors:
        console.print(
            f"\n[yellow]Scan completed with {len(result.errors)} provider error(s). "
            "Other provider results and reports were preserved.[/yellow]"
        )
        raise typer.Exit(2)


@app.command()
def explain(scan_id: str, evidence_id: str) -> None:
    """Explain why a stored finding received its confidence value."""
    data = get_stored(scan_id)
    match = next(
        (
            item for item in data.get("evidence", [])
            if item.get("id") == evidence_id
        ),
        None,
    )
    if not match:
        raise typer.BadParameter(
            f"Evidence {evidence_id} not found in {scan_id}"
        )

    score = float(match.get("confidence", 0))
    details = explain_confidence(
        score,
        direct_match=score >= 0.8,
        direct_source=bool(
            match.get("url")
            or match.get("provider") == "email-validator"
        ),
        independently_confirmed=False,
        stale=match.get("freshness") in {"AGING", "HISTORICAL"},
    )
    console.print(Panel.fit(
        json.dumps(details, indent=2),
        title=f"Confidence explanation — {evidence_id}",
    ))


@app.command()
def timeline(scan_id: str) -> None:
    """Show a chronological evidence view for a stored scan."""
    data = get_stored(scan_id)
    items = sorted(
        data.get("evidence", []),
        key=lambda item: (
            item.get("observed_at")
            or item.get("retrieved_at")
            or ""
        ),
    )
    table = Table(title=f"Timeline — {scan_id}", box=box.SIMPLE_HEAVY)
    table.add_column("Observed/Retrieved")
    table.add_column("Evidence")
    table.add_column("Finding")
    table.add_column("Freshness")
    for item in items:
        table.add_row(
            item.get("observed_at")
            or item.get("retrieved_at", ""),
            item.get("id", ""),
            item.get("title", ""),
            item.get("freshness", "UNKNOWN"),
        )
    console.print(table)


@app.command()
def diff(scan_a: str, scan_b: str) -> None:
    """Compare two stored scans by normalized evidence hashes."""
    first = get_stored(scan_a)
    second = get_stored(scan_b)
    first_map = {
        item.get("normalized_hash"): item
        for item in first.get("evidence", [])
        if item.get("normalized_hash")
    }
    second_map = {
        item.get("normalized_hash"): item
        for item in second.get("evidence", [])
        if item.get("normalized_hash")
    }

    new = [
        second_map[key]
        for key in second_map.keys() - first_map.keys()
    ]
    missing = [
        first_map[key]
        for key in first_map.keys() - second_map.keys()
    ]

    console.print(f"[green]NEW FINDINGS:[/green] {len(new)}")
    for item in new:
        console.print(
            f" + {item.get('title')} [{item.get('provider')}]"
        )
    console.print(
        f"[yellow]MISSING/CHANGED REFERENCES:[/yellow] {len(missing)}"
    )
    for item in missing:
        console.print(
            f" - {item.get('title')} [{item.get('provider')}]"
        )


@app.command()
def feature(name: str) -> None:
    """Explain a major feature in plain language."""
    docs = {
        "confidence": (
            "Confidence",
            "Evidence-strength indicator. It is not proof of real-world identity.",
            "emailintel explain SCAN_ID EVD_ID",
        ),
        "timeline": (
            "Timeline",
            "Orders evidence by observation/retrieval time so historical data "
            "is not confused with current data.",
            "emailintel timeline SCAN_ID",
        ),
        "coverage": (
            "Coverage",
            "Shows only implemented provider checks; it does not claim "
            "complete Internet coverage.",
            "emailintel coverage",
        ),
        "plan": (
            "Smart Plan",
            "Explains why provider categories are selected for consumer versus "
            "custom-domain email targets.",
            "emailintel plan EMAIL",
        ),
        "live-output": (
            "Live Terminal Output",
            "Shows every selected public source, query/reference URL, result status, "
            "latency, evidence ID and final source links directly in the terminal.",
            "emailintel scan EMAIL --deep",
        ),
    }
    item = docs.get(name.lower())
    if not item:
        console.print("Available: confidence, timeline, coverage, plan, live-output")
        raise typer.Exit(1)
    title, meaning, command = item
    console.print(Panel.fit(
        f"[bold]{title}[/bold]\n\n{meaning}\n\n[cyan]{command}[/cyan]"
    ))


if __name__ == "__main__":
    app()
