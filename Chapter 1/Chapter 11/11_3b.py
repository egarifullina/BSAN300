#%%
import pandas as pd
import matplotlib.pyplot as plt 

data = {"Course": ["CSCI112", "CSCI312", "PHIL258"],
        "Enrollment": [40, 32, 19]}

frame = pd.DataFrame(data, index = data["Course"])
frame.plot(marker = "o", xlabel = "Course", 
           ylabel = "Enrollment")

# frame.plot(xlabel = "Course", 
#           ylabel = "Enrollment", kind = "bar")
plt.show()

#Processing a data frame often involves accessing individual rows or columns of data.
#Finding the mean, median, and standard deviation of a column of data:
enrollmentCol = frame["Enrollment"]
print("Mean enrollment:", enrollmentCol.mean())
print("Median enrollment:", enrollmentCol.median())
print("Standard deviation enrollment:", enrollmentCol.std())

# %%
