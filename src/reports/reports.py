from pathlib import Path


REPORTS_DIR = str(Path.cwd() / "reports")


def get_report_path(name):
    return str(Path(REPORTS_DIR) / f"{name}.pdf")


def report_exists(name):
    return Path(get_report_path(name)).exists()


def get_reports_dir():
    return REPORTS_DIR


def list_reports():
    reports_dir = Path(REPORTS_DIR)
    if not reports_dir.is_dir():
        return []
    return [
        p.stem
        for p in reports_dir.iterdir()
        if p.suffix == ".pdf"
    ]


def get_report_size(name):
    path = Path(get_report_path(name))
    if path.exists():
        return path.stat().st_size
    return 0
