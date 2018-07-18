#!/usr/bin/env python

import unittest
import yaml

from xfer.config import Config


class ConfigTest(unittest.TestCase):

    def test_config_defaults(self):
        config = Config('tests/fixtures/xfer_profiles_only.yaml')
        self.assertEqual(config.config_filename,
                         'tests/fixtures/xfer_profiles_only.yaml')
        self.assertIsNotNone(config.default_config)

    def test_config_with_bad_yaml(self):
        with self.assertRaises(yaml.YAMLError):
            Config('tests/fixtures/xfer_bad.yaml')


if __name__ == "__main__":
    unittest.main()
