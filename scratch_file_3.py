

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}



def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node] - visited)
    return visited


print(dfs(graph, 'A'))

from collections import deque

def bfs(graph, start):
    queue = deque()
    queue.append(start)
    visited = set()
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

print(bfs(graph, 'A'))



def recursively_test_palindromes(s):
    text = s.replace(" ", '')
    print(text)
    if text[0] != text[-1]:
        return False
    elif len(s) > 3:
        return recursively_test_palindromes(s[1:len(s) -1])
    else:
        return True



print(recursively_test_palindromes('testingworld'))

y = [1,[11,42,[8, 1], 4, [22,21]]]

def productSum(arr):
    result = 0
    for item in arr:
        if type(item) == list:
            result += productSum(item)
        else:
            result += item
    return result

print(productSum(y))

import re


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
    print(largestCount)
    for i in range(largestCount - 1, -1, -1):
        for word in wordMap[i]:
            finalwords.append([word, str(i + 1)])
    return finalwords


document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"

print(word_count_engine(document))






















