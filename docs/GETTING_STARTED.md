# Getting Started

This guide is for first-time EmailIntel Ultra users.

## 1. Requirements

- Python 3.11 or newer
- Git
- Internet access
- Windows 10/11, Kali, Ubuntu, Debian, or another modern Linux distribution

No mandatory API key, OAuth login, browser plugin, or paid account is required for the currently implemented baseline.

## 2. Install on Windows

Open PowerShell:

```powershell
git clone https://github.com/chandra980/EmailIntel-Ultra.git
cd EmailIntel-Ultra
powershell -ExecutionPolicy Bypass -File install.ps1
```

If installation succeeds, verify:

```powershell
.\.venv\Scripts\emailintel.exe version
.\.venv\Scripts\emailintel.exe doctor
```

## 3. Install on Linux

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

## 4. See What Sources Exist

Windows:

```powershell
.\.venv\Scripts\emailintel.exe providers
```

Linux:

```bash
.venv/bin/emailintel providers
```

## 5. Preview the Scan Plan

```bash
emailintel plan your@email.com
```

This shows which source groups are relevant to the target.

## 6. Run Your First Full Current Scan

The current release uses `--deep` for the strongest implemented provider selection:

```bash
emailintel scan your@email.com --deep
```

Use an email address you own or are authorized to investigate.

## 7. Read the Terminal Output

Watch for:

- QUERYING
- RESULT
- provider name
- source URL
- latency
- Evidence ID
- confidence
- error/limitation

At the end, EmailIntel Ultra prints a complete result table and source links.

## 8. Open the Reports

After scanning:

```text
reports/EI-.../
```

Open `report.html` in a browser for the easiest visual review.

## 9. Important Interpretation Rule

`NOT_FOUND` means only that one provider returned no result.

It does not mean:

- the email does not exist;
- no account exists anywhere;
- no other public reference exists.

## 10. Future Terminal Interface

The repository includes a professional neon terminal UI specification. It defines the planned command-center experience and eventual single-command full-deep workflow.

See:

```text
docs/TERMINAL_UI_SPEC.md
```
