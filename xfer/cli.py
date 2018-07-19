import click
from .config import Config
from .multilogger import MultiLogger


@click.command()
@click.option('--dry-run', '-n', is_flag=True, help='Output what would happen.')
@click.option('--config', '-c', default='~/.xfer.yaml', help='Configuration file.')
@click.argument('profile', required=True)
def main(profile, dry_run, config):
    """A file transfer cli to rule them all."""
    xfer_config = Config(config_filename=config)
    logger = MultiLogger(loggers=xfer_config.loggers).getLogger()

    logger.info("test log")
    pass
