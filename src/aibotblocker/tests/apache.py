import json
import os.path
import unittest
from aibotblocker.servers.apache import create_config


class TestApache(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

        with open(os.path.join("tests", "config.json"), "r") as config_file:
            self.config = json.load(config_file)

    def test_create_config(self):
        actual = create_config(
            self.config["comment"],
            self.config["user_agents"],
        ).strip()

        with open(os.path.join("tests", "apache.conf"), "r") as robots_conf_file:
            expected = robots_conf_file.read().strip()

        print(actual)

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
