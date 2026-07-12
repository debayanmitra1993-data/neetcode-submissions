class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n_rows = len(obstacleGrid)
        n_cols = len(obstacleGrid[0])

        if n_rows == 1 and n_cols == 1:
            if obstacleGrid[0][0] == 1:
                return 0
            else:
                return 1

        dpmatrix = [[1 for _ in range(n_cols)] for _ in range(n_rows)]

        for rowidx in range(n_rows - 2, -1, -1):
            if obstacleGrid[rowidx][n_cols - 1] == 1:
                dpmatrix[rowidx][n_cols - 1] = 0
            else:
                dpmatrix[rowidx][n_cols - 1] = dpmatrix[rowidx + 1][n_cols - 1] 
        
        for colidx in range(n_cols - 2, -1, -1):
            if obstacleGrid[n_rows - 1][colidx] == 1:
                dpmatrix[n_rows - 1][colidx] = 0
            else:
                dpmatrix[n_rows - 1][colidx] = dpmatrix[n_rows - 1][colidx + 1]
        
        for rowidx in range(n_rows - 2, -1, -1):
            for colidx in range(n_cols - 2, -1, -1):
                if obstacleGrid[rowidx][colidx] == 1:
                    dpmatrix[rowidx][colidx] = 0
                else:
                    dpmatrix[rowidx][colidx] = dpmatrix[rowidx + 1][colidx] + dpmatrix[rowidx][colidx + 1]
        
        return dpmatrix[0][0]

        