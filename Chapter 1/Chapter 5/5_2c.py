# Our next example function computes the average value in a list of numbers

def average(lyst):
    theSum = 0
    for number in lyst:
        theSum = theSum + number # or theSum += number
    return theSum / len(lyst) # the average is the sum divided by the number of items in the list
print(average([1, 3, 5, 7])) 