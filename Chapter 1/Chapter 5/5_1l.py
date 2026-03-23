# Object identity - if two variables refer to the exact same object in memory.
# Python's is operator can be used to test for object identity.

first = [20, 30, 40]
second = first
third = list(first)

print(first == second)  # object identity (Output: True)
print(first == third)   # structural equivalence (Output: True) #testing if these are the same object in memory, not if they are structurally equivalent

print(first is second)  # Output: True
print(first is third)   # Output: False
