class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n_row = len(obstacleGrid)
        n_col = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[n_row - 1][n_col - 1] == 1:
            return 0

        dpmatrix = [[0 for _ in range(n_col)] for _ in range(n_row)]
        dpmatrix[n_row - 1][n_col - 1] = 1    

        # populate last row...
        for colidx in range(n_col - 2, -1, -1):
            if obstacleGrid[n_row - 1][colidx] == 1:
                dpmatrix[n_row - 1][colidx] = 0
            else:
                dpmatrix[n_row - 1][colidx] = dpmatrix[n_row - 1][colidx + 1]

        # populate last col...
        for rowidx in range(n_row - 2, -1, -1):
            if obstacleGrid[rowidx][n_col - 1] == 1:
                dpmatrix[rowidx][n_col - 1] = 0
            else:
                dpmatrix[rowidx][n_col - 1] = dpmatrix[rowidx + 1][n_col - 1]
        
        for rowidx in range(n_row - 2, -1, -1):
            for colidx in range(n_col - 2, -1, -1):
                if obstacleGrid[rowidx][colidx] == 1:
                    dpmatrix[rowidx][colidx] = 0
                else:
                    dpmatrix[rowidx][colidx] = dpmatrix[rowidx + 1][colidx] + dpmatrix[rowidx][colidx + 1]
        
        return dpmatrix[0][0]




        