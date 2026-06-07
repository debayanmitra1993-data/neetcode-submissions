class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False 
    
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        currpointer = self.root 
        for char in word:
            if char not in currpointer.children:
                currpointer.children[char] = TrieNode()
            currpointer = currpointer.children[char]
        currpointer.word = True 

    def search(self, word: str) -> bool:
        return self.searchhelper(word, self.root)
    
    def searchhelper(self, word, currpointer):
        for charidx in range(len(word)):
            char = word[charidx]
            if char == ".":
                if len(currpointer.children) == 0:
                    return False
                for child in currpointer.children:
                    rest_word = word[charidx + 1:]
                    iswordbool = self.searchhelper(rest_word, currpointer.children[child])
                    if iswordbool == True:
                        return True 
                return False
            else:
                if char not in currpointer.children:
                    return False 
                currpointer = currpointer.children[char]
        return currpointer.word
                    
            
