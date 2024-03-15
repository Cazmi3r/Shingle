"""Reorder a Mailing to be shingled"""

from pathlib import Path
import pandas as pd

class FileBuffer():
    """gathers files to be processed"""
    def __init__(self, path: Path, is_folder: bool=False):
        """
        will create an array of files to be processed by shingle
        the path will be treated as a file if is_folder is false
        path will be treated as a folder if is_folder is true         
        """
        self.path = path
        self.is_folder = is_folder
        self.buffer = []
        if not is_folder:
            self.add_file()
    def add_file(self):
        """append path as a file to buffer"""
        if self.path.is_file():
            self.buffer.append(self.path)
        else:
            raise ValueError("File not found")

class Shingle:
    """Reorders a Mailing to be shingled"""
    def __init__(self, file_buffer:FileBuffer):
        """
        optionally takes a file to process or a path to process.
        if neither is populated process will fail
        path_mode determines if shingle should prioritize processing a path or a single file
        the buffer holds the files to be shingled
        """

        self.file_buffer = file_buffer
    def process(self):
        """process the files in the buffer"""
        pass
    def load_buffer(self):
        """
        loads the buffer with files to process
        if in path mode
        creates a list from all csn and csv files
        if in file mode
        creates a list of size 1 using the file provided
        """
        pass
    def validate_file(self, file):
        """validate file is a proper value"""
        pass
