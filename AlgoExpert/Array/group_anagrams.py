

"""
Group Anagrams

write a function that takes in an array of strings and groups them

sample Input: ['yo', 'act', 'flop', 'tac', 'cat', 'oy', 'olfp']

"""



def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
    return list(anagrams.values())


