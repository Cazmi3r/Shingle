"""Runs a shingle job as a script"""

from pathlib import Path
from shingle.shingle import Shingle

def process_file():
    """process one file using cli"""
    print("Welcome to the Process File function")
    while True:
        # collect path to file
        try:
            # confirm path is valid
            pass
        except ValueError:
            pass
            # handle exception if path is not valid
        else:
            # process the file
            break
def process_folder():
    """process all files in a folder cli"""
    print("Welcome to the Process Folder function")
    path = Path(r"C:\BCC\FS\Input")
    shingle = Shingle(path, 4, 4, is_folder=True)
    shingle.process()
