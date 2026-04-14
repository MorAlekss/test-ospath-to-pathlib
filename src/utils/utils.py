from pathlib import Path


def make_absolute(path):
    return str(Path(path).resolve())


def get_relative(path, base):
    try:
        return str(Path(path).relative_to(base))
    except ValueError:
        # Fallback for paths not under base (like os.path.relpath)
        import os.path
        return os.path.relpath(path, base)


def join_paths(*parts):
    return str(Path(parts[0]).joinpath(*parts[1:]))


def split_path(path):
    return (str(Path(path).parent), Path(path).name)


def is_absolute(path):
    return Path(path).is_absolute()


def get_stem(filepath):
    return Path(filepath).stem
