#!/usr/bin/env python
'''Working with files in python'''

def main():
    ''' open a file for writing and create it if it doesnt exist:'''
    # python already knows abotu files no import necessary
    # open textfile.txt with write access and '+' means to create file if does not exist also store as f object:

    f = open("testfile.txt", "w+")

    # write some lines of data to the file:
    for i in range(10):
        f.write(f"This is line {i} \r\n")



if __name__ == "__main__":
    main()
