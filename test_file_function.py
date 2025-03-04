import pytest

from functions import write_and_read_file

@pytest.mark.parametrize("filename, text, expected", [
    ("test_file.txt", "", ""),
    ("test_file.txt", "Hello, pytest!", "Hello, pytest!")
])

def test_input(tmp_path, filename, text, expected):
    file_temp = tmp_path / filename
    assert write_and_read_file(file_temp, text) == expected

def test_incorrect_override(tmp_path):
    file_temp = tmp_path / "test_file.txt"
    write_and_read_file(file_temp, "Hello")
    assert write_and_read_file(file_temp, "Hello2") == "Hello2"