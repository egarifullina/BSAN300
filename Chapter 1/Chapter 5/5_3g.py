# Example: finding the mode of a list of values
# The mode of a list of values is the value that occurs most often in the list
# The following script inputs a list of words from a text of file and prints their mode

fileName = input("Enter the filename: ")
f = open(fileName, "r")

# Input the text, convert its words to uppercase, 
# add the words to a list

upperWords = []

for line in f: # assuming this file has multiple lines (ending with \n)
    words = line.split()
    print(words) # for debugging
    for word in words:
        word = word.upper()
        upperWords.append(word)

# Obtain unique words and frequencies, saving these to a dictionary

theDictionary = {}  
for word in upperWords:
    number = theDictionary.get(word, None) # get the current frequency of this word, or None if it is not in the dictionary
    if number == None: # word entered for the first time # this word is not in the dictionary, so add it with frequency 1
        theDictionary[word] = 1
    else: # word already seen, increment its number # this word is already in the dictionary, so increase its frequency by 1
        theDictionary[word] = number + 1

    print(theDictionary) 


# Find the mode by obtaining max value in dictionary and determining its key

theMaximum = max(theDictionary.values()) # find the maximum frequency
for key in theDictionary: # find the word(s) with this frequency
    if theDictionary[key] == theMaximum:
        print("The mode is", key) # print the mode(s)
        break # if there is more than one mode, this will only print one of them