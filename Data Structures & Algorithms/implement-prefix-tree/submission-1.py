class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        pointer = self.root 
        for char in word:
            if char not in pointer.children:
                pointer.children[char] = TrieNode()
            pointer = pointer.children[char]
        pointer.word = True

    def search(self, word: str) -> bool:
        pointer = self.root
        for char in word:
            if char not in pointer.children:
                return False
            else:
                pointer = pointer.children[char]
        return pointer.word
        
    def startsWith(self, prefix: str) -> bool:
        pointer = self.root 
        for char in prefix:
            if char not in pointer.children:
                return False
            else:
                pointer = pointer.children[char]
        return True
        
        