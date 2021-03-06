#!/usr/bin/env python
'''Working with filesystem shell methods in Python'''

import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    '''make duplicate of an existing file'''
    if path.exists("textfile.txt"):
        # get path to file in current directory
        src = path.realpath("textfile.txt")

        # Make a backup copy by appending "bak" to the name
        dst = src + ".bak"

        # copy the file:
        '''shutil.copy(src, dst)'''
        # use shutil.copystat() for permissions, modification times and other info

        # Rename the original file
        '''os.rename("textfile.txt", "testfile.txt")'''

    '''Put all contents of directory into a Zip Archive'''
    if path.exists("testfile.txt"):
        src = path.realpath("testfile.txt")
        # use path.split to get directory path
        root_dir, tail = path.split(src)
        shutil.make_archive("archive", "zip", root_dir)

        '''More fine grained control for adding to a zipfile:'''
        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("testfile.txt")
            newzip.write("textfile.txt.bak")

if __name__ == "__main__":
    main()
