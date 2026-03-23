"""
The file method write expects a string as an argument.
Other types of data must first be converted to strings
before being written to an output file (e.g., using the str function).
"""

import random

f = open("integers.txt", "w") # open file for output
for count in range(500):
    number = random.randint(1, 500) # generate a random integer between 1 and 500
    f.write(str(number) + "\n") # convert integer to string and write to file
f.close() # close the file when done