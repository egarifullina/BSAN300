#Alternative: Use a Boolean variable to control the loop

done = False
while not done: #equivalent to done != False
    number = int(input("Enter the numeric grade: "))
    
    if number >= 0 and number <= 100:
        done = True
    else:
        print("Invalid grade. Please enter a number between 0 and 100.")



if number > 89:
    letter = "A"
elif number > 79:
    letter = "B"
elif number > 69:
    letter = "C"
elif number > 59:
    letter = "D"
else:
    letter = "F"

print("The letter grade is", letter)