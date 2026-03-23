"""
String representation of integrers and floating-point numbers 
can be converted to the numbers by using the functions int and float, respectively. 
The functions int and float can also be used to convert numbers to a different type (e.g., converting a floating-point number to an integer).
"""

f = open("integers.txt", "r") # open file for input
theSum = 0
for line in f:
    line = line.strip() # remove any leading/trailing whitespace characters (including newline) from the line
    number = int(line) # convert the string to an integer
    theSum += number # add the number to the sum
print("The sum of the integers in the file is:", theSum)
f.close() # close the file when done