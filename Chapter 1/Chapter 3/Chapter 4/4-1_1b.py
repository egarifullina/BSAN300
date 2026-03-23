#The subscript operator, [], allows access to a single character in a string
# at a given position

name = "Alan Turing"
print(name[0]) #Examine the first character#0 because the first character is at index 0
print(name[1]) #1 because the second character is at index 1

print(name[5]) #5 because the sixth character is at index 5
#print(name[len(name)]) #An index error #len(name) is 11, but the last character is at index 10, so this will cause an error
print(name[len(name)-1]) #Examine the last character #len(name) is 11, so len(name)-1 is 10, which is the index of the last character   
print(name[-1]) #Examine the last character using negative indexing #-1 is the index of the last character, -2 is the index of the second to last character, and so on
print(name[-2]) #Examine the second to last character using negative indexing

#the string is an immutable data structure
# - the characters can be accessed but not changed, replaced, inserted, or removed

#name[0] = "B" #This will cause an error because strings are immutable and cannot be changed

