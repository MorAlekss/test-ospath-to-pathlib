from pathlib import Path


BACKUP_DIR = str(Path.cwd() / "backups")


def get_backup_path(filename):
    return str(Path(BACKUP_DIR) / filename)


def backup_exists(filename):
    return Path(get_backup_path(filename)).exists()


def get_backup_dir():
    return BACKUP_DIR


def list_backups():
    if not Path(BACKUP_DIR).is_dir():
        return []
    return [f.name for f in Path(BACKUP_DIR).iterdir()]


def get_backup_size(filename):
    path = get_backup_path(filename)
    if Path(path).exists():
        return Path(path).stat().st_size
    return 0
