from src.utils.file_reader import validate_json_file, read_json_files
from unittest.mock import patch, mock_open
import os
import pytest

@patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}')
def test_validate_json_file(mock_file):
    result = validate_json_file("test.json")
    assert result["key"] == "value"

@patch("os.listdir")
@patch("src.utils.file_reader.validate_json_file")
def test_read_json_files(mock_validate, mock_listdir):
    mock_listdir.return_value = ["file1.json", "file2.json"]
    mock_validate.return_value = {"key": "value"}
    result = read_json_files("dummy_folder")
    assert len(result) == 2
    assert result[0]["key"] == "value"
