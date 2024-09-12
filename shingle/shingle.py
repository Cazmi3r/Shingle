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
        if is_folder:
            self.add_folder(self.path)
        else:
            self.add_file(self.path)
        if not self.validate_buffer:
            raise ValueError("Buffer was created with nothing in it")
    def add_folder(self, path: Path):
        """append all csv or csn files in a folder to the buffer"""
        if self._validate_folder(path):
            print("folder is valid")
            file_generator = path.glob('*[.]cs[n,v]')
            for file in file_generator:
                file_path = Path(file)
                self.add_file(file_path)
    def _validate_folder(self, path: Path):
        """Validates folder"""
        if not path.is_dir():
            raise ValueError("Folder doesn't exist")
        else:
            return True
    def add_file(self, file: Path):
        """append path as a file to buffer"""
        if self._validate_file(file):
            self.buffer.append(file)
            print(f"Added File: {file}")
        else:
            print(f"file {file} was not added")
    def _validate_file(self, file: Path):
        """returns true if the file can be processed by shingle"""
        print("entering Validate_file")
        print(f"trying to add file {file} to buffer")
        if not file.is_file():
            raise ValueError("File not found")
        if file.suffix not in [".csv", ".csn",".CSV", ".CSN"]:
            raise ValueError("file extension is wrong")
        return True
    def validate_buffer(self):
        """checks to see if buffer is empty"""
        if len(self.buffer) == 0:
            return False
        return True
    def pop_file(self):
        """returns the last object added to the buffer"""
        if self.validate_buffer():
            return self.buffer.pop()
        return False


class Shingle:
    """Reorders a Mailing to be shingled"""
    def __init__(self, path, ns:int, ew:int, is_folder:bool=False):
        """
        ns = the number of records up and down on a page
        ew = the number of records left and right on a page
        is_folder determains if the program should process a file at the 
        path or all files at the path
        nup is how many records appear on a page
        """
        self.ns = ns
        self.ew = ew
        self.nup = ns *ew
        self.buffer = FileBuffer(path, is_folder)
    def process(self):
        """process the files in the buffer"""
        while not self._is_buffer_empty():
            file = self.buffer.pop_file()
            input_df = pd.read_csv(file)
            rows_in_file = len(input_df)
            # how many records are on the last page
            extra_records = rows_in_file % self.nup
            # how many records need to be added to make the file len divide into Nup 
            records_to_add = self.nup - extra_records
            # add extra records if needed then update rows in files
            if extra_records != 0:
                input_df = self._copy_bottom_record(input_df, records_to_add)
                rows_in_file = len(input_df)
            new_index = self._generate_new_index(rows_in_file)
            output_df = input_df.reindex(new_index)
            output_df.to_csv(str(file)[:-4]+"_Shingle.CSN", index=None)
    def _is_buffer_empty(self):
        """checks to see if there are more files in the buffer"""
        if len(self.buffer.buffer) == 0:
            return True
        return False
    def _generate_new_index(self, size):
        """generates the index for the output"""
        # fill original seq list
        seq_original = []
        for i in range(size):
            seq_original.append(i)
        # Generate number of empty buckets 
        ns_buckets = []
        for i in range(self.ns):
            ns_buckets.append([])
        # How many seq should go in each bucket
        row_len = int(size/self.ew)
        # add seq to each bucket
        for bucket in ns_buckets:
            for i in range(row_len):
                bucket.append(seq_original.pop(0))
        # how many pages are there
        pages = int(row_len/self.ew)
        # create output
        seq_output = []
        for i in range(pages):
            for bucket in ns_buckets:
                for _ in range(self.ew):
                    seq_output.append(bucket.pop(0))
        return seq_output
    def _copy_bottom_record(self, df, repeat):
        """appends bottom record to df repeat num of times"""
        last_record = pd.DataFrame(df[-1:].values, columns = df.columns)
        for _ in range(repeat):
            df = pd.concat([df, last_record])
        df.reset_index(drop=True, inplace=True)
        return df
