# file handling -> python -> create , update,delete read
# mode = r, w, a, r+, w+, a+
# delete -> as -> modules import -> delete
# r-> read -> existing file

fs = open("text/hello.txt", mode="r")
# read properties -> read(), readline(), readlines()
# print(fs.read())
print(fs.readline())
print(fs.readlines()) #list of line
fs.close()

# w -> write -> existing file not needed it can create itself

fs1 = open("text/hi.txt", mode="w")
fs1.write("Hello, how are you?")
fs1.close()
# w+ -> read and write -> existing file not needed it can create itself
fs1 = open("text/hi.txt", mode="w+")
fs1.write("Hello, Are you good?")
fs1.seek(0)
one =fs1.read()
print(one)
fs1.close()

# a+ -> append mode
fs3 = open("text/hi.txt", mode="a+")
fs3.write(fs0)

#DELETE  -> REMOVE  -> IMPORT OS
import os
os.remove("text/hi.txt") #delete file

# wap to print the table of a number using file handling
# wap to print the table for 0 to 10 in separate file using file handling