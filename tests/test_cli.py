from typer.testing import CliRunner

from emailintel.cli import app

runner = CliRunner()


def test_version():
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "EmailIntel Ultra" in result.stdout


def test_plan():
    result = runner.invoke(app, ["plan", "person@gmail.com"])
    assert result.exit_code == 0
    assert "consumer-email" in result.stdout
    assert "developer" in result.stdout


def test_coverage():
    result = runner.invoke(app, ["coverage"])
    assert result.exit_code == 0
    assert "Total implemented checks" in result.stdout


def test_providers_show_sources():
    result = runner.invoke(app, ["providers"])
    assert result.exit_code == 0
    assert "GitHub Public Commit Search" in result.stdout
    assert "crt.sh Certificate Transparency" in result.stdout


def test_live_output_feature_help():
    result = runner.invoke(app, ["feature", "live-output"])
    assert result.exit_code == 0
    assert "Live Terminal Output" in result.stdout
