"""
Many real-world data sets are complex, structured as two-dimensional tables with multiple rows and columns.
These structured data can be saved in a special type of text file in CSV format for export
to other analysis programs. Python's pandas library can be used to load data sets from CSV 
files and clean them before performing analyses and visualization.
"""

# In pandas, a data set is represented as a data frame
# which consists of a set of columns and rows and includes
# many operations that support data analysis.

import pandas as pd

data = {"Course": ["CSCI112", "CSCI312", "PHIL258"],
        "Enrollment": [40, 32, 19]}

frame = pd.DataFrame(data)
print(frame)

