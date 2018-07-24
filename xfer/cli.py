import os
import sys
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

    if profile not in xfer_config.profiles:
        logger.critical("xfer profile: %s not found in configuration: %s" % (
            profile, config))
        sys.exit(1)

    logger.info("Running %s for profile: %s" % (
        os.path.basename(sys.argv[0]),
        profile
    ))

    if dry_run:
        logger.warning("Dry run enabled: No actions will be taken on this run")

    pass
