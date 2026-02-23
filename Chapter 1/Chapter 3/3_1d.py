# Count-controlled loops - loops that count through a range of numbers
product = 1
for count in range(4):
    product = product * (count + 1) # Multiply by count + 1 because count starts at 0

print(product)

# To specify an explicit lower bound, use two-argument form of range
product = 1
for count in range(1, 5):  # Loop from 1 to 4 (go through it 4 times but count starts at 1)
    product = product * count
print(product)  