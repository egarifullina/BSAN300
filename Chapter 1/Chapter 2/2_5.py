# Python includes many useful functions, which are organized in libraries of code called modules.
# Functions often require arguments, referred to by names known as parameters.

round(5.25)
# 5.25 is an argument to the round function

input("Prompt: ")
# "Prompt: " is an argument to the input function

print(..., ..., ..., ...)
# The print function can take multiple arguments, separated by commas

# The math module includes functions that perform basic mathematical operations, such as sqrt(), sin(), cos(), and log().
# Before using a function from a module, you must import the module using the import statement.
import math
print(math.sqrt(16))


# If you are going to use only a couple of the module's resources, you can just import the individual resources,
# which saves memory and makes your program run faster.

from math import sqrt, pi
print(sqrt(25))
print(pi)
