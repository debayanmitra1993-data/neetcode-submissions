class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp_matrix = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]

        for rowidx in range(len(dp_matrix) - 2, -1, -1):
            for colidx in range(len(dp_matrix[rowidx]) - 2, -1, -1):
                if text1[colidx] == text2[rowidx]:
                    dp_matrix[rowidx][colidx] = dp_matrix[rowidx + 1][colidx + 1] + 1
                else:
                    dp_matrix[rowidx][colidx] = max(
                        dp_matrix[rowidx][colidx + 1],
                        dp_matrix[rowidx + 1][colidx]
                    )
        return dp_matrix[0][0]