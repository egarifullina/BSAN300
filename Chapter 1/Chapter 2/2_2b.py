# You can join two or more strings ti form a new
# string using the concatenation operator.

print("Hi " + "there, " + "Ken!")
print("Hi", "there,", "Ken!")

cost = 10.00
print("$", cost) 
print("$ " + cost) #This will cause an error
print("$ " + str(cost)) 

# The * operator allows you to build a string by
# repeating another string a given number of times.
print("Ha" * 5) 
print(" " * 10 + "Python") 