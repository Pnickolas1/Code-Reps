""""
interweaving strings




"""


def interweavingStrings(one, two, three):
    return isInterweaving(one, two, three, 0, 0)

def isInterweaving(one, two, three, i, j):
    k = i + j
    if k == len(three):
        return True

    if i < len(one) and one[i] == three[k]:
        if isInterweaving(one, two, three, i + 1, j):
            return True

    if j < len(two) and two[j] == three[k]:
        return isInterweaving(one, two, three, i, j + 1)
    return False
