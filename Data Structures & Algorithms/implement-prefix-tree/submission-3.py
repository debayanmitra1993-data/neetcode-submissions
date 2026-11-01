class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False 

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        pointer = self.root
        for char in word:
            if char in pointer.children:
                pointer = pointer.children[char]
            else:
                pointer.children[char] = TrieNode()
                pointer = pointer.children[char]
        pointer.is_word = True
            
    def search(self, word: str) -> bool:
        pointer = self.root
        for char in word:
            if char not in pointer.children:
                return False 
            pointer = pointer.children[char]
        return pointer.is_word

    def startsWith(self, prefix: str) -> bool:
        pointer = self.root
        for char in prefix:
            if char not in pointer.children:
                return False
            pointer = pointer.children[char]
        return True
