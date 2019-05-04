

"""
the first well known cipher, used by Julius Caeser to order military commands

shifted each letter in his military commands, communicate in advance to agree on a shift to use.

apply the shift to each letter in each message, sent away openly. The cipher was broken after
an arab mathmetician, using a clue left by the language a message is written in. Scan text from any
book count the frequency of the letters used, this is a fingerprint of the language.

its a frequency analysis


tests your understanding of the modulo operator


use unicode values = built in functions take in a character and return that chars unicode value
ord() function

time: O(n)
space: O(n)

"""


def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)



def caeser_cipher(string, key):

    newLetters = []
    newkey = key % 26

    for letter in string:
        newLetters.append(getNewLetter(letter, newkey))
    return "".join(newLetters)



print(caeser_cipher("abcd", 1))







