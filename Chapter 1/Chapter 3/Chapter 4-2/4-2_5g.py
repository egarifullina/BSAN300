# The next code segment modifies the previous example
# to handle integers separated by spaces and/or newlines

f = open("integers.txt", "r")
theSum = 0
lines = f.read() # read the entire contents of the file
wordlist = lines.split() # split the line into words
print(wordlist)
f.close()

"""
f = open("integers.txt", "r")
theSum = 0
lines = lines
    for word in wordlist:
        number = int(word) # convert the string to an integer
        theSum += number # add the number to the sum
print("The sum of the integers in the file is:", theSum)
f.close()
"""