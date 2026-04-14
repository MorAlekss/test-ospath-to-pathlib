from src.reports.reports import get_report_path, report_exists, get_reports_dir, list_reports, get_report_size
from src.utils.utils import make_absolute, join_paths, split_path, is_absolute, get_stem
from src.backup.backup import get_backup_path, backup_exists, get_backup_dir, list_backups, get_backup_size


def test_get_report_path():
    result = get_report_path("monthly")
    assert result.endswith("monthly.pdf")


def test_report_exists_false():
    assert report_exists("nonexistent") == False


def test_list_reports_empty():
    assert isinstance(list_reports(), list)


def test_get_report_size_nonexistent():
    assert get_report_size("nonexistent") == 0


def test_make_absolute():
    result = make_absolute(".")
    assert result.startswith("/")


def test_join_paths():
    result = join_paths("/tmp", "test", "file.txt")
    assert result == "/tmp/test/file.txt"


def test_split_path():
    head, tail = split_path("/tmp/test/file.txt")
    assert head == "/tmp/test"
    assert tail == "file.txt"


def test_is_absolute_true():
    assert is_absolute("/tmp/file.txt") == True


def test_is_absolute_false():
    assert is_absolute("relative/path") == False


def test_get_stem():
    assert get_stem("/tmp/test/file.txt") == "file"


def test_get_backup_path():
    result = get_backup_path("backup.tar.gz")
    assert result.endswith("backup.tar.gz")


def test_backup_exists_false():
    assert backup_exists("nonexistent.tar.gz") == False


def test_list_backups_empty():
    assert isinstance(list_backups(), list)


def test_get_backup_size_nonexistent():
    assert get_backup_size("nonexistent.tar.gz") == 0
