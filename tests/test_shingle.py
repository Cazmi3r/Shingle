"""test cases for shingle and its file buffer"""

from pathlib import Path
import pytest
from shingle.shingle import FileBuffer as fb
from shingle.shingle import Shingle

class TestFileBuffer:
    """Tests the functionality of the file buffer"""
    def test_add_file(self):
        """can a file be added to the buffer"""
        path = Path(r"data\test.csv")
        file_buffer = fb(path)
        with open(file_buffer.buffer[0], encoding="utf-8") as f:
            assert f.read() == "hello I'm test.csv"
    def test_add_file_not_found(self):
        """throws value error when file can not be found"""
        path = Path(r"data\testt.csv")
        with pytest.raises(ValueError):
            file_buffer = fb(path)
            assert file_buffer
    def test_add_folder(self):
        """can all files in a folder be added to the buffer"""
        path = Path(r"data\folder")
        file_buffer = fb(path,is_folder=True)
        print(f"file buffer: {file_buffer.buffer}")
        expected_result = ["test_file1.CSN", "test_file2.CSN", "test_file3.CSN"]
        test_case = []
        for file in file_buffer.buffer:
            test_case.append(file.name)
        print(f"expected Result: {expected_result}")
        print(f"test case: {test_case}")
        assert expected_result == test_case
    def test_add_folder_not_found(self):
        """throws value error when folder can not be found"""
        path = Path(r"data\NotAfolder")
        with pytest.raises(ValueError):
            file_buffer = fb(path,is_folder=True)
            assert file_buffer
    def test_pop(self):
        """can we return an object in the buffer"""
        path = Path(r"data\test.csv")
        file_buffer = fb(path)
        assert file_buffer.pop_file() == path

class TestShingle:
    """Tests the functionality of the shingle object"""
    def test_create_shingle(self):
        """can we create a shingle without error"""
        path = Path(r"data\folder\test_file1.CSN")
        shingle = Shingle(path, 3, 3)
        print(shingle)
        assert True
    def test_process_single_file(self):
        """can we create a single file 9up"""
        path = Path(r"data\folder\test_file1.CSN")
        shingle = Shingle(path, 3, 3)
        shingle.process()
        assert False
    
