


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
                # if orderMap[words[i][j]] is in order, or properly lexiographically relative i + 1, then just
                # break and move on to the next one, there is no sense in continuing to evaluate
                # i , vs i + 1
                break
    return True