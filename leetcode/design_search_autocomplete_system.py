import collections

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}
        self.subs = set()
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def setup(self, words):
        for word in words:
            self.add(word)
            
    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node.subs.add(word)
            node = node.children[c]
        node.subs.add(word)
        node.word = True
        
    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return ''
            else:
                node = node.children[c]
        return node.subs
                

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.sentences = sentences
        self.times = times
        self.cnts = collections.defaultdict(int)
        self.ords = collections.defaultdict(list)
        self.trie = Trie()
        self.trie.setup(sentences)
        self.ins = ''
        self.add_cnts()
        
    def add_cnts(self):
        for i in range(len(self.times)):
            self.cnts[self.sentences[i]] = self.times[i]
            self.sorter(self.sentences[i]) 
        
    def sorter(self, sent):
        if sent not in self.ords:
            self.ords[sent] = [ord(c) for c in sent]

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.trie.add(self.ins)
            self.cnts[self.ins] += 1
            self.sorter(self.ins)
            self.ins = ""
            return []
        self.ins += c
        sents = list(self.trie.search(self.ins))
        sents.sort(key=lambda x: self.ords[x])
        sents.sort(key=lambda x: -self.cnts[x])
        return sents[:3]