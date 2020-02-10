"""
numbers in pi

given 3141592 return the min number of spaces to return
your favorite numbers

[3141, 5, 31, 2, 4159, 9, 42]



"""
pi = '3141592'
numbers = ['3141', '5', '31', '2', '4159', '9', '42']




def getMinSpaces(pi, numbersTable, cache, idx):
    if idx == len(pi):
        return -1
    if idx in cache:
        return cache[idx]
    minSpaces = float('inf')
    for i in range(idx, len(pi)):
        prefix = pi[idx: i + 1]
        if prefix in numbersTable:
            minSpacesInSuffix = getMinSpaces(pi, numbersTable, cache, i + 1)
            minSpaces = min(minSpaces, minSpacesInSuffix + 1)
    cache[idx] = minSpaces
    return cache[idx]

def numbersInPi(pi, numbers):
    numbersTable = {number: True for number in numbers}
    minSpaces = getMinSpaces(pi, numbersTable, {}, 0)
    return -1 if minSpaces == float('inf') else minSpaces


print(numbersInPi(pi, numbers))