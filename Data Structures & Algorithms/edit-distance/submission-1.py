class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp_matrix = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        # last row
        for colidx in range(len(dp_matrix[0]) - 2, -1, -1):
            dp_matrix[len(dp_matrix) - 1][colidx] = dp_matrix[len(dp_matrix) - 1][colidx + 1] + 1

        # last col
        for rowidx in range(len(dp_matrix) - 2, -1, -1):
            dp_matrix[rowidx][len(dp_matrix[rowidx]) - 1] = dp_matrix[rowidx + 1][len(dp_matrix[rowidx]) - 1] + 1
        
        for rowidx in range(len(dp_matrix) -2, -1, -1):
            for colidx in range(len(dp_matrix[rowidx]) -2, -1, -1):
                if word2[colidx] == word1[rowidx]:
                    dp_matrix[rowidx][colidx] = dp_matrix[rowidx + 1][colidx + 1] 
                else:
                    dp_matrix[rowidx][colidx] = min(
                        dp_matrix[rowidx + 1][colidx],
                        dp_matrix[rowidx][colidx + 1],
                        dp_matrix[rowidx + 1][colidx + 1]
                    ) + 1
        print("dp_matrix = ", dp_matrix)
        return dp_matrix[0][0]