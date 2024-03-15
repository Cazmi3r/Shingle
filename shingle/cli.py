"""Runs a shingle job as a script"""

from pathlib import Path
from shingle.shingle import Shingle
from shingle.shingle import FileBuffer as fb

def process_file():
    """process one file using cli"""
    print("Welcome to the Process File function")
    while True:
        path = Path(input("Input path: "))
        try:
            file_buffer = fb(path)
        except ValueError:
            print(path)
            print("Not a valid file try again")
        else:
            file_buffer = fb(path)
            with open(file_buffer.buffer[0], encoding="utf-8") as f:
                print(f.read())
            break
def process_folder():
    """process all files in a folder cli"""
    print("Welcome to the Process Folder function")
