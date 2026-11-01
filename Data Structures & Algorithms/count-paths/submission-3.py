class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dpmatrix = [[0 for _ in range(n)] for _ in range(m)]

        # populate last row as '1'
        for colidx in range(len(dpmatrix[0])):
            dpmatrix[m - 1][colidx] = 1
        
        # populate last col as '1'
        for rowidx in range(len(dpmatrix)):
            dpmatrix[rowidx][n - 1] = 1
        
        
        for rowidx in range(m - 2, -1, -1):
            for colidx in range(n -2, -1, -1):
                dpmatrix[rowidx][colidx] = dpmatrix[rowidx + 1][colidx] + dpmatrix[rowidx][colidx + 1]
        
        return dpmatrix[0][0]