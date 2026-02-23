# Loop to compute exponentiation for a non-negative exponent
number = 2
exponent = 3
product = 1 # Initialize product to 1 because it's the multiplicative identity

for eachPass in range(exponent):
    product = product * number
    print(product, end = " ")

print(product, end = " ");