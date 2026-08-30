class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        path = set()
        currpath = []
        outputs = []
        self.recursiontree(n, 0, path, currpath, outputs)
        # print("outputs = ", outputs)

        board = [["." for _ in range(n)] for _ in range(n)]
        board_outputs = []
        for output in outputs:
            board_output = [row.copy() for row in board]
            for cell in output:
                rowidx, colidx = cell[0], cell[1]
                board_output[rowidx][colidx] = "Q"
            board_output = ["".join(row) for row in board_output]
            board_outputs.append(board_output)
        # print("board outputs = ", board_outputs)
        return board_outputs
    
    def recursiontree(self, n, rowidx, path, currpath, outputs):
        if rowidx == n:
            outputs.append(currpath.copy())
            return

        for colidx in range(n):
            if self.checkvalidity(rowidx, colidx, currpath, n):
                path.add((rowidx, colidx))
                currpath.append((rowidx, colidx))
                self.recursiontree(n, rowidx + 1, path, currpath, outputs)
                currpath.pop()
                path.remove((rowidx, colidx))
    
    def checkvalidity(self, rowidx, colidx, currpath, n):
        for ele in currpath:
            if ele[0] == rowidx:
                return False
            if ele[1] == colidx:
                return False
            if abs(ele[0] - rowidx) == abs(ele[1] - colidx):
                return False
            # forbidden_cells = self.get_forbidden_cells(ele[0], ele[1], n)
            #if (rowidx, colidx) in forbidden_cells:
            #    return False
        return True
    
    def get_forbidden_cells(self, rowidx, colidx, n):
        forbidden_cells_set = set()
        
        # go South-East till you reach corner.
        currrowidx, currcolidx = rowidx + 1, colidx + 1
        while currcolidx < n and currrowidx < n:
            forbidden_cells_set.add((currrowidx, currcolidx))
            currrowidx += 1
            currcolidx += 1
        
        # go South-West till you reach corner.
        currrowidx, currcolidx = rowidx + 1, colidx - 1
        while currcolidx >= 0 and currrowidx < n:
            forbidden_cells_set.add((currrowidx, currcolidx))
            currrowidx += 1
            currcolidx -= 1
        
        # go North-West till you reach corner.
        currrowidx, currcolidx = rowidx - 1, colidx - 1
        while currcolidx >= 0 and currrowidx >= 0:
            forbidden_cells_set.add((currrowidx, currcolidx))
            currrowidx -= 1
            currcolidx -= 1
        
        # go North-East till you reach corner.
        currrowidx, currcolidx = rowidx - 1, colidx + 1
        while currcolidx < n and currrowidx >= 0:
            forbidden_cells_set.add((currrowidx, currcolidx))
            currrowidx -= 1
            currcolidx += 1

        
        return forbidden_cells_set