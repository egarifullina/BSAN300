"""
Bar charts visually represent a data set in terms of rectangular shapes or bars.
The following example displays a bar for each enrollment value in a two-dimensional grid.
"""
# %%
import matplotlib.pyplot as plt

# Prepare the data
data = {"CSCI112": 40, "CSCI1312": 32, "PHIL258": 19}

courses = list(data.keys())
enrollments = list(data.values())

# Set up and show the horizontal bar chart
plt.figure(figsize = (4, 4))
plt.bar(courses, enrollments, width = 0.2) 
plt.title("Students Enrolled in Ken's courses")
plt.xlabel("Course")
plt.ylabel("Number of Students")
plt.show()

# %%
