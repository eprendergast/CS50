from cs50 import get_string
import sys

key = int(sys.argv[1]) #store key from user input

plain_text = get_string("Please enter text to encipher: ") #prompt user for a string

print("ciphertext: ", end="")
for c in plain_text:
    if c.isalpha() == True:
        if c.isupper() == True:
            d = chr(((ord(c)-65 + key) % 26) + 65)
            print(d, end="")
        if c.islower() == True:
            d = chr(((ord(c)-97 + key) % 26) + 97)
            print(d, end="")
    elif c.isalpha() == False:
        print(c, end="")
    else:
        print("ERROR")
print()