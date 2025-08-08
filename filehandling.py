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
fs3.write(fs(0))

#DELETE  -> REMOVE  -> IMPORT OS
import os
os.remove("text/hi.txt") #delete file

# wap to print the table of a number using file handling
# wap to print the table for 0 to 10 in separate file using file handling

# with -> open and close
with open("text/hello.txt", "w+") as fs:
    for i in range (1,11):
        fs.write(f"7*{1} = {7*i}\n")
        fs.seek(0)
    print(fs.read())

# wap to print the table for 0 to 10 in separate file using file handling using with-> open and close
for i in range (1,11):
    with open(f"table/multiply{i}.txt", "w") as fs:   
        for j in range(1,11):
            fs.write(f"{i} * {j} = {j*i}\n")


