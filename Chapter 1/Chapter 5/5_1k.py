# Mutable property of lists leads to interesting phenomena.
# In the code below, first and second are aliases (i.e., they
# refer to the same lists.)

first = [10, 20, 30]
second = first
print(first)   # Output: [10, 20, 30]
print(second)  # Output: [10, 20, 30]
# Modifying the list through one of the aliases modifies the
# list for both aliases.

first[1] = 99
print(first)   # Output: [10, 99, 30]
print(second)  # Output: [10, 99, 30]

# To prevent aliasing, create a new object and copy the contents of the original to it

third = []
for element in first:
    third.append(element)
print(first)   # Output: [10, 99, 30]
print(third)   # Output: [10, 99, 30]

first[1] = 100
print(first)   # Output: [10, 100, 30]
print(third)   # Output: [10, 99, 30]

