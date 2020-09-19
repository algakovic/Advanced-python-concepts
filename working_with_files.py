#!/usr/bin/env python
'''Working with files in python'''

def main():
    ''' open a file for writing and create it if it doesnt exist:'''
    # python already knows about files no import necessary
    # open textfile.txt with write access 'w' and '+' means to create file if does not exist also store as f object:

    f = open("testfile.txt", "r")

    # write some lines of data to the file:
    '''for i in range(10):
        f.write(f"This is line {i} \r\n")'''

    # Read the file contents:
    # use "r" e.g. open(somefile, 'r')
    # can also use:
    if f.mode == 'r':
        contents = f.read()
        print(contents)

    # or use readlines() to read specific lines:
    '''if f.mode == 'r':
        fl = f.readlines()
        for x in fl:
            print(x)'''

    # use 'a' parameter to append to end of file instead of writing over the existing info:
    # E.g: f = open ("testfile.txt", "a")

    # f.close()

if __name__ == "__main__":
    main()
