# Example: bound-delimited summation
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
theSum = 0

for number in range(lower, upper + 1): # Note: upper + 1 to include upper bound because range excludes the upper limit (it usually goes up to but does not include the upper limit, upp - 1)
    theSum = theSum + number
print(theSum) 

