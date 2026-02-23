print(range(4))
print(list(range(4))) # range returns a list (sequence of numbers)

print(list(range(1, 5))) # specify start and end (end is exclusive)

# You can use for loops to visit each value in a list
for number in [6, 4, 8]:
    print(number, end = " ")

# Strings are also sequences of characters
# in which values can be visited with a foor loop
for character in "Hi there!": 
    print(character, end = " ")

      