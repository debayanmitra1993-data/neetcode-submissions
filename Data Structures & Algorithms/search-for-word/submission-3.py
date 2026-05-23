class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for rowidx in range(len(board)):
            for colidx in range(len(board[rowidx])):
                char = board[rowidx][colidx]
                if char == word[0]:
                    finalvisited = []
                    self.findinboard(word, rowidx, colidx, set(), board, 0, finalvisited)
                    if len(finalvisited) > 0:
                        return True
        return False
    
    def findinboard(self, word, rowidx, colidx, visited, board, depth, finalvisited):
        if word[depth] != board[rowidx][colidx]:
            return 
        elif word[depth] == board[rowidx][colidx]:
            visited.add((rowidx, colidx))
            if depth == len(word) - 1:
                finalvisited.append(visited.copy())
                return 
            else:
                if rowidx - 1 >= 0:
                    if (rowidx - 1, colidx) not in visited:
                        self.findinboard(word, rowidx -1, colidx, visited, board, depth + 1, finalvisited)
                if rowidx + 1 < len(board):
                    if (rowidx + 1, colidx) not in visited:
                        self.findinboard(word, rowidx +1, colidx, visited, board, depth + 1, finalvisited)
                if colidx - 1 >= 0:
                    if (rowidx, colidx - 1) not in visited:
                        self.findinboard(word, rowidx , colidx -1, visited, board, depth + 1, finalvisited)
                if colidx + 1 < len(board[rowidx]):
                    if (rowidx, colidx + 1) not in visited:
                        self.findinboard(word, rowidx, colidx + 1, visited, board, depth + 1, finalvisited)
                
            visited.remove((rowidx, colidx))

        



