from hashlib import md5

incrementor = 0                 # incrementor to change plaintext
plaintext = str(incrementor)    # Plaintext to encode
hashFound = False               # Boolean keeps track of if hash has been found
targetString = "'='"          # String to search for within the resulting hash

targetStringHex = targetString.encode().hex() # Convert target string to hex

while not hashFound:
    hashStringHex = md5(plaintext.encode()).hexdigest()

    if hashStringHex.find(targetStringHex) % 2 == 0:
        print("STRING HASH FOUND!")
        print("PLAINTEXT: " + plaintext)
        print("HASH (Hex): " + hashStringHex)
        hashFound = True

    incrementor += 1
    plaintext = str(incrementor)
