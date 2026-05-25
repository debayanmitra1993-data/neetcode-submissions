class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # row check 
        for rowidx in range(len(board)):
            store = {}
            for colidx in range(len(board[rowidx])):
                ele = board[rowidx][colidx]
                if ele == ".":
                    continue

                if ele in store:
                    return False 
                else:
                    store[ele] = True 

        # col check
        for colidx in range(len(board[0])):
            store = {}
            for rowidx in range(len(board)):
                ele = board[rowidx][colidx]
                if ele == ".":
                    continue
                    
                if ele in store:
                    return False 
                else:
                    store[ele] = True

        # 3x3 grid check
        for r in range(0, 3, 1):
            for c in range(0, 3, 1):
                print("3x3 r,c = ", r,c)
                grid_val = self.func_grid_check(board, r*3, c*3)
                if grid_val == False:
                    return False
        return True 

    def func_grid_check(self, board, rowidx, colidx):
        print("entering func grid check with = ", rowidx, colidx)
        store = {}
        for row in range(rowidx, rowidx + 3, 1):
            for col in range(colidx, colidx + 3, 1):
                print("r, c = ", row, col)
                ele = board[row][col]
                if ele == ".":
                    continue 
                
                if ele in store:
                    return False 
                store[ele] = True 
        return True 

        