'''
You open a file for input in a manner similar to opening a file for output, 
except that you use "r" instead of "w" as the second argument to the open function. 
When you are done with an input file, you should close it using the close method of the file object.
'''

f = open("mylife.txt", "r") # open file for input
text = f.read()
print(text) # print the contents of the file
f.close() # close the file when done