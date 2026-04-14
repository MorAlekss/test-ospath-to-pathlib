import os


def get_file_path(directory, filename):
    return os.path.join(directory, filename)


def file_exists(filepath):
    return os.path.exists(filepath)


def get_file_size(filepath):
    if os.path.exists(filepath):
        return os.path.getsize(filepath)
    return 0


def get_filename(filepath):
    return os.path.basename(filepath)


def get_directory(filepath):
    return os.path.dirname(filepath)


def get_extension(filepath):
    return os.path.splitext(filepath)[1]


def is_directory(path):
    return os.path.isdir(path)


def list_files(directory):
    if not os.path.isdir(directory):
        return []
    return [os.path.join(directory, f) for f in os.listdir(directory)]
