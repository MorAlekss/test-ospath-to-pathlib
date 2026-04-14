import os


REPORTS_DIR = os.path.join(os.getcwd(), "reports")


def get_report_path(name):
    return os.path.join(REPORTS_DIR, f"{name}.pdf")


def report_exists(name):
    return os.path.exists(get_report_path(name))


def get_reports_dir():
    return REPORTS_DIR


def list_reports():
    if not os.path.isdir(REPORTS_DIR):
        return []
    return [
        os.path.splitext(f)[0]
        for f in os.listdir(REPORTS_DIR)
        if os.path.splitext(f)[1] == ".pdf"
    ]


def get_report_size(name):
    path = get_report_path(name)
    if os.path.exists(path):
        return os.path.getsize(path)
    return 0
