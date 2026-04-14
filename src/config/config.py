import os


CONFIG_DIR = os.path.join(os.path.expanduser("~"), ".config", "myapp")


def get_config_path(filename):
    return os.path.join(CONFIG_DIR, filename)


def config_exists(filename):
    return os.path.exists(os.path.join(CONFIG_DIR, filename))


def get_config_dir():
    return CONFIG_DIR


def ensure_config_dir():
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)
    return CONFIG_DIR


def get_default_config():
    base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, "defaults", "config.json")
