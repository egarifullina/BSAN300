# A tuple resembles a list, but is immutable (i.e., it cannot be changed after it is created).
# You indicate a tuple by enclosing its elements in () instead of [].

fruits = ("apple", "banana", "cherry")
print(fruits)  # Output: ('apple', 'banana', 'cherry')
meats = ("beef", "pork", "chicken")
print(meats)   # Output: ('beef', 'pork', 'chicken
# You can access the elements of a tuple using indexing, just like a list.

food = meats + fruits 
print(food)

# A tuple is created by placing a sequence of values separated by commas inside parentheses.
# Tuples are often used to represent records with multiple fields, such as a person's name and age.

veggies = ["carrot", "broccoli", "spinach"]
print(tuple(veggies))  # Output: ('carrot', 'broccoli', 'spinach')