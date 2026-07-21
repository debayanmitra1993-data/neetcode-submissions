class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        pointer = self.root
        for char in word:
            if char not in pointer.children:
                pointer.children[char] = TrieNode()
            pointer = pointer.children[char]
        pointer.word = True
    
    def search(self, word):
        pointer = self.root
        for char in word:
            if char not in pointer.children:
                return False
            pointer = pointer.children[char]
        return pointer.word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        mytrie = Trie()
        for word in words:
            mytrie.insert(word)
        pointer = mytrie.root
        
        outlst = []
        for rowidx in range(len(board)):
            for colidx in range(len(board[rowidx])):
                visited = set()
                currstr = ""
                self.dfs(rowidx, colidx, board, pointer, visited, outlst, currstr)
        return list(set(outlst))
    
    def dfs(self, rowidx, colidx, board, pointer, visited, outlst, currstr):
        char = board[rowidx][colidx]
        if char not in pointer.children:
            return 
        else:
            visited.add((rowidx, colidx))
            pointer = pointer.children[char]
            currstr = currstr + char
            if pointer.word == True:
                outlst.append(currstr)
            if self.isvalididx(rowidx - 1, colidx, board, visited):
                self.dfs(rowidx - 1, colidx, board, pointer, visited, outlst, currstr)
            if self.isvalididx(rowidx + 1, colidx, board, visited):
                self.dfs(rowidx + 1, colidx, board, pointer, visited, outlst, currstr)
            if self.isvalididx(rowidx, colidx- 1, board, visited):
                self.dfs(rowidx , colidx - 1, board, pointer, visited, outlst, currstr)
            if self.isvalididx(rowidx, colidx + 1, board, visited):
                self.dfs(rowidx , colidx + 1, board, pointer, visited, outlst, currstr)
            visited.remove((rowidx, colidx))
            

        
    def isvalididx(self, rowidx, colidx, board, visited):
        if rowidx < 0 or colidx < 0 or rowidx > len(board) - 1 or colidx > len(board[0]) - 1:
            return False
        
        if (rowidx, colidx) in visited:
            return False
        
        return True

        
    

        
        