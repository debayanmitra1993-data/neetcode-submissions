class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # text1 is in column
        # text2 is in row

        dpmatrix = [
            [0 for _ in range(len(text1))] for _ in range(len(text2))
        ]
        if text1[0] == text2[0]:
            dpmatrix[0][0] = 1 
        
        for colidx in range(1, len(dpmatrix[0])):
            if text2[0] == text1[colidx]:
                dpmatrix[0][colidx] = 1 
            else:
                dpmatrix[0][colidx] = dpmatrix[0][colidx - 1]
        
        for rowidx in range(1, len(dpmatrix)):
            if text1[0] == text2[rowidx]:
                dpmatrix[rowidx][0] = 1
            else:
                dpmatrix[rowidx][0] = dpmatrix[rowidx - 1][0]
        
        for rowidx in range(1, len(dpmatrix)):
            for colidx in range(1, len(dpmatrix[rowidx])):
                if text1[colidx] == text2[rowidx]:
                    dpmatrix[rowidx][colidx] = 1 + dpmatrix[rowidx - 1][colidx - 1]
                else:
                    dpmatrix[rowidx][colidx] = max(
                        dpmatrix[rowidx - 1][colidx],
                        dpmatrix[rowidx][colidx - 1]
                    )
        return dpmatrix[-1][-1]
