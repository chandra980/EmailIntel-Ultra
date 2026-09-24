# Troubleshooting

## Command Not Found

### Windows

Use the executable inside the virtual environment:

```powershell
.\.venv\Scripts\emailintel.exe version
```

If missing:

```powershell
.\.venv\Scripts\pip.exe install -e .
```

### Linux

```bash
.venv/bin/emailintel version
```

If missing:

```bash
.venv/bin/pip install -e .
```

## Python Version Error

Check:

```bash
python --version
```

or:

```bash
python3 --version
```

Use Python 3.11+.

## PowerShell Blocks the Installer

Use:

```powershell
powershell -ExecutionPolicy Bypass -File install.ps1
```

## Doctor Reports DNS Failure

Check Internet/DNS connectivity.

Try opening:

```text
https://rdap.org/
https://dns.google/
```

Provider failures should not stop the rest of the scan.

## Provider Shows RATE_LIMITED

This is not a local installation bug.

The remote public service may be limiting requests. EmailIntel Ultra intentionally does not bypass rate limits.

Try again later.

## Provider Shows UNAVAILABLE

The remote service may be:

- offline;
- temporarily slow;
- returning an unexpected response;
- blocking automated requests.

Other provider results remain valid independently.

## Scan Finishes Very Quickly

A quick result means the selected providers completed quickly.

It does not mean the entire Internet was scanned.

Use:

```bash
emailintel providers
emailintel plan EMAIL
```

to understand exactly what was eligible and implemented.

## HTML Report Does Not Open Automatically

Open manually:

```text
reports/EI-.../report.html
```

## Old Code After git pull

Refresh the editable install:

Windows:

```powershell
.\.venv\Scripts\pip.exe install -e .
```

Linux:

```bash
.venv/bin/pip install -e .
```

## Need More Diagnostic Detail

Run:

```bash
emailintel doctor
emailintel version
emailintel providers
```

When reporting a bug, include:

- operating system;
- Python version;
- command used;
- complete error text;
- provider name if relevant.

Do not include passwords, private tokens, cookies, or secrets in bug reports.
