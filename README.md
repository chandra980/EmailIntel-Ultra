# EmailIntel Ultra

**Advanced Passive Email OSINT & Public Identity Intelligence Framework**  
Created and maintained by **Chandra Kumar Yadav**

Zero mandatory API keys · Zero mandatory login · Evidence-first · Live terminal intelligence · Windows/Linux · Professional reports

## What it is

EmailIntel Ultra is an open-source Python CLI for lawful, passive analysis of publicly accessible email-related information. It is designed to show the operator **what is being checked, which public source is being queried, what came back, how long each source took, and the direct source/reference URL** — directly in the terminal as well as in saved reports.

The project prioritizes evidence provenance, transparent confidence, target-aware scan planning, domain/mail intelligence, honest provider counts, and reproducible reporting.

## Terminal-first workflow

A normal scan now works like this:

```text
TARGET
  ↓
SCAN PLAN
  ↓
PUBLIC SOURCES SELECTED
  ↓
QUERYING source + query/reference URL
  ↓
RESULT status + latency + source link
  ↓
COMPLETE TERMINAL RESULTS
  ↓
SOURCE LINKS / WHERE DATA CAME FROM
  ↓
DETAILED EVIDENCE PANELS
  ↓
HTML / JSON / CSV / TXT reports saved
```

You do **not** need to open the report file just to understand the scan. The report is an additional saved artifact.

## Implemented public/no-login sources

| Provider | Source | Purpose | Target |
|---|---|---|---|
| email-validator | Local validation | Syntax, normalization, target classification | All |
| dns-mail-intelligence | Public DNS | MX/TXT/NS/DMARC mail-domain intelligence | All |
| public-rdap | RDAP.org | Public registration metadata | Custom domains |
| github-public-commit-search | GitHub public commit index | Exact public author-email commit references | All |
| crtsh-certificate-transparency | crt.sh | Public certificate-transparency/domain history | Custom domains |
| gravatar-public-profile | Gravatar | Public profile association by normalized email hash | All |
| openpgp-public-key | keys.openpgp.org | Public OpenPGP email-key publication | All |

No provider is counted as implemented unless code exists in the repository.

## Why can a scan finish in seconds?

EmailIntel Ultra runs independent public-source checks concurrently. A fast result does **not** mean it scanned the entire Internet.

The terminal shows:

- exactly which providers were selected;
- each source/query reference;
- when a provider starts;
- each provider result;
- latency in milliseconds;
- total scan time;
- how many evidence records were produced.

For a consumer email such as Gmail, irrelevant corporate-domain checks are intentionally skipped. For a custom-domain email, RDAP and certificate-transparency checks can be added automatically.

Use:

```bash
emailintel plan EMAIL
```

to see why categories will be selected or skipped before scanning.

## Main scan commands

### Fast public scan

```bash
emailintel scan EMAIL --fast
```

Uses the smaller, high-value provider set.

### Balanced scan

```bash
emailintel scan EMAIL --mode balanced
```

Runs the normal target-aware provider set.

### Deep scan

```bash
emailintel scan EMAIL --deep
```

Runs all currently eligible implemented public providers.

### Reduce terminal trace

```bash
emailintel scan EMAIL --deep --quiet
```

This suppresses per-provider live trace but still prints the complete final formatted result.

## What you see in the terminal

For every selected network source:

```text
QUERYING [1/5] GitHub Public Commit Search
          provider: github-public-commit-search
          source:   https://api.github.com/search/commits?...

RESULT FOUND github-public-commit-search — Exact public GitHub commit email reference(s): 2 (412 ms)
          https://api.github.com/search/commits?...
```

The final output includes:

- scan ID;
- target;
- mode;
- elapsed time;
- evidence count;
- positive-finding count;
- complete formatted results table;
- evidence ID;
- status;
- confidence;
- latency;
- source URLs;
- evidence-family ID;
- raw normalized details;
- provider errors/limitations.

Rich-compatible terminals render HTTP links as clickable hyperlinks. The raw URL is still printed for terminals that do not support clickable links.

## Windows

```powershell
git clone https://github.com/chandra980/EmailIntel-Ultra.git
cd EmailIntel-Ultra
powershell -ExecutionPolicy Bypass -File install.ps1

.\.venv\Scripts\emailintel.exe doctor
.\.venv\Scripts\emailintel.exe providers
.\.venv\Scripts\emailintel.exe plan example@example.com
.\.venv\Scripts\emailintel.exe scan example@example.com --deep
```

## Linux / Kali / Ubuntu / Debian

```bash
git clone https://github.com/chandra980/EmailIntel-Ultra.git
cd EmailIntel-Ultra
bash install.sh

.venv/bin/emailintel doctor
.venv/bin/emailintel providers
.venv/bin/emailintel plan example@example.com
.venv/bin/emailintel scan example@example.com --deep
```

## Other commands

```bash
emailintel providers
emailintel coverage
emailintel doctor
emailintel timeline SCAN_ID
emailintel explain SCAN_ID EVD_ID
emailintel diff SCAN_A SCAN_B
emailintel feature live-output
emailintel feature confidence
emailintel version
```

## Reports

Every scan can create:

```text
reports/EI-YYYYMMDD-XXXXXX/
├── report.html
├── report.json
├── findings.csv
└── summary.txt
```

Files remain useful for archiving and analysis, but the main scan result is also fully visible in the terminal.

## Evidence model

Each finding records:

- Evidence ID
- Scan ID
- provider/category
- result status
- confidence
- freshness
- direct source/query URL where available
- provider/parser version
- SHA-256 normalized evidence hash
- evidence-family ID
- retrieval timestamp
- structured details
- provider error when relevant

## Repository update policy — latest implementation only

The `main` branch is the single current implementation.

When an existing feature is replaced:

- update/replace the existing implementation;
- do not create `v2/`, `v3/`, `old/`, `legacy/` or duplicate runnable implementations;
- remove obsolete code when it is no longer required;
- keep documentation aligned with the current code.

Git commit history remains available naturally for audit/recovery, but users should see only the latest runnable implementation in the repository tree.

## Important limitations

- Does not reveal private login history.
- Does not retrieve, test, or display leaked passwords.
- Does not bypass CAPTCHA, authentication, rate limits, or private APIs.
- NOT_FOUND from one source is not proof that an account does not exist elsewhere.
- Historical public evidence does not prove current identity or affiliation.
- Provider availability depends on the remote source and network state.
- A quick scan means the selected sources completed quickly; it does not mean the entire Internet was scanned.

## Responsible use

Use EmailIntel Ultra only for lawful OSINT, defensive security research, authorized investigations, or analysis of information that is genuinely public and anonymously accessible.

## Advanced specification

The full advanced specification is in [docs/ADVANCED_SPEC.md](docs/ADVANCED_SPEC.md). Roadmap items are not marked implemented until code and tests exist.

## License

MIT.
