import os
import sys
import logging

logger = logging.getLogger(os.path.basename(sys.argv[0]))


class Source(object):

    def __init__(self, work_dir=None, backup=False,
                 cleanup=True, dry_run=False):
        self.work_dir = work_dir
        self.backup = backup
        self.cleanup = cleanup
        self.dry_run = dry_run

    def get(self):
        self.__fetch()
        if self.backup:
            self.__backup()
        else:
            logger.warning("src backup disabled")
        if self.cleanup:
            self.__cleanup()
        else:
            logger.info("src cleanup disabled")


    def __fetch(self):
        logger.info("fetching from src")
        self.do_fetch()

    def __backup(self):
        logger.info("creating src backup")
        self.do_backup()

    def __cleanup(self):
        logger.warning("cleaning up src")
        self.do_cleanup()
