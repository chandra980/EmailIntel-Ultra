$ErrorActionPreference = "Stop"
$python = $null
foreach ($candidate in @("py", "python", "python3")) {
  if (Get-Command $candidate -ErrorAction SilentlyContinue) { $python = $candidate; break }
}
if (-not $python) { throw "Python 3.11+ is required." }
& $python -c "import sys; assert sys.version_info >= (3,11), 'Python 3.11+ required'"
& $python -m venv .venv
& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\pip.exe install -e .
& .\.venv\Scripts\emailintel.exe version
& .\.venv\Scripts\emailintel.exe doctor
Write-Host "INSTALLATION VERIFIED"
