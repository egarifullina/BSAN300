#string methods (table 4-2)

s = "Hi there!"
print(s.center(11)) #Center the string in a field of width 11 (the length of the string) - this will not change the string because it is already centered
print(s.count("e")) #Count the number of occurrences of "e" in the string - there are 2 "e"s in the string
print(s.endswith("there!")) #Check if the string ends with "there!" - this will return True because the string does end with "there!"
print(s.startswith("Hi")) #Check if the string starts with "Hi" - this will return True because the string does start with "Hi"
print(s.find("the")) #Find the index of the first occurrence of "the" in the string - this will return 3 because "the" starts at index 3
#find returns the first occurence
print(s.isalpha()) #Check if the string is all alphabetic characters - this will return False because there are spaces and punctuation in the string
print(s.isdigit()) #Check if the string is all digits - this will return False because there are letters and punctuation in the string
print(s.islower()) #Check if the string is all lowercase - this will return False because there are uppercase letters in the string
print(s.isupper()) #Check if the string is all uppercase - this will return False because there are lowercase letters in the string
print(s.lower()) #Convert the string to lowercase - this will return "hi there!" because all the letters will be converted to lowercase
print(s.upper()) #Convert the string to uppercase - this will return "HI THERE!" because all the letters will be converted to uppercase
print(s.replace("Hi", "Hello")) #Replace "Hi" with "Hello" in the string - this will return "Hello there!" because "Hi" will be replaced
print(s.split()) #Split the string into a list of substrings based on whitespace - this will return ["Hi", "there!"] because the string will be split into two substrings based on the space
