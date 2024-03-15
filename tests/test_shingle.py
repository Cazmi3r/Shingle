"""test cases for shingle and its file buffer"""

from pathlib import Path
import pytest
from shingle.shingle import FileBuffer as fb

class TestFileBuffer:
    """Tests the functionality of the file buffer"""
    def test_add_file(self):
        """can a file be added to the buffer"""
        path = Path(r"data\test.csv")
        file_buffer = fb(path)
        file_buffer = fb(path)
        with open(file_buffer.buffer[0], encoding="utf-8") as f:
            assert f.read() == "hello I'm test.csv"
    def test_add_folder(self):
        """can all files in a folder be added to the buffer"""
        path = Path(r"data\folder")
        file_buffer = fb(path,is_folder=True)
        assert file_buffer.validate_folder(path)
    def test_add_folder_not_found(self):
        """can all files in a folder be added to the buffer"""
        path = Path(r"data\NotAfolder")
        with pytest.raises(ValueError):
            file_buffer = fb(path,is_folder=True)
            assert file_buffer
