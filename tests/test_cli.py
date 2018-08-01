import pytest
from click.testing import CliRunner
from xfer import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_cli(runner, caplog):
    result = runner.invoke(cli.main)
    assert result.exit_code == 2
    assert 'Error: Missing argument "profile".' in result.output.strip()
    assert result.exception


def test_cli_with_profile_and_no_config(runner, caplog):
    result = runner.invoke(cli.main, ['--config', 'nothere.yaml', 'test'])
    assert result.exception
    assert result.exit_code == -1
    assert 'Can\'t find or open config file: nothere.yaml' in result.output.strip()


def test_cli_with_config_and_bad_profile(runner, caplog):
    result = runner.invoke(cli.main, ['--config',
                                      'tests/fixtures/xfer_full.yaml', 'test'])
    assert result.exception
    assert result.exit_code == 1
    assert 'profile test not found' in caplog.text


def test_cli_dry_run_with_config_and_profile(runner, caplog):
    result = runner.invoke(cli.main, ['--dry-run', '--config',
                                      'tests/fixtures/xfer_full.yaml',
                                      'files_to_s3'])
    assert not result.exception
    assert result.exit_code == 0
    assert 'profile files_to_s3 running' in caplog.text
    assert 'dry_run enabled' in caplog.text


def test_cli_with_config_and_profile(runner, caplog):
    result = runner.invoke(cli.main, ['--config',
                                      'tests/fixtures/xfer_full.yaml',
                                      'files_to_s3'])
    assert not result.exception
    assert result.exit_code == 0
    assert 'profile files_to_s3 running' in caplog.text
