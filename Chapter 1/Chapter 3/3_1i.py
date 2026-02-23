# when the step argument is a negative number,
# the range function generates a sequence of numbers
# from the first argument down to the second argument
# plus one (because the upper limit is exclusive)

for count in range(10, 0, -1): #we don't want to include 0 # -1 step means counting down each time from 10 to 1
    print(count, end = " ")