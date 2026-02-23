# Count-controlled loops - loops that count through a range of numbers
product = 1
for count in range(4):
    product = product * (count + 1) # Multiply by count + 1 because count starts at 0
    print(product)

