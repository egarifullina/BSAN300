"""
Many data processing applications require output
that has a tabular format. The print function automatically
begins printing an output datum in the first available column.
"""

for exponent in range(7,11):
    print(exponent, 10 ** exponent)

"""
Python includes a general formatting mechanism that allows
the programmer to specify field widths for different
types of data.
< format string > % < datum >
"""

print("%6s" % "four") # 6 is the field width, s means string
# Right justify in 6 columns

print("%-6s" % "four") 
# Left justify in 6 columns

# to format intergers, the letter d is used instead of s
print("%6d" % 42) # right justify in 6 columns
print("%-6d" % 42) # left justify in 6 columns

for exponent in range(7, 11):
    print("%-3d%12d" % ((exponent, 10 ** exponent)))

# To format a data value of type float:
# %<field.width>.<precision>f
salary = 100.00
print("Your salary is $%0.2f" % salary) # 2 digits after the decimal point

