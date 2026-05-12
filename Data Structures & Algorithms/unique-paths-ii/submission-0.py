class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp_matrix = [[1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        
        # iterate across last row and allocate...
        foundone = False
        for colidx in range(len(obstacleGrid[0]) - 1, -1, -1):
            if foundone == True:
                dp_matrix[len(obstacleGrid) - 1][colidx] = 0
            else:
                if obstacleGrid[len(obstacleGrid) - 1][colidx] == 1:
                    foundone = True
                    dp_matrix[len(obstacleGrid) - 1][colidx] = 0
        
        # iterate across last column and allocate...
        foundone = False
        for rowidx in range(len(obstacleGrid) - 1, -1, -1):
            if foundone == True:
                dp_matrix[rowidx][len(obstacleGrid[rowidx]) - 1] = 0
            else:
                if obstacleGrid[rowidx][len(obstacleGrid[rowidx]) - 1] == 1:
                    foundone = True
                    dp_matrix[rowidx][len(obstacleGrid[rowidx]) - 1] = 0
        
        for rowidx in range(len(dp_matrix) - 2, -1, -1):
            for colidx in range(len(dp_matrix[rowidx]) - 2, -1, -1):
                if obstacleGrid[rowidx][colidx] == 1:
                    dp_matrix[rowidx][colidx] = 0
                else:
                    dp_matrix[rowidx][colidx] = dp_matrix[rowidx + 1][colidx] + dp_matrix[rowidx][colidx + 1]

        return dp_matrix[0][0]