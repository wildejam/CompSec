#!/usr/bin/python3

import sys
from collections import Counter

#taken from Wikipedia
letter_freqs = {
    'A': 0.08167,
    'B': 0.01492,
    'C': 0.02782,
    'D': 0.04253,
    'E': 0.12702,
    'F': 0.02228,
    'G': 0.02015,
    'H': 0.06094,
    'I': 0.06966,
    'J': 0.00153,
    'K': 0.00772,
    'L': 0.04025,
    'M': 0.02406,
    'N': 0.06749,
    'O': 0.07507,
    'P': 0.01929,
    'Q': 0.00095,
    'R': 0.05987,
    'S': 0.06327,
    'T': 0.09056,
    'U': 0.02758,
    'V': 0.00978,
    'W': 0.02361,
    'X': 0.00150,
    'Y': 0.01974,
    'Z': 0.00074
}

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def pop_var(s):
    """Calculate the population variance of letter frequencies in given string."""
    freqs = Counter(s)
    mean = sum(float(v)/len(s) for v in freqs.values())/len(freqs)  
    return sum((float(freqs[c])/len(s)-mean)**2 for c in freqs)/len(freqs)



if __name__ == "__main__":
    # Read ciphertext from stdin
    # Ignore line breaks and spaces, convert to all upper case
    cipher = sys.stdin.read().replace("\n", "").replace(" ", "").upper()
    #################################################################
    # Your code to determine the key and decrypt the ciphertext here

    # variables used to store key length and final key
    cipher = cipher.lower()
    keyLength = 0
    key = ""
    
    # function used to calculate frequencies of letters in vigenere substrings based on keyLength
    # splits inputString into substrings based on key length and records frequencies
    def calcFreqVigenere(inputString, keyLength):
        subStringFreqs = []
        subStringArr = []
        for i in range(0, keyLength):
            subStringArr += [""]
        j = 0
        for char in inputString:
            subStringArr[j] += char
            j = (j + 1) % keyLength

        for subStr in subStringArr:
            freqs = Counter(subStr)
            k = {}
            for i in alphabet.lower():
                if i in list(freqs.keys()):
                    k.update({i: freqs[i] / len(subStr)})
                else:
                    k.update({i: 0})
            subStringFreqs.append(k)

        return subStringFreqs

    # function used to calculate population variance of vigenere substrings.
    # calculates popVar of each substring based on keyLength, and averages them all together.
    def calcPopVarVigenere(inputString, keyLength):
        finalPopVar = 0
        subStringArr = []
        for i in range(0, keyLength):
            subStringArr += [""]
        j = 0
        for char in inputString:
            subStringArr[j] += char
            j = (j + 1) % keyLength

        for subStr in subStringArr:
            finalPopVar += pop_var(subStr)
        finalPopVar /= keyLength
        return finalPopVar
    
    # function used to check the closeness of two sets of letter frequencies
    # works by subtracting each frequency by the respective frequency in the other set,
    # and then adds the results of these subtractions together into one "score" value
    def checkCloseness(dict1Lst, dict2Lst):
        differenceValue = 0
        
        i = 0
        for dict1Value in dict1Lst:
            differenceValue += abs(dict1Value - dict2Lst[i])
            i += 1
        
        return differenceValue
    
    # ----------------------MAIN SCRIPT BEGINS HERE-------------------------------------------------------------

    # Determine key length by choosing the first "high" (> 0.001) population variance amongst key sizes 2-13
    for i in range(2,14):
        popVar = calcPopVarVigenere(cipher, i)
        if popVar > 0.001:
            keyLength = i
            break

    # Calculate frequencies of substrings and store them in an array of dictionaries
    # (each dictionary contains the frequencies for one of the substrings)
    subStrFreqs = calcFreqVigenere(cipher, keyLength)
    
    # Calculate the difference scores between the frequencies in english and each iteration
    # of the frequencies. i.e: keep shifting the frequencies until all 26 shifts are stored,
    # and take the shift with the lowest difference "score". This is our answer for that char of the key.
    for freqDictionary in subStrFreqs:
        differencesList = []
        freqDictList = list(freqDictionary.values())
        alphabetList = list(letter_freqs.values())

        for i in range(0, 26):
            differencesList.append(checkCloseness(freqDictList, alphabetList))
            freqDictList.append(freqDictList.pop(0))

        key += chr(differencesList.index(min(differencesList)) + 65)

    print(key)