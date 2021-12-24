# tests/{{ cookiecutter.project_slug }}/test_cli.py

from typer.testing import CliRunner

from {{cookiecutter.project_slug}} import __version__
from {{cookiecutter.project_slug}}.cli import app

runner = CliRunner()


def test_cli_without_args_options():
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert "42" in result.stdout


def test_cli_with_option_version():
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert result.stdout == f"{__version__}\n"
