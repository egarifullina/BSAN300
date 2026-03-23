#Substring
#Pythin subscript operatot can be used to obtain a substring
#through a process called slicing by placing a colon (:) in the subscript
name = "Hello World"

print(name[0:]) #Prints "Hello World" - the substring from index 0 to the end of the string

print(name[0:1])
#Prints "H" - the substring from index 0 to 0 (1 is not included)

print(name[0:2])
#Prints "He" - the substring from index 0 to 1 (2 is not included)  

print(name[:len(name)]) #Prints "Hello World" - the substring from the beginning of the string to the end of the string (len(name) is 11, so this is the substring from index 0 to 10)

print(name[0:5]) #Prints "Hello" - the substring from index 0 to 4 (5 is not included)
print(name[6:11]) #Prints "World" - the substring from index 6 to 10 (11 is not included)
print(name[6:]) #Prints "World" - the substring from index 6 to the end of the string
print(name[:5]) #Prints "Hello" - the substring from the beginning of the string to index 4 (5 is not included)

print(name[-3:]) #Prints "rld" - the substring from index -3 to the end of the string
print(name[:-3]) #Prints "Hello Wo" - the substring from the beginning of the string to index -4 (the last 3 characters are not included)


