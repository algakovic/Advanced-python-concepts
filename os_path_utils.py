#!/usr/bin/env python
'''Exploring path utilities with the OS library in Python'''

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


print(os.name)
print("-------------------------------------------------------------")
# check for file existence and type:

print(f'''does 'textfile.txt' exist?: {path.exists("textfile.txt")}''')
print(f"Is 'textfile.txt' a file?: {path.isfile('textfile.txt')}")
print(f"Is 'textfile.txt' a directory?: {path.isdir('textfile.txt')}")
print("-------------------------------------------------------------")
# Use file paths
print(f"Path to 'textfile.txt': {path.realpath('textfile.txt')}")

# Get the modification time:
t = time.ctime(path.getmtime("textfile.txt"))
print(t)

print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))
print("-------------------------------------------------------------")
# Epoch and local times:
print (f"seconds since epoch = {time.time()}")
print (f"Local time: {time.localtime()}")
print (f"UTC time: {time.gmtime()}")

print("-------------------------------------------------------------")
# How long ago was the item modified?
td = datetime.datetime.now() - datetime.datetime.fromtimestamp(
    path.getmtime("textfile.txt")
)
print (f"It has been: {td} since the file was modified")
print (f"Or, {td.total_seconds()} seconds")
