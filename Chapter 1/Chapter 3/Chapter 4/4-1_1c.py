#The subscript operator is also useful in loops where you want to
#use the position as well as the characters in a string

data = "Hi there!"

for index in range(len(data)): #Loop through the indices of the string
    print(index, data[index]) #Print the index and the character at that index  


