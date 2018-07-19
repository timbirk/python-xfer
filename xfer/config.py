#!/usr/bin/env python

import yaml
from collections import defaultdict

DEFAULT_CONFIG = '''
loggers:
  console:
    level: info
monitoring:
  sensu:
    host: localhost
    port: 3030
'''


class Config(object):

    def __init__(self, config_filename='~/xfer.yaml'):
        '''
        The Config class is intended to resolve configuration from sensible
        defaults and user provided configuration.

        :arg str config_filename: Name / path to the configuration file on which
            this config object.
        '''

        self.config_filename = config_filename

        self.default_config = self._init_defaults()

        self.loggers = defaultdict(None)
        self.monitoring = defaultdict(None)
        self.profiles = defaultdict(None)

        self._setup()

    def _init_defaults(self):
        '''Initialise default configuration from DEFAULT_CONFIG
        '''
        return yaml.load(DEFAULT_CONFIG)

    def _setup(self):
        '''Reads in the xfer config file on sets config values appropriately
        '''
        try:
            with open(self.config_filename, 'r') as stream:
                try:
                    user_config = yaml.safe_load(stream)

                    if user_config and 'profiles' in user_config:
                        self.profiles = user_config['profiles']
                    else:
                        raise KeyError("Unable to find profiles in: %s" %
                                       self.config_filename)

                    if user_config and 'loggers' in user_config:
                        self.loggers = user_config['loggers']
                    else:
                        self.loggers = self.default_config['loggers']

                    if user_config and 'monitoring' in user_config:
                        self.monitoring = user_config['monitoring']
                    else:
                        self.monitoring = self.default_config['monitoring']

                except yaml.YAMLError as exc:
                    print("Error in configuration file: %s" % exc)
                    if hasattr(exc, 'problem_mark'):
                        mark = exc.problem_mark
                        print("Error position: (%s:%s)" % (mark.line+1,
                                                           mark.column+1))
                    raise

        except IOError:
            print("Can't find or open config file: %s" % self.config_filename)
            raise
