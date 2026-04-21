# Line plots are like scattered plots but connect the dots 
# representing the data at given positions with line segments
# The folowing example plots the values of y = x * 2 and x ** 2, for 1..5, in line plots

#%%
import matplotlib.pyplot as plt 

# Prepare the data

xValues = list(range(1,6))
doubles = list(map(lambda x: x * 2, xValues))
squares = list(map(lambda x: x ** 2, xValues))

# Set up and show the line plots
plt.plot(xValues, doubles, label = "y = x * 2", color = "blue", marker = "o")
plt.plot(xValues, squares, label = "y = x ** 2", color = "red", marker = "o")
plt.xticks(xValues)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()

plt.show()

# %%
