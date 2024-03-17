"""Reorder a Mailing to be shingled"""

from pathlib import Path
import pandas as pd

class FileBuffer():
    #TODO add validation to the buffer. Make sure it's not empty and files are valid
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
        if is_folder:
            self.add_folder(self.path)
        else:
            self.add_file(self.path)
    def add_folder(self, path: Path):
        """append all csv or csn files in a folder to the buffer"""
        if self.validate_folder(path):
            print("folder is valid")
            file_generator = path.glob('*[.]cs[n,v]')
            for file in file_generator:
                file_path = Path(file)
                self.add_file(file_path)
            pass
    def validate_folder(self, path: Path):
        """Validates folder"""
        if not path.is_dir():
            raise ValueError("Folder doesn't exist")
        else:
            return True
    def add_file(self, file: Path):
        """append path as a file to buffer"""
        if self.validate_file(file):
            self.buffer.append(file)
            print(f"Added File: {file}")
        print(f"file {file} was not added")
    def validate_file(self, file: Path):
        """returns true if the file can be processed by shingle"""
        print("entering Validate_file")
        print(f"trying to add file {file} to buffer")
        if not file.is_file():
            raise ValueError("File not found")
        if file.suffix not in [".csv", ".csn",".CSV", ".CSN"]:
            raise ValueError("file extension is wrong")
        return True



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
