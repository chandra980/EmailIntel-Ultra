# Usage Guide

## Recommended Current Command

For maximum currently implemented provider coverage:

```bash
emailintel scan target@example.com --deep
```

## Available Scan Controls

Current implementation:

```bash
emailintel scan EMAIL --fast
emailintel scan EMAIL --mode balanced
emailintel scan EMAIL --deep
```

Recommended: `--deep`.

The terminal UI specification plans to replace these user-facing scan choices with one automatic full-deep workflow.

## Before Scanning

Run:

```bash
emailintel plan EMAIL
```

The planner classifies the target and explains selected/excluded categories.

## Provider Inventory

```bash
emailintel providers
```

This lists actual implemented providers only.

## Coverage

```bash
emailintel coverage
```

Coverage is provider/category coverage, not a claim that the whole Internet was searched.

## Doctor

```bash
emailintel doctor
```

Checks Python, local SQLite, DNS/network resolution, and provider registry availability.

## Scan Output

The normal live scan prints:

1. target and mode;
2. selected provider/source table;
3. QUERYING events;
4. RESULT events;
5. final investigation summary;
6. complete terminal results;
7. source-link table;
8. evidence-detail panels;
9. saved report paths.

## Quiet Mode

```bash
emailintel scan EMAIL --deep --quiet
```

This suppresses live provider trace but still prints the final formatted result.

## Redaction

```bash
emailintel scan EMAIL --deep --redact
```

This masks the email in terminal summary output.

## No History

```bash
emailintel scan EMAIL --deep --no-history
```

Prevents saving the scan to local SQLite history.

## Report Format

```bash
emailintel scan EMAIL --deep --format html
emailintel scan EMAIL --deep --format json
emailintel scan EMAIL --deep --format csv
emailintel scan EMAIL --deep --format txt
emailintel scan EMAIL --deep --format all
```

## Timeline

```bash
emailintel timeline SCAN_ID
```

Shows locally stored evidence ordered by observation/retrieval time.

## Confidence Explanation

```bash
emailintel explain SCAN_ID EVD_ID
```

Shows why a stored evidence item received its confidence value.

## Compare Scans

```bash
emailintel diff SCAN_A SCAN_B
```

Compares normalized evidence hashes between two saved scans.

## Important Limitations

EmailIntel Ultra does not:

- prove account ownership from one public reference;
- reveal private login history;
- retrieve leaked password values;
- bypass CAPTCHA;
- bypass authentication;
- bypass rate limits;
- access private repositories/accounts.

## Update the Project

```bash
git pull
```

Then reinstall editable package:

Windows:

```powershell
.\.venv\Scripts\pip.exe install -e .
```

Linux:

```bash
.venv/bin/pip install -e .
```
