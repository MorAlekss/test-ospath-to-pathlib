import os


def make_absolute(path):
    return os.path.abspath(path)


def get_relative(path, base):
    return os.path.relpath(path, base)


def join_paths(*parts):
    return os.path.join(*parts)


def split_path(path):
    return os.path.split(path)


def is_absolute(path):
    return os.path.isabs(path)


def get_stem(filepath):
    return os.path.splitext(os.path.basename(filepath))[0]
