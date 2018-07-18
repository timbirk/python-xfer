import pytest
from click.testing import CliRunner
from xfer import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_cli(runner):
    result = runner.invoke(cli.main)
    assert result.exit_code == 2
    assert 'Error: Missing argument "profile".' in result.output.strip()
    assert result.exception


def test_cli_with_profile_and_no_config(runner):
    result = runner.invoke(cli.main, ['--config', 'nothere.yaml', 'test'])
    assert result.exception
    assert result.exit_code == -1
    assert 'Can\'t find or open config file: nothere.yaml' in result.output.strip()
