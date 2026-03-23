#The if-else statement is the most common type of selection statement
# Also called a two-way selection statement because it has two possible paths of execution
import math

area = float(input("Enter the area of the circle: "))

if area > 0:
    radius = math.sqrt(area / math.pi)
    print("The radius of the circle is: ", radius)

else:
    print("Error: the area must be greater than 0.")

