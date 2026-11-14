class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n_cols = len(text1)
        n_rows = len(text2)
        dpmatrix = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
        if text2[0] == text1[0]:
            dpmatrix[0][0] = 1

        # populate first row..
        for colidx in range(1, n_cols):
            if text2[0] == text1[colidx]:
                dpmatrix[0][colidx] = 1
            else:
                dpmatrix[0][colidx] = dpmatrix[0][colidx - 1]
        
        # populate first col..
        for rowidx in range(1, n_rows):
            if text1[0] == text2[rowidx]:
                dpmatrix[rowidx][0] = 1
            else:
                dpmatrix[rowidx][0] = dpmatrix[rowidx - 1][0]
        
        # populate rest of the dp matrix..
        for rowidx in range(1, n_rows):
            for colidx in range(1, n_cols):
                if text2[rowidx] == text1[colidx]:
                    dpmatrix[rowidx][colidx] = 1 + dpmatrix[rowidx - 1][colidx - 1]
                else:
                    dpmatrix[rowidx][colidx] = max(
                        dpmatrix[rowidx - 1][colidx],
                        dpmatrix[rowidx][colidx - 1]
                    )
        return dpmatrix[-1][-1]