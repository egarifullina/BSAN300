"""
Researchers who do quantitative analysis are often interested
in the median of a set of numbers. 
The median is the number in the middle when the numbers are sorted. 
If there is an even number of numbers, the median is the average of the two middle numbers. 
For example, the median of 1, 2, 3, 4, 5 is 3, and the median of 1, 2, 3, 4 is (2 + 3) / 2 = 2.5
Median - the value that is less than half the numbers
in a set and greater than the other half.
"""

fileName = input("Enter a filename: ")
f = open(fileName, "r")

# Input the text, convert to numbers, and add the numbers to a list
numbers = []
for line in f:
    words = line.split()
    for word in words:
        numbers.append(float(word))
numbers.sort()
midpoint = len(numbers) // 2
print("The median is", end = " ")
if len(numbers) % 2 == 1: # if the number of elements is odd
    print(numbers[midpoint])
else: # if the number of elements is even
    print((numbers[midpoint] + numbers[midpoint - 1]) / 2) 
