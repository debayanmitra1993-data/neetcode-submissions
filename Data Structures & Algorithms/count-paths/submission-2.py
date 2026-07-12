class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dpmatrix = [[1 for _ in range(n)] for _ in range(m)]
        
        for rowidx in range(len(dpmatrix) - 2, -1, -1):
            for colidx in range(len(dpmatrix[rowidx]) - 2, -1, -1):
                dpmatrix[rowidx][colidx] = dpmatrix[rowidx + 1][colidx] + dpmatrix[rowidx][colidx + 1]
        return dpmatrix[0][0]

