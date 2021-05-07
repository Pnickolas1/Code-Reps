


"""
reverse a string


"""


def reverseList(words):
    left = 0
    right = len(words) -1

    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
    return words

def reverseWordsInString(string):

    words = []
    currentIdx = 0

    for i in range(len(string)):
        char = string[i]

        if char == " ":
            words.append(string[currentIdx: i])
            currentIdx = i
        elif string[currentIdx] == " ":
            words.append(string[currentIdx])
            currentIdx = i

    words.append(string[currentIdx:])
    reverseList(words)
    return "".join(words)