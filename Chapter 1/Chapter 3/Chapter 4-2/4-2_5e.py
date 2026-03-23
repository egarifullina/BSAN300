"""
In cases where you might want to read a specified number of lines
from a file (say, the first line only), 
you can use the readline method of the file object.
"""

f = open("mylife.txt", "r") # open file for input
line = f.readline() # read the first line of the file
print(line) # print the first line of the file
line = f.readline() # read the first line of the file
print(line) # print the first line of the file
f.close() # close the file when done

f = open("mylife.txt", "r") 
while True:
    line = f.readline() # read a line from the file
    if line == "": # reached the end of the file
        break
    print(line) # print the line that was read
f.close()