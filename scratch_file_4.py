
# implement a Trie from a list of words
def getNeighbors(r, c, board):
    neighbors = []
    if r > 0 and c > 0:
        neighbors.append([r - 1, c - 1])
    if r > 0 and c < len(board[0]) - 1:
        neighbors.append([r -1, c + 1])
    if r < len(board) - 1 and c < len(board[0]) - 1:
        neighbors.append([r + 1, c + 1])
    if r < len(board) - 1 and c > 0:
        neighbors.append([r + 1, c - 1])
    if r > 0:
        neighbors.append([r -1, c])
    if r < len(board) - 1:
        neighbors.append([r + 1, c])
    if c > 0:
        neighbors.append([r, c - 1])
    if c < len(board[0]) - 1:
        neighbors.append([r, c + 1])
    return neighbors

class Trie:
    def __init(self):
        self.root = {}
        self.endSymbol = "*"

    def addWord(self, word):
        current = self.root
        for letter in word:
            if current not in current:
                current[letter] = {}
            current = current[letter]
        current[self.endSymbol] = word


def explore(r, c, visited, board, trie, wordsFound):
    if visited[r][c]:
        return
    letter = board[r][c]
    if letter not in trie:
        return
    visited[r][c] = True
    trieNode = trie[letter]
    if "*" in trieNode:
        wordsFound[trieNode["*"]] = True


def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.addWord(word)
    wordsFound = {}
    visited = [[False for letter in row] for row in board]
    for r in range(len(board)):
        for c in range(len(board[r])):
            explore(r, c, visited, board, trie.root, wordsFound)
    return list(wordsFound.keys())
