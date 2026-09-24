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


def test_coverage():
    result = runner.invoke(app, ["coverage"])
    assert result.exit_code == 0
    assert "Total implemented provider checks" in result.stdout
