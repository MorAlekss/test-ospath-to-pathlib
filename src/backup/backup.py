import os


BACKUP_DIR = os.path.join(os.getcwd(), "backups")


def get_backup_path(filename):
    return os.path.join(BACKUP_DIR, filename)


def backup_exists(filename):
    return os.path.exists(get_backup_path(filename))


def get_backup_dir():
    return BACKUP_DIR


def list_backups():
    if not os.path.isdir(BACKUP_DIR):
        return []
    return os.listdir(BACKUP_DIR)


def get_backup_size(filename):
    path = get_backup_path(filename)
    if os.path.exists(path):
        return os.path.getsize(path)
    return 0
