"""
Config Utilities for Automation Framework.

@author: Raed Eleyan.
@contact: raedeleyan1@gmail.com
@date: 10/14/2025
"""
import os
import json


class ConfigUtilities:

    CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config", "config.json")
    def __init__(self):
        self.config = self._load_config()

    def _load_config(self) -> dict:
        """
        Load the JSON config file.

        :return: The configuration as a dictionary.
        :raises FileNotFoundError: If the config file doesn't exist.
        """
        if not os.path.exists(self.CONFIG_PATH):
            raise FileNotFoundError(f"Config file {self.CONFIG_PATH} doesn't exist.")
        with open(self.CONFIG_PATH) as f:
            return json.load(f)

    def get_webdriver_mode(self) -> str:
        """
        Get the WebDriver mode from the configuration file.

        :return: 'local' or 'grid'.
        :raises KeyError: if the 'mode' key is missing in the configuration file.
        """
        mode = self.config.get('mode')
        if not mode:
            raise KeyError("The 'mode' key is missing in the configuration file.")
        return mode.lower()

    def get_specified_browser(self) -> str:
        """
        Get the browser specified in the configuration file.

        :return: The browser name (e.g., 'chrome', 'firefox')
        :raises KeyError: if the 'browser' key is missing in the configuration file.
        """
        browser = self.config.get('browser')
        if not browser:
            raise KeyError("THe 'browser' key is missing in the configuration file.")
        return browser.lower()
