#!/usr/bin/env python

import unittest
import yaml

from collections import OrderedDict
from xfer.config import Config


class ConfigTest(unittest.TestCase):

    def test_config_defaults(self):
        config = Config('tests/fixtures/xfer_profiles_only.yaml')
        self.assertEqual(config.config_filename,
                         'tests/fixtures/xfer_profiles_only.yaml')
        self.assertIsNotNone(config.default_config)

    def test_full_config(self):
        config = Config('tests/fixtures/xfer_full.yaml')
        self.assertEqual(config.work_dir, '/opt/xfer')
        self.assertEqual(config.loggers,
                         {'gelf': {'post': 12021, 'host': 'localhost'},
                          'console': {'level': 'info'}})
        self.assertEqual(config.monitoring,
                         {'port': 13030, 'host': '127.0.0.1'})
        self.assertIsInstance(config.profiles, OrderedDict)

    def test_config_with_bad_yaml(self):
        with self.assertRaises(yaml.YAMLError):
            Config('tests/fixtures/xfer_bad.yaml')

    def test_config_not_there(self):
        with self.assertRaises(IOError):
            Config('tests/fixtures/xfer_not_exist.yaml')

    def test_config_without_profiles(self):
        with self.assertRaises(KeyError):
            Config('tests/fixtures/xfer_no_profiles.yaml')


if __name__ == "__main__":
    unittest.main()
