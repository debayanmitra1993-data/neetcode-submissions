class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_matrix = [[1 for _ in range(m)] for _ in range(n)]

        for rowidx in range(1, len(dp_matrix)):
            for colidx in range(1, len(dp_matrix[rowidx])):
                dp_matrix[rowidx][colidx] = dp_matrix[rowidx - 1][colidx] + dp_matrix[rowidx][colidx - 1]
        return dp_matrix[-1][-1] 
        
        