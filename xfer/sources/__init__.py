class Source(object):

    def __init__(self, backup=False, cleanup=True, dry_run=False):
        self.backup = backup
        self.cleanup = cleanup
        self.dry_run = dry_run

    def get(self):
        pass

    def __fetch(self):
        pass

    def __backup(self):
        pass

    def __cleanup(self):
        pass
