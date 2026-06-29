class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n_row = len(board)
        n_col = len(board[0])

        for colidx in range(n_col):
            if board[0][colidx] == "O":
                self.dfs(board, 0, colidx)
        for colidx in range(n_col):
            if board[n_row - 1][colidx] == "O":
                self.dfs(board, n_row - 1, colidx)
        for rowidx in range(n_row):
            if board[rowidx][0] == "O":
                self.dfs(board, rowidx, 0)
        for rowidx in range(len(board)):
            if board[rowidx][n_col - 1] == "O":
                self.dfs(board, rowidx, n_col - 1)
        
        # replace O with X and T with O
        for rowidx in range(n_row):
            for colidx in range(n_col):
                if board[rowidx][colidx] == "O":
                    board[rowidx][colidx] = "X"
                if board[rowidx][colidx] == "T":
                    board[rowidx][colidx] = "O"
        

    
    def dfs(self, board, rowidx, colidx):
        if rowidx < 0 or colidx < 0 or rowidx > len(board) - 1 or colidx > len(board[0]) - 1:
            return 
        if board[rowidx][colidx] == "X":
            return 
        if board[rowidx][colidx] == "T":
            return 

        board[rowidx][colidx] = "T"
        self.dfs(board, rowidx - 1, colidx)
        self.dfs(board, rowidx + 1, colidx)
        self.dfs(board, rowidx, colidx - 1)
        self.dfs(board, rowidx, colidx + 1)
