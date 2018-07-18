#!/usr/bin/env python

import yaml
from collections import defaultdict

DEFAULT_CONFIG = """
logging:
  console:
    level: info
monitoring:
  sensu:
    host: localhost
    port: 3030
"""


class Config(object):

    def __init__(self, config_filename='~/xfer.yaml'):
        """
        The Config class is intended to resolve configuration from sensible
        defaults and user provided configuration.

        :arg str config_filename: Name / path to the configuration file on which
            this config object.
        """

        self.config_filename = config_filename

        self.default_config = self._init_defaults()

        self.logging = defaultdict(None)
        self.monitoring = defaultdict(None)
        self.profiles = defaultdict(None)

        self._setup()

    def _init_defaults(self):
        """Initialise default configuration from DEFAULT_CONFIG
        """
        return yaml.load(DEFAULT_CONFIG)

    def _setup(self):
        """Reads in the xfer config file on sets config values appropriately
        """

        with open(self.config_filename, 'r') as stream:
            try:
                print(yaml.load(stream))
            except yaml.YAMLError as exc:
                print("Error in configuration file: %s" % exc)
                if hasattr(exc, 'problem_mark'):
                    mark = exc.problem_mark
                    print("Error position: (%s:%s)" % (mark.line+1,
                                                       mark.column+1))
                raise yaml.YAMLError
