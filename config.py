import configparser
import sys


class ConfigReader:

    @staticmethod
    def read_config(section, key):
        root_dir = sys.path[0]

        config = configparser.ConfigParser()
        config.read(root_dir + '/config.ini')

        # Check that the Section & key exists
        if config.has_section(section) and config.has_option(section, key):
            return config[section][key]
        else:
            raise KeyError(f"Section '{section}' or key '{key}' not found in config.ini")
