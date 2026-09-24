# EmailIntel Ultra

**Advanced Passive Email OSINT & Public Identity Intelligence Framework**  
Created and maintained by **Chandra Kumar Yadav**

Zero mandatory API keys · Zero mandatory login · Evidence-first · Windows/Linux · Professional reports

## What it is
EmailIntel Ultra is an open-source Python CLI for lawful, passive analysis of publicly accessible email-related information. It focuses on evidence provenance, transparent confidence, target-aware scan planning, domain/mail intelligence, and reproducible reporting rather than inflated provider counts.

## Implemented now

| Feature | Purpose | Command | Status |
|---|---|---|---|
| Email validation | Normalize/classify a target | `emailintel scan EMAIL` | Implemented |
| Smart scan plan | Explain category selection | `emailintel plan EMAIL` | Implemented |
| DNS mail intelligence | MX/TXT/NS/DMARC public records | scan | Implemented |
| Public RDAP | Public custom-domain registration metadata | scan | Implemented |
| Gravatar public profile | Exact normalized email hash association | scan | Implemented |
| OpenPGP public key | Detect a published public key | scan | Implemented |
| Evidence ledger | IDs, hashes, family IDs, parser/provider versions | scan | Implemented |
| SQLite history | Local scan history | default | Implemented |
| Confidence explanation | Explain stored evidence confidence | `emailintel explain SCAN EVD` | Implemented |
| Timeline | Chronological stored evidence view | `emailintel timeline SCAN` | Implemented |
| Scan diff | Compare evidence hashes across scans | `emailintel diff A B` | Implemented |
| Coverage matrix | Honest implemented-provider count | `emailintel coverage` | Implemented |
| Doctor | Runtime/DNS/SQLite/provider diagnostics | `emailintel doctor` | Implemented |
| HTML/JSON/CSV/TXT reports | Professional export | `--format all` | Implemented |

## Important limitations
- Does not reveal private login history.
- Does not retrieve, test, or display leaked passwords.
- Does not bypass CAPTCHA, authentication, rate limits, or private APIs.
- NOT_FOUND from one source is not proof that an account does not exist elsewhere.
- Historical public evidence does not prove current identity or affiliation.
- Provider availability depends on the remote source and network state.

## Windows
```powershell
git clone https://github.com/chandra980/EmailIntel-Ultra.git
cd EmailIntel-Ultra
powershell -ExecutionPolicy Bypass -File install.ps1
.\.venv\Scripts\emailintel.exe doctor
.\.venv\Scripts\emailintel.exe scan example@example.com --fast
```

## Linux / Kali / Ubuntu / Debian
```bash
git clone https://github.com/chandra980/EmailIntel-Ultra.git
cd EmailIntel-Ultra
bash install.sh
.venv/bin/emailintel doctor
.venv/bin/emailintel scan example@example.com --fast
```

## Core commands
```bash
emailintel scan EMAIL --fast
emailintel scan EMAIL --mode balanced
emailintel scan EMAIL --deep
emailintel plan EMAIL
emailintel providers
emailintel coverage
emailintel doctor
emailintel timeline SCAN_ID
emailintel explain SCAN_ID EVD_ID
emailintel diff SCAN_A SCAN_B
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

## Evidence model
Each finding records Evidence ID, Scan ID, provider/category, status, confidence, freshness, source URL, provider/parser version, SHA-256 normalized evidence hash, evidence-family ID, and retrieval timestamp.

## Responsible use
Use EmailIntel Ultra only for lawful OSINT, defensive security research, authorized investigations, or analysis of information that is genuinely public and anonymously accessible.

## Advanced specification
The full advanced specification is in [docs/ADVANCED_SPEC.md](docs/ADVANCED_SPEC.md). Roadmap items are not marked implemented until code and tests exist.

## License
MIT.
