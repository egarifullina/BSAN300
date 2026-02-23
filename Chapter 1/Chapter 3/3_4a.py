"""
The foor loop executes a set of statements a definite number of times. 
However, in many situations, the number of iterations a loop is unpredictable.
In such cases, a while loop is more appropriate.
The while loop can be used to describe conditional iteration, meaning the
process continues to repeat as long as a condition remains true.
"""

# For example, a program's input loop can accept values until 
# the user enters a sentinel that terminates the input.

theSum = 0.0
data = input("Enter anumber or just enter to quit: ")
while data != "":         # while the user has not pressed the enter key
    number = float(data)
    theSum += number      # add number to theSum (augmented operation) # theSum = theSum + number
    data = input("Enter anumber or just enter to quit: ")

print("The sum is", theSum)