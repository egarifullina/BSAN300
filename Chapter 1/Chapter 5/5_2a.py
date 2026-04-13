"""
Defining our own functions allows us to organize our code
in existing scripts more effectively.
Definition of a function consists of a header and a body.
"""

def square(x):
    print(x * x)

square(4) # Output: 16


"""
Place a return statement at each exit point of a function 
when the function should explicitly return a value
"""

number = round(4.6424, 2)
print(number)

number = input("Enter a number: ")
print(number)

def square(x):
    return x * x    

number = square(5)
print("Number =", number)


def square(x):
    return x * x    

print(square(5))

