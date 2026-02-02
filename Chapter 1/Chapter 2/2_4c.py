# You must use a type conversion function when working with the input of numbers

print(int("33")) 
print(float("33.44")) 
print(float(33))

# Note that the int function converts a float to an int by truncation, not by rounding
print(int(6.75))

# To round a float to the nearest interger, use a round function
print(round(6.75))

# You can also convert numbers to strings using the str function
# Note that Python is a strongly typed programming language (QUIZ!!!)
#It means the interpreter checks the types of values before performing operations on them
profit = 1000.55
print("$", profit)
print("$" + str(profit))

# 2 + "3" would cause an error because you cannot add an interger and a string
# Instead, you can convert the string to an interger
print(2 + int("3"))

