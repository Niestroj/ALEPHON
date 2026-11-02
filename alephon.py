from os import system
from os import name
from math import sqrt
import random

letterIndex = [
    "A", "B", "C", "D", "E", "F", "G", "H",     # 0 - 7
    "I", "J", "K", "L", "M", "N", "O", "P",     # 8 - 15
    "Q", "R", "S", "T", "U", "V", "W", "X",     # 16 - 23
    "Y", "Z",                                   # 24, 25
    ".", ",", "?", "!", " "                     # 26 - 30
]                                               # In total, 0-30 aka 31 different letters. The numberIndex needs to match the length of this or the program will terminate.
numberIndex = [
    11, 13, 17, 19, 23, 29, 31, 37,
    41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101, 103, 107,
    109, 113,
    127, 131, 137, 139, 149
]                                               # Also 31 entries
# This contains an assortment of unique sequences that should not be able to appear in maths. ill make them long, but this can at some point be the normal value of any part of the string.
# the only way to mitigate this would be to use different characters, which would make the breaks between segments hilariously obvious.
# So i'll take this tradeoff in definitive accuracy for a nicer looking "encryption"
breakCharacterIndex = [
    "0000", "1234", "4321", "2468", "8642",
    "1111", "2222", "3333", "4444", "5555",
    "6666", "7777", "8888", "9999"
]

ErrorState = False
NT_COMMAND = "cls"
UNIX_COMMAND = "clear"
inputMessage = ""
outputMessage = ""

def RunningOnWindows():         # Returns OS, for now this works only on Windows and bash-based shells. If you add other OS' you need to add the corresponding function calls to the system=COMMAND call
    if(name=="nt"): return True
    else: return False

def EncodeMessage():
    ResetInOutMessages()
    global inputMessage
    global outputMessage
    inputMessage = input("ENTER TEXT TO ENCODE:\n")
    inputMessage = inputMessage.upper()
    cryptoMultiplier = 0
    for x in inputMessage:
        indexFound = False
        print("X (LETTER) " + str(cryptoMultiplier) + " is: " + x)
        cryptoMultiplier += 1       # Needs to be set to 1 before first iteration, otherwise the first letter will be unprovable
        for y in range(len(letterIndex)):
            if (x == letterIndex[y]):
                print("Y (NUMBER) is at index " + str(y))
                outputMessage = outputMessage + str(GarbleEncodedCharacter(sqrt(numberIndex[y]) * cryptoMultiplier)) # THIS FUNCTION WILL BE VISUALIZED IN THE README.MD OF THIS PROJECT ON GITHUB.
                outputMessage = outputMessage + AddBreakSequence(outputMessage)
                indexFound = True
            elif (not indexFound and y >= len(letterIndex)-1):  # IF the previous function has already reached its final loop, and the character has no corresponding index, we just dont add it to the final string
                print("LETTER HAS NO INDEX")
    print("\n" +outputMessage + "\n")        # Prints the final composite of encoded characters

def ResetInOutMessages():
    global inputMessage
    global outputMessage
    inputMessage = ""
    outputMessage = ""

def DecodeMessage():
    ResetInOutMessages()
    global inputMessage
    global outputMessage
    inputMessage = input("ENTER TEXT TO DECODE:\n")
    messageSequence = inputMessage

    for x in breakCharacterIndex:
        messageSequence = messageSequence.replace(x, " ")

    messageSequence = messageSequence.split()
    print("FOUND ENCODED CHARACTERS: " + str(messageSequence))
    counter = 0
    for x in messageSequence:
        #print(round((float(x) / counter) ** 2))
        counter += 1
        messageSequence[counter-1] = round((float(x) / counter) ** 2)
    print("HALFSTEP DECODE: " + str(messageSequence) + "\n")
    
    for x in messageSequence:
        counter = 0
        for y in numberIndex:
            if (x == y):
                outputMessage = outputMessage + letterIndex[counter]
            counter += 1
    print("FINAL RESULT COMPLETE:\n")
    print(outputMessage + "\n")
    

def ClearTerminal():
    if (RunningOnWindows()):    system(command=NT_COMMAND)
    else:                       system(command=UNIX_COMMAND)

def GarbleEncodedCharacter(characterFloat):     # Add a random amount of decimal points to the float. Theyre prime numbers, so they all are horribly long without this. This also adds a calculable randomness.
    return format(characterFloat, f".{random.randrange(2, 6)}f")

# CHECK LAST CHARACTER OF STRING, ADD A RANDOM BREAK SEQUENCE FROM THE LIST THAT DOES NOT REPEAT THE LAST NUMBER.
# RETURNS ONLY THE SEQUENCE ITSELF, WHICH IS ADDED TO THE FINAL COMPOSITE STRING in EncodeMessage().
def AddBreakSequence(characterOfMessage):
    sequenceToChoose = None
    while sequenceToChoose == None or sequenceToChoose[0] == characterOfMessage[-1]:
        sequenceToChoose = random.choice(breakCharacterIndex)
    return sequenceToChoose

# If the lists dont add up, encryption is assumed as compromised. Therefore we wont even try to do it.
if (len(letterIndex) != len(numberIndex)): ErrorState = True
else: ErrorState = False

# INITIALISATION COMPLETE.
# PROGRAM LOOP:
while (ErrorState != True):
    print("NEED INPUT - ENCODE OR DECODE TEXT?")
    choice = input("PRESS 1 TO ENCODE. PRESS 2 TO DECODE.\n")

    ClearTerminal()

    if (choice == "1"):           EncodeMessage()
    elif (choice == "2"):         DecodeMessage()

else:
    print("THERE WAS AN ERROR - PROGRAM TERMINATING. CHECK GITHUB FOR FIX.")
