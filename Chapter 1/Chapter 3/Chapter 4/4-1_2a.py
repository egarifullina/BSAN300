'''
Ceaser cipher replaces each character in plain text 
with a character in a given distance away
The ord function returns the ordinal position in the ASCII sequence.
The chr is the inverse function.
'''

plainText = input("Enter a one-word, lowercase message: ")
distance = int(input("Enter a distance value: "))
code = ""

for ch in plainText:
    ordValue = ord(ch) #Get the ordinal value of the character
    cipherValue = ordValue + distance #Calculate the new ordinal value by adding the distance
    if cipherValue > ord("z"): #if value is after z, move back to a
        cipherValue = ord("a") + distance - (ord('z') - ordValue +1) #Wrap around to the beginning of the alphabet if the new ordinal value exceeds 'z'
    code = code + chr(cipherValue) #Convert the new ordinal value back to a character and add it to the code string

print(code) #Print the encrypted message
    