import os
from pathlib import Path


def make_absolute(path):
    return str(Path(path).resolve())


def get_relative(path, base):
    return os.path.relpath(path, base)


def join_paths(*parts):
    return str(Path(parts[0]).joinpath(*parts[1:]))


def split_path(path):
    p = Path(path)
    return (str(p.parent), p.name)


def is_absolute(path):
    return Path(path).is_absolute()


def get_stem(filepath):
    return Path(filepath).stem
