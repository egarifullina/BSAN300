# The while loop can be complicated to write correctly
# It is possible to simplify its structure and improve its readability.

theSum = 0

while True: 
    data = input("Enter a number or just enter to quit: ")
    if data == "":   # Termination condition
        break
    number = float(data)
    theSum += number
print("The sum is", theSum)

# In this version, the loop is defined as an infinite loop using while True.
# The termination condition is tested inside the loop.
# When the condition is met, the break statement is executed,
# which immediately terminates the loop.