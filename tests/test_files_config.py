from src.files.files import get_file_path, file_exists, get_filename, get_directory, get_extension, is_directory, get_file_size, list_files
from src.config.config import get_config_path, get_config_dir, get_default_config


def test_get_file_path():
    result = get_file_path("/tmp", "test.txt")
    assert result == "/tmp/test.txt"


def test_file_exists_false():
    assert file_exists("/nonexistent/path/file.txt") == False


def test_get_filename():
    assert get_filename("/tmp/test/file.txt") == "file.txt"


def test_get_directory():
    assert get_directory("/tmp/test/file.txt") == "/tmp/test"


def test_get_extension():
    assert get_extension("file.txt") == ".txt"


def test_get_extension_no_ext():
    assert get_extension("file") == ""


def test_is_directory_false():
    assert is_directory("/nonexistent/path") == False


def test_is_directory_true():
    assert is_directory("/tmp") == True


def test_get_file_size_nonexistent():
    assert get_file_size("/nonexistent/file.txt") == 0


def test_list_files_nonexistent():
    assert list_files("/nonexistent/dir") == []


def test_get_config_path():
    result = get_config_path("settings.json")
    assert result.endswith("settings.json")


def test_get_config_dir():
    result = get_config_dir()
    assert "myapp" in result


def test_get_default_config():
    result = get_default_config()
    assert result.endswith("config.json")
