# the random module supports several ways to generate random numbers

import random

for roll in range(10):
    print(random.randint(1, 6), end = " ") # simulates rolling a six-sided die # generates a random integer between 1 and 6 (inclusive)
 #end because we want to print all the rolls on the same line
 







# random.random() generates a random float between 0.0 and 1.0
print(random.random())

# random.randint(a, b) generates a random integer between a and b (inclusive)
print(random.randint(1, 10))
