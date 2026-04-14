from pathlib import Path


def get_file_path(directory, filename):
    return str(Path(directory) / filename)


def file_exists(filepath):
    return Path(filepath).exists()


def get_file_size(filepath):
    if Path(filepath).exists():
        return Path(filepath).stat().st_size
    return 0


def get_filename(filepath):
    return Path(filepath).name


def get_directory(filepath):
    return str(Path(filepath).parent)


def get_extension(filepath):
    return Path(filepath).suffix


def is_directory(path):
    return Path(path).is_dir()


def list_files(directory):
    if not Path(directory).is_dir():
        return []
    return [str(Path(directory) / p.name) for p in Path(directory).iterdir()]
