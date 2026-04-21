# Scatter plots visually represent a data set as a collection of points or dots in a two-dimensional grid
# The following example shows a scatter plot of the unique numbers from 1 through 100, scattered at random positions

# %% 
import matplotlib.pyplot as plt
import stats

# Prepare the data
positions = list(range(1, 101))
numbers = stats.getRandomList(100, 1, 100, unique = True)

# Set up and show the scatter plot
plt.scatter(positions, numbers, color = "purple", marker = ".")
plt.title("Scatter Plot of Unique Random Numbers from 1...100")
plt.xlabel("Position")
plt.ylabel("Random Number")
plt.show()
# %%
