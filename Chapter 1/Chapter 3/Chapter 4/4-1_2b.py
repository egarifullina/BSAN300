#To decrypt

code = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))
plainText = ""

for ch in code:
    ordValue = ord(ch) #Get the ordinal value of the character
    cipherValue = ordValue - distance #Calculate the new ordinal value by subtracting the distance
    if cipherValue < ord("a"): #if value is before a, move back to z
        cipherValue = ord("z") - (distance - (ordValue - ord("a") +1)) #Wrap around to the end of the alphabet if the new ordinal value is less than 'a'
    plainText = plainText + chr(cipherValue) #Convert the new ordinal value back to a character and add it to the plainText string

    #bitstring = binary
    