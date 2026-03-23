"""
A for loop can be used to read one line of a file at a time. 
When you use a for loop to read a file, the loop variable is assigned the value of each line in the file, one at a time. 
The loop continues until there are no more lines to read. 
This is a common way to process files in Python, as it allows you to easily access and manipulate each line of the file.
"""

f = open("mylife.txt", "r") # open file for input
for line in f:
    print(line)
f.close() 