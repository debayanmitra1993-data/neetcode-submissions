class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        currpointer = self.root
        for char in word:
            if char not in currpointer.children:
                currpointer.children[char] = TrieNode()
            currpointer = currpointer.children[char]
        currpointer.word = True

    def search(self, word: str) -> bool:
        currpointer = self.root
        for char in word:
            if char not in currpointer.children:
                return False 
            else:
                currpointer = currpointer.children[char]
        return currpointer.word

    def startsWith(self, prefix: str) -> bool:
        currpointer = self.root
        for char in prefix:
            if char not in currpointer.children:
                return False
            else:
                currpointer = currpointer.children[char]
        return True 

        
        