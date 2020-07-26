

""""
Knuth Morris Pratt Algorithm

KNP - string matching, does 1 string live inside anther string


- commonly used in DNA sequencing
- takes advantage of patterns within strings



 -- Notes* in the build pattern phase, is the prefix == suffix ?

"""


def buildPattern(substring):
    pattern = [-1 for x in substring]
    j = 0
    i = 1
    while i < len(substring):
        if substring[i] == substring[j]:
            pattern[i] = j
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else:
            i += 1
    return pattern

def doesMatch(string, substring, pattern):
    i = 0
    j = 0
    while i + len(substring) - j <= len(string):
        if string[i] == substring[j]:
            if j == len(substring) - 1:
                return True
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else:
            i += 1
    return False

def knuthMorrisPrattAlgorithm(string, substring):
    pattern = buildPattern(substring)
    return doesMatch(string, substring, pattern)
