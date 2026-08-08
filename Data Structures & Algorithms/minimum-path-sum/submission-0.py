class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dpmatrix = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dpmatrix[0][0] = grid[0][0]

        for colidx in range(1, len(grid[0])):
            dpmatrix[0][colidx] = dpmatrix[0][colidx - 1] + grid[0][colidx]
        
        for rowidx in range(1, len(grid)):
            dpmatrix[rowidx][0] = dpmatrix[rowidx - 1][0] + grid[rowidx][0]
        
        for rowidx in range(1, len(grid)):
            for colidx in range(1, len(grid[rowidx])):
                dpmatrix[rowidx][colidx] = min(
                    dpmatrix[rowidx - 1][colidx],
                    dpmatrix[rowidx][colidx - 1]
                ) + grid[rowidx][colidx]
        return dpmatrix[-1][-1]