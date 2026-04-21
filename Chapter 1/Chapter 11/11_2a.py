"""
Visualization of data and the patterns contained therein
can take the form of plots, graphs, charts, and animations.
Data visualization generally involves the graphical representation of data in such
a form as to assist in their analysis.
The matplotlib.pyplot module includes resources for creating all the 
visualizations shown in this section.
"""

# Pie charts represent a data set in terms of "slices,"
# each of which shows the relative percentage of an item in a whole circular "pie"
# The following example displays a pie chart of monthly living expenses

# %%
import matplotlib.pyplot as plt

# Prepare the data
expenses = {"Rent": 1200, "Food": 700, "Healthcare": 500, "Transportation": 300
            , "Utilities": 600, "Entertainment": 200}

labels = list(expenses.keys())
slices = list(expenses.values())

# Set up and show the pie chart
plt.pie(slices, labels = labels, autopct = "%1.1f%%")
plt.title("Pie Chart of Living Expenses")
plt.show()
# %%
