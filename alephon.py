verbose = True

from os import system
from os import name
from math import sqrt
import random

logo = [    " ██████░  ██░       ████████░ ████████░ ██░   ██░  ██████░  ███░  ██░        ██░   ██░   ████░    ",
            "██░   ██░ ██░       ██░       ██░   ██░ ██░   ██░ ██░   ██░ ████░ ██░        ██░   ██░  ██░██░    ",
            "████████░ ██░       █████░    ████████░ ████████░ ██░   ██░ ██░██░██░        ███░ ███░ ██░ ██░    ",
            "██░   ██░ ██░       ██░       ██░       ██░   ██░ ██░   ██░ ██ ░████░         ██░ ██░      ██░    ",
            "██░   ██░ ████████░ ████████░ ██░       ██░   ██░  ██████░  ██  ░███░          ████░      ████░   "
        ]
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
breakCharacterIndex = [     # ADD AS MANY AS YOU WANT, MAKE THE DATA POISONED AS FUCK!!!!
    "0000", "1234", "4321", "2468", "8642",
    "1111", "2222", "3333", "4444", "5555",
    "6666", "7777", "8888", "9999", "....",
    "demo", "exit", "hell", "hate", "humans",
    "fuck", "word", "gang", "rand", "SPRK",
    "DPRK", "CPHR", "BREAK", "LONGWORD", "WHATEVER",
    "WOW", "I_SEE", "APPLUM", "BANANUM", "STRAWBERRUM",
    "ATOMIC", "TUNGSTEN", "SECRET", "NINJA", "RICARDONIESTROJ",
    "die", "fuck", "marry", "kill", "cannabis", "THC", "MOLECULES",
    "DATAPOINT", "HATE", "FLESH", "HAATE!"
]
ErrorState = False
NT_COMMAND = "cls"
UNIX_COMMAND = "clear"
inputMessage = ""
outputMessage = ""
verboseMessage = "░▒▓▒░ ALEPHON IS RUNNING IN VERBOSE MODE ░▒▓▒░"
verboseErrorMessage = "!!! ERROR !!!"

def RunningOnWindows():         # Returns OS, for now this works only on Windows and bash-based shells. If you add other OS' you need to add the corresponding function calls to the system=COMMAND call
    if (verbose): 
        print(verboseMessage + " - ALEPHON is running on " + name)
        print(verboseMessage + " - expected: either \"nt\" for locking in windows, or if not nt, ALEPHON automatically uses the UNIX bash shell commands.")
    if(name=="nt"): return True
    else: return False

def EncodeMessage():
    ResetInOutMessages()
    global inputMessage
    global outputMessage
    if (verbose):   print(verboseMessage + " - ENTER TEXT TO ENCODE:")
    inputMessage = input("ENTER TEXT TO ENCODE:\n\n")
    inputMessage = inputMessage.upper()
    cryptoMultiplier = 0
    for x in inputMessage:
        indexFound = False
        cryptoMultiplier += 1       # Needs to be set to 1 before first iteration, otherwise the first letter will be unprovable
        for y in range(len(letterIndex)):
            if (x == letterIndex[y]):
                if (verbose): print(verboseMessage + " - ungarbled numerical code at string index[" + str(cryptoMultiplier-1) + "] is: " + str(numberIndex[y]))
                outputMessage = outputMessage + str(GarbleEncodedCharacter(sqrt(numberIndex[y]) * cryptoMultiplier)) # THIS FUNCTION WILL BE VISUALIZED IN THE README.MD OF THIS PROJECT ON GITHUB.
                if (verbose):   print(verboseMessage + " - garbled numerical code corresponds to: " + str(GarbleEncodedCharacter(sqrt(numberIndex[y]) * cryptoMultiplier)))
                outputMessage = outputMessage + AddBreakSequence(outputMessage)
                indexFound = True
            elif (not indexFound and y >= len(letterIndex)-1):  # IF the previous function has already reached its final loop, and the character has no corresponding index, we just dont add it to the final string
                cryptoMultiplier -= 1
                if (verbose): print(verboseMessage + " - The letter corresponding to string index[" + str(cryptoMultiplier-1) + "] has no corresponding numberIndex. You can add it to both lists if you keep mathematical consistency in mind and their relative indexes the same.\n")
    if (verbose):
        print(verboseMessage + " - TO DISABLE VERBOSE MODE, EDIT LINE 1 OF THIS FILE TO \"verbose=False\"")
        print(verboseMessage + " - finished encoding the string \"" + inputMessage + "\". final output is:\n\n" + outputMessage + "\n")
    else: print("\n" +outputMessage + "\n")        # Prints the final composite of encoded characters

def ResetInOutMessages():
    global inputMessage
    global outputMessage
    inputMessage = ""
    outputMessage = ""

def DecodeMessage():
    ResetInOutMessages()
    global inputMessage
    global outputMessage
    if (verbose):   print(verboseMessage + " - ENTER TEXT TO DECODE:")
    inputMessage = input("ENTER TEXT TO DECODE:\n\n")
    messageSequence = inputMessage

    for x in breakCharacterIndex:
        messageSequence = messageSequence.replace(x, " ")
    if (verbose):   print(verboseMessage + " - reformatted encoded string \"" + inputMessage + "\" to: \"" + str(messageSequence) + "\"")

    messageSequence = messageSequence.split()
    if (verbose):   print(verboseMessage + " - found encoded characters:" + str(messageSequence))
    counter = 0
    for x in messageSequence:
        #print(round((float(x) / counter) ** 2))
        counter += 1
        messageSequence[counter-1] = round((float(x) / counter) ** 2)
    if (verbose):   print(verboseMessage + " - further decoding of randomized square roots equals: \"" + str(messageSequence) + "\"")
    
    for x in messageSequence:
        counter = 0
        for y in numberIndex:
            if (x == y):
                outputMessage = outputMessage + letterIndex[counter]
            counter += 1
    if (verbose):
        print(verboseMessage + " - decoding complete! Note that characters that are not in letterIndex , will simply not appear. If you decide to add them later, remember to add a corresponding number to it in numberIndex too.")
        print(verboseMessage + " - DISPLAYING FINAL DECODER RESULT: \"" + outputMessage + "\"")
    else:
        print("FINAL RESULT COMPLETE:")
    print("\n" + outputMessage + "\n")
        

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
    if (verbose):
        print(verboseMessage + " - pseudorandom function chose: \"" + sequenceToChoose + "\" as a break sequence")
        print(verboseMessage + " - has been encoded into string composite.\n")
    return sequenceToChoose

def DisplayLogo():
    for x in range(0, len(logo)):
        print(logo[x])
    print("\n\n\n")     # Make some space between.

# If the lists dont add up, encryption is assumed as compromised. Therefore we wont even try to run it.
if (len(letterIndex) != len(numberIndex)): ErrorState = True
else: ErrorState = False

if (not verbose): ClearTerminal()
DisplayLogo()                   # INITIALISATION COMPLETE.
RunningOnWindows()

while (ErrorState != True):     # PROGRAM LOOP:
    if (verbose):
        print(verboseMessage + " - ALEPHON NEEDS INPUT - ENCODE OR DECODE TEXT?")
        print(verboseMessage + " - Press 1 to encode a text, or press 2 to decode a text.")
    choice = input("Press 1 to encode a text, or press 2 to decode a text.\n\n")
    if (not verbose):  ClearTerminal()
    if (choice == "1"):           EncodeMessage()
    elif (choice == "2"):         DecodeMessage()
    else:
        if (verbose): print(verboseMessage + " - READ THE PROMPT! REDO!")
    pauseInput = None
    while pauseInput == None:
        pauseInput = input("Press Enter to Continue...")        # Should pause until enter is hit
    if (not verbose):   ClearTerminal()
else:                           # TERMINATE
    print("THERE WAS AN ERROR - PROGRAM TERMINATING. CHECK GITHUB FOR FIX.")
