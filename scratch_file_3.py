


def longestCommonPrefix(strs):

    if len(strs) == 0:
        return ""

    prefix = strs[0]

    for current in strs:
        while current.startswith(prefix) == False:

            if prefix == "":
                return prefix

            prefix = prefix[:-1]
    return prefix


def longCommonPrefix(strs):

    prefixCounter = 0

    prefix = strs[0][prefixCounter]

    for word in strs[1:]:
        if strs[0][0: prefixCounter] == word[prefixCounter]:
            prefixCounter += 1

    return strs[0][0: prefixCounter]




x = ["flower","flow","flight"]


print(longCommonPrefix(x))