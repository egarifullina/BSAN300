# data can be output to a text file using a file object

f = open("mylife.txt", "w") # open file for output #open a file for writing (if the file does not exist, it will be created; if it does exist, it will be overwritten)
f.write("First line.\nSecond line.\n") # write two lines of text
f.close() # close the file when done
