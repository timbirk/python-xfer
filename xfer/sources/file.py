from . import Source, logger


class FileSource(Source):

    def __init__(self, work_dir=None, backup=True,
                 cleanup=True, dry_run=False, path=None):
        Source.__init__(self, work_dir, backup, cleanup, dry_run)
        self.path = path

    def do_fetch(self):
        print(self.path)

    def do_backup(self):
        pass

    def do_cleanup(self):
        pass
