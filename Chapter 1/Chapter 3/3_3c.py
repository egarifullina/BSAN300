# Print the max and min of two input numbers

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

if first > second:
    maximum = first
    minimum = second

else:
    maximum = second
    minimum = first

print("The maximum is", maximum)
print("The minimum is", minimum)


# Note: Python includes two built-in functions, max and min
# that can make the if-then statement above unnecessary
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

print("Maximum: ", max(first, second))
print("Minimum: ", min(first, second))



# Multi-way selection statement - can check if they are equal

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

if first > second:
    maximum = first
    minimum = second
    print("The maximum is", maximum)
    print("The minimum is", minimum)

elif second > first:
    maximum = second
    minimum = first
    print("The maximum is", maximum)
    print("The minimum is", minimum)

else:
    print("The numbers are equal.")
