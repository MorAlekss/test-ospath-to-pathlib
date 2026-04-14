from pathlib import Path


CONFIG_DIR = str(Path.home() / ".config" / "myapp")


def get_config_path(filename):
    return str(Path(CONFIG_DIR) / filename)


def config_exists(filename):
    return (Path(CONFIG_DIR) / filename).exists()


def get_config_dir():
    return CONFIG_DIR


def ensure_config_dir():
    Path(CONFIG_DIR).mkdir(parents=True, exist_ok=True)
    return CONFIG_DIR


def get_default_config():
    return str(Path(__file__).resolve().parent / "defaults" / "config.json")
