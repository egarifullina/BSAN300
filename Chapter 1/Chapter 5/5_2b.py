# A Boolean function usually tests its argument for the presence of absence of some property. 
# For example, the built-in function `isinstance` tests whether its first argument is an instance 
# of the class specified by its second argument. 
# The function `isinstance` is a Boolean function because it returns either `True` or `False`.

def odd(x):
    if x % 2 == 1: # x has a remainder of 1 (odd)
        return True
    else:
        return False
    
print(odd(5)) #True
print(odd(6)) # False # The function `odd` returns `True` when the argument is an odd number and `False` when the argument is an even number.
# The function `odd` is a Boolean function because it returns either `True` or `False`.
# We can test the function `odd` by calling it with different arguments and printing the results
