import re

"""
what did I learn? 

- hashmap the counter
- regex in python re.sub(chars, replaceWith, string)
-  utilize the index within a string [[1], [2 ], [3]]
    - 


"""
document = "Practice makes perfect, you'll get perfecT by practice. just practice! just just just!!"

def word_count_engine(document):
    wordBank = {}
    words = document.split(' ')
    largestCount = 0

    # O(n) time , O(n) space
    for word_raw in words:
        # strip out non numeric chars
        word = re.sub(r'[^\w]', '', word_raw)
        if word.lower() in wordBank:
            wordBank[word.lower()] += 1
        else:
            wordBank[word.lower()] = 1

        if wordBank[word.lower()] > largestCount:
            largestCount = wordBank[word.lower()]

    wordMap = [[] for x in range(largestCount)]

    for key, val in wordBank.items():
        wordMap[val - 1].append(key)

    finalwords = []
    for i in range(largestCount - 1, -1, -1):
        for word in wordMap[i]:
            finalwords.append([f"{word}", f"{i + 1}"])

    return finalwords

test = word_count_engine(document)
Expected = [["just","4"],["practice","3"],["perfect","2"],["makes","1"],["youll","1"],["get","1"],["by","1"]]

print(test == Expected)

"""
Input:
{'practice': 3, 'makes': 1, 'perfect': 2, 'youll': 1, 'get': 1, 'by': 1, 'just': 4}

Expected = [["just","4"],["practice","3"],["perfect","2"],["makes","1"],["youll","1"],["get","1"],["by","1"]]
Actual:   [['just', '4'], ['practice', '3'], ['perfect', '2'], ['get', '1'], ['makes', '1'], ['youll', '1'], ['by', '1']]


actual = [['just', '4'], ['practice', '3'], ['perfect', '2'], ['makes', '1'], ['youll', '1'], ['get', '1'], ['by', '1']]

"""


