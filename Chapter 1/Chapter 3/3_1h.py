# Range expects a third argument that allows you to specify a step value 
print(list(range(1, 6, 1)))    # same as using two arguments 
print(list(range(1, 6, 2))) # use every other number
print(list(range(1, 6, 3))) # use every third number

# Example: sum of even numbers from 2 to 10
# using a step value of 2
theSum = 0
for count in range(2, 11, 2):
    theSum += count
    print(theSum)