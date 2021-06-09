


"""
alien language


"""



def alienLanguage(words, order):
    orderMap = {}

    for i, val in enumerate(order):
        orderMap[val] = i

    for i in range(len(words) - 1):

        for j in range(len(words[i])):

            if j >= len(words[i + 1]):
                return False

            if words[i][j] != words[i + 1][j]:
                if orderMap[words[i][j]] > orderMap[words[i + 1][j]]:
                    return False
                break
    return True