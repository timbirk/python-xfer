import os
import sys
import click
from .config import Config
from .multilogger import MultiLogger
from .monitoring import Monitoring
from .sources import Source
from .sources.file import FileSource

@click.command()
@click.option('--dry-run', '-n', is_flag=True, help='Output what would happen.')
@click.option('--config', '-c', default='~/.xfer.yaml', help='Configuration file.')
@click.argument('profile', required=True)
def main(profile, dry_run, config):
    """A file transfer cli to rule them all."""

    xfer_config = Config(config_filename=config)
    logger = MultiLogger(loggers=xfer_config.loggers).getLogger()
    monitoring = Monitoring(profile=profile, options=xfer_config.monitoring)

    if profile not in xfer_config.profiles:
        logger.critical("profile %s not found in configuration %s" % (
            profile, config))
        monitoring.unknown(
            message="profile %s not found in configuration %s" %
            (profile, config))
        sys.exit(1)

    logger.info("profile %s running" % (profile))

    if dry_run:
        logger.warning("dry_run enabled")

    run_profile = xfer_config.profiles[profile]

    if 'src' not in run_profile:
        logger.critical("profile %s has no src configuration" % profile)

        monitoring.unknown(
            message="profile %s has no src configuration" % profile)
        sys.exit(1)

    run_src = run_profile['src']
    if len(run_src) > 1:
        logger.critical(
            "profile %s src configuration must only contain 1 src type"
            % profile)

        monitoring.unknown(
            message="profile %s src configuration must only contain 1 src type"
            % profile)
        sys.exit(1)

    if 'file' in run_src:
        work_files = FileSource(work_dir=xfer_config.work_dir,
                                **run_src['file']).get()

    pass
