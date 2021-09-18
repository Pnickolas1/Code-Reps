

"""
loss less data compression algo




"""



def runLengthEncoding(string):

    encodedCharacters = []
    currentRunLength = 1

    for i in range(1, len(string)):
        currentCharacter = string[i]
        previousCharacter = string[i - 1]

        if currentCharacter != previousCharacter or currentRunLength == 9:
            encodedCharacters.append(str(currentRunLength))
            encodedCharacters.append(previousCharacter)
            currentRunLength = 0
        currentRunLength += 1

        # handle the last value
    encodedCharacters.append(str(currentRunLength))
    encodedCharacters.append(string[len(string) -1])
    return "".join(encodedCharacters)

print(runLengthEncoding('aaaaabbcccccc'))