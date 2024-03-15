"""test cases for shingle and its file buffer"""

from pathlib import Path
from shingle.shingle import Shingle
from shingle.shingle import FileBuffer as fb

class TestFileBuffer:
    """Tests the functionality of the file buffer"""
    def test_add_file(self):
        """can a file be added to the buffer"""
        path = Path(r"data\test.txt")
        file_buffer = fb(path)
        file_buffer = fb(path)
        with open(file_buffer.buffer[0], encoding="utf-8") as f:
            assert f.read() == "hello I'm test.txt"
