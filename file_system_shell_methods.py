#!/usr/bin/env python
'''Working with filesystem shell methods in Python'''

import os
from os import path
import shutil

def main():
    # make duplicate of an existing file
    if path.exists("textfile.txt"):
        # get path to file in current directory
        src = path.realpath("textfile.txt")

        # Make a backup copy by appending "bak" to the name
        dst = src + ".bak"

        # 

if __name__ == "__main__":
    main()