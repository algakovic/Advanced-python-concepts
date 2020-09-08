#!/usr/bin/env python
'''Working with filesystem shell methods in Python'''

import os
from os import path
import shutil
from shutil import make_archive
def main():
    # make duplicate of an existing file
    if path.exists("textfile.txt"):
        # get path to file in current directory
        src = path.realpath("textfile.txt")

        # Make a backup copy by appending "bak" to the name
        dst = src + ".bak"

        # copy the file:
        # shutil.copy(src, dst)
        # use shutil.copystat() for permissions, modification times and other info

        # Rename the original file
        # os.rename("textfile.txt", "testfile.txt")

        '''Put things into a Zip Archive''' 
        # use path.split to get directory path

        root_dir, tail = path.split(src)
        shutil.make_archive("my_archive", "zip", root_dir)

if __name__ == "__main__":
    main()
