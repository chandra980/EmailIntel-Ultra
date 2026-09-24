# EmailIntel Ultra

**Advanced Passive Email OSINT & Public Identity Intelligence Framework**  
Created and maintained by **Chandra Kumar Yadav**

Evidence-first · Public/no-login sources · Windows/Linux · Live terminal output · HTML/JSON/CSV/TXT reports

> EmailIntel Ultra is designed for lawful, authorized public-source investigation. It does not retrieve passwords, private login history, session data, or bypass authentication/CAPTCHA/rate limits.

---

## Current Project Status

EmailIntel Ultra currently has a **working CLI baseline** with:

- email validation and classification;
- live terminal source tracing;
- public DNS / mail intelligence;
- RDAP for custom domains;
- GitHub public commit references;
- certificate-transparency intelligence;
- Gravatar public-profile checks;
- OpenPGP public-key checks;
- evidence IDs and evidence-family hashes;
- confidence and freshness metadata;
- SQLite scan history;
- scan timeline and diff;
- HTML / JSON / CSV / TXT reports;
- Windows and Linux installers;
- automated tests / GitHub Actions.

The new professional neon terminal command-center design is documented in:

- [Terminal UI Specification](docs/TERMINAL_UI_SPEC.md)
- [Advanced Intelligence Specification](docs/ADVANCED_SPEC.md)

Those specification documents describe the **next implementation target**. Features are not considered implemented until code and tests exist.

---

# Quick Start

## Windows

Open **PowerShell**:

```powershell
git clone https://github.com/chandra980/EmailIntel-Ultra.git
cd EmailIntel-Ultra
powershell -ExecutionPolicy Bypass -File install.ps1
```

Verify installation:

```powershell
.\.venv\Scripts\emailintel.exe version
.\.venv\Scripts\emailintel.exe doctor
```

Run the strongest currently implemented scan:

```powershell
.\.venv\Scripts\emailintel.exe scan your@email.com --deep
```

## Linux / Kali / Ubuntu / Debian

```bash
git clone https://github.com/chandra980/EmailIntel-Ultra.git
cd EmailIntel-Ultra
bash install.sh
```

Verify:

```bash
.venv/bin/emailintel version
.venv/bin/emailintel doctor
```

Run the strongest currently implemented scan:

```bash
.venv/bin/emailintel scan your@email.com --deep
```

---

# Recommended Workflow

For the current working release:

```text
INSTALL
  ↓
DOCTOR
  ↓
PROVIDERS
  ↓
PLAN
  ↓
DEEP SCAN
  ↓
TERMINAL RESULTS
  ↓
SOURCE LINKS
  ↓
SAVED REPORTS
```

Commands:

```bash
emailintel doctor
emailintel providers
emailintel plan target@example.com
emailintel scan target@example.com --deep
```

---

# What the Terminal Shows

During a scan, EmailIntel Ultra displays:

- target;
- selected scan mode;
- selected public-source providers;
- source/query reference;
- provider start event;
- result status;
- latency;
- evidence ID;
- direct source URL where available.

Example:

```text
QUERYING [2/6] GitHub Public Commit Search
provider: github-public-commit-search
source: https://api.github.com/...

RESULT FOUND
Exact public GitHub commit email reference(s): 2
Latency: 421 ms
Source: https://api.github.com/...
```

At completion, the terminal prints:

- final investigation summary;
- complete result table;
- confidence;
- freshness;
- evidence IDs;
- source links;
- provider errors/limitations;
- detailed evidence panels.

---

# Current Scan Modes

The current CLI still supports:

```bash
emailintel scan EMAIL --fast
emailintel scan EMAIL --mode balanced
emailintel scan EMAIL --deep
```

For maximum currently implemented public-source coverage, use:

```bash
emailintel scan EMAIL --deep
```

The terminal UI specification defines the future UX where the normal command becomes simply:

```bash
emailintel scan EMAIL
```

and automatically performs the full eligible deep scan without exposing fast/balanced/deep choices.

That single-command behavior is a **planned replacement**, not yet claimed as implemented.

---

# Public Sources Currently Implemented

| Provider | Public Source | Purpose |
|---|---|---|
| email-validator | Local deterministic validation | Syntax, normalization, classification |
| dns-mail-intelligence | Google Public DNS-over-HTTPS | MX/TXT/NS/DMARC mail-domain intelligence |
| public-rdap | RDAP.org | Public domain registration metadata |
| github-public-commit-search | GitHub public commit index | Exact public author-email references |
| crtsh-certificate-transparency | crt.sh | Public certificate history / related hostnames |
| gravatar-public-profile | Gravatar | Public profile association |
| openpgp-public-key | keys.openpgp.org | Public OpenPGP email-key publication |

The project deliberately avoids fake provider counts. A provider is listed as implemented only when repository code exists.

---

# Consumer Email vs Custom-Domain Email

EmailIntel Ultra uses target-aware planning.

For addresses such as:

```text
person@gmail.com
person@yahoo.com
person@outlook.com
```

organization/RDAP/certificate data for the provider domain may be irrelevant to the individual, so those checks can be skipped.

For:

```text
employee@company.com
```

custom-domain intelligence can include:

- DNS;
- RDAP;
- mail infrastructure;
- certificate transparency;
- organization-related domain context;
- developer/public references.

Use:

```bash
emailintel plan EMAIL
```

to see why categories are selected or excluded.

---

# Main Commands

## Show version

```bash
emailintel version
```

## Diagnose the installation

```bash
emailintel doctor
```

## Show implemented providers

```bash
emailintel providers
```

## Show coverage

```bash
emailintel coverage
```

## Explain the scan plan

```bash
emailintel plan target@example.com
```

## Run the strongest current scan

```bash
emailintel scan target@example.com --deep
```

## Reduce live terminal trace

```bash
emailintel scan target@example.com --deep --quiet
```

## Show a saved scan timeline

```bash
emailintel timeline SCAN_ID
```

## Explain confidence for evidence

```bash
emailintel explain SCAN_ID EVD_ID
```

## Compare two saved scans

```bash
emailintel diff SCAN_A SCAN_B
```

---

# Reports

By default, a scan can generate:

```text
reports/
└── EI-YYYYMMDD-XXXXXX/
    ├── report.html
    ├── report.json
    ├── findings.csv
    └── summary.txt
```

### HTML
Best for human review.

### JSON
Best for automation and downstream processing.

### CSV
Best for spreadsheet analysis.

### TXT
Best for quick plain-text archiving.

---

# Evidence Model

Each finding can include:

- Evidence ID;
- Scan ID;
- provider;
- category;
- status;
- confidence;
- freshness;
- direct source URL;
- retrieval timestamp;
- provider/parser version;
- normalized SHA-256 evidence hash;
- evidence-family ID;
- structured details;
- error/limitation information.

A confidence score describes evidence strength. It is not proof of real-world identity ownership.

---

# Understanding Result States

### VERIFIED
Strong direct public evidence passed the provider parser.

### FOUND
A relevant public reference was returned.

### NOT_FOUND
That provider returned no result. It does **not** prove that the information does not exist anywhere else.

### RATE_LIMITED
The public source refused more requests. EmailIntel Ultra does not bypass the limit.

### UNAVAILABLE
The source could not provide a usable response.

### ERROR
The provider failed locally or remotely. Other providers continue.

---

# Updating Your Local Copy

If you already cloned the repository:

```bash
cd EmailIntel-Ultra
git pull
```

Then refresh the editable install.

Windows:

```powershell
.\.venv\Scripts\pip.exe install -e .
```

Linux:

```bash
.venv/bin/pip install -e .
```

---

# Documentation

| Guide | Purpose |
|---|---|
| [Getting Started](docs/GETTING_STARTED.md) | Beginner installation and first scan |
| [Usage Guide](docs/USAGE.md) | Commands, scan workflow and reports |
| [Troubleshooting](docs/TROUBLESHOOTING.md) | Common Windows/Linux issues |
| [Project Status](docs/PROJECT_STATUS.md) | Implemented vs specification/roadmap |
| [Terminal UI Specification](docs/TERMINAL_UI_SPEC.md) | Dark/light-green professional TUI target |
| [Advanced Specification](docs/ADVANCED_SPEC.md) | Long-term advanced intelligence architecture |
| [Responsible Use](docs/responsible-use.md) | Legal/safety operating boundaries |

---

# Professional Terminal UI Direction

The current terminal UI specification requires a **dark terminal + light-green intelligence interface**, a command-center layout, clear source status, evidence navigation, ETA, professional progress views, and a final deep-investigation screen. fileciteturn125file0L39-L83

It also specifies that the eventual primary workflow should expose only **FULL DEEP INTELLIGENCE SCAN** to normal users. fileciteturn125file0L164-L189

This is the implementation direction, while the README keeps current executable behavior clearly separated from planned functionality.

---

# Responsible Use

Use EmailIntel Ultra only for:

- your own email addresses;
- authorized security assessments;
- lawful public-source research;
- defensive investigation;
- legitimate incident-response/research workflows.

The project does not support:

- credential attacks;
- password retrieval;
- login/recovery probing;
- CAPTCHA bypass;
- authentication bypass;
- private-data extraction;
- stolen-data access;
- rate-limit evasion.

---

# Repository Policy

The `main` branch contains the latest runnable implementation.

When functionality is replaced:

- update the existing implementation;
- remove obsolete code when appropriate;
- update tests and documentation;
- do not create duplicate runnable `v2/`, `v3/`, `old/` or `legacy/` implementations.

Git history remains available naturally for audit and recovery.

---

# License

MIT License.

Copyright © 2026 Chandra Kumar Yadav.
