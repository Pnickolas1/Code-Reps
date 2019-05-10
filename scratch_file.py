from random import randint
random_numbers = [24, 40, 23, 98, 44, 19, 8, 31, 31, 8, 38, 0, 35, 50, 3,
                   45, 44, 41, 5, 16, 29, 25, 25, 32, 25, 20, 34, 36, 3, 19]

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

randoms = [5, 1, 10, 4, 25, 3, 16, 9]

"""

space: O(n)
time: O(n)

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393,
196418, 317811,
"""


def getNewLetterCode(letter, newKey):
    newLetterCode = ord(letter) + newKey
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)




def caeser_ciper(string, key):

    newKey = key % 26
    newLetter = []

    for letter in string:
        newLetter.append(getNewLetterCode(letter, newKey))
    return "".join(newLetter)




print(caeser_ciper("abcd", 1))
