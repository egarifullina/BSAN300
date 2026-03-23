"""
When it is used with strings, the left operand of in is a target
substring and the right operand is a string to be searched. 
It returns True if target string is somewhere in search strings, 
or False othewise. The in operator is case sensitive, so "hi" in "Hi there!" will return False because of the capital H.
"""

fileList = ["myfile.txt", "myprogram.exe", "yourfile.txt"]

for fileName in fileList:
    if ".txt" in fileName: #Check if the file name contains the substring ".txt"
        print(fileName, "is a text file") #If it does, print that it is a text file
    else:
        print(fileName, "is not a text file") #If it does not, print that it is not a text file


for fileName in fileList:
    pass #This is a placeholder for code that will be added later, it does nothing and is used to avoid syntax errors when the code is incomplete\