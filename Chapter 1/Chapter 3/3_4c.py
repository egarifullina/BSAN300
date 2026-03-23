#Summation with a while
theSum = 0
count = 1

while count <= 100000:
    theSum += count
    count += 1
 
print(theSum)
 
# Summation with a while loop using while True
theSum = 0
count = 1
 
while True:
    if count > 100000:
        break
    theSum += count
    count += 1
 
print(theSum)