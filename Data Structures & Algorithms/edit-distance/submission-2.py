class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        nrow = len(word1) + 1
        ncol = len(word2) + 1

        dpmatrix = [[0 for _ in range(ncol)] for _ in range(nrow)]

        # fill last row..    
        for colidx in range(ncol - 2, -1, -1):
            dpmatrix[nrow - 1][colidx] = dpmatrix[nrow - 1][colidx + 1] + 1
        
        # fill last col..    
        for rowidx in range(nrow - 2, -1, -1):
            dpmatrix[rowidx][ncol - 1] = dpmatrix[rowidx + 1][ncol - 1] + 1
        
        # fill rest of the dp matrix cells..
        for rowidx in range(nrow - 2, -1, -1):
            for colidx in range(ncol - 2, -1, -1):
                if word1[rowidx] == word2[colidx]:
                    dpmatrix[rowidx][colidx] = dpmatrix[rowidx + 1][colidx + 1]
                else:
                    dpmatrix[rowidx][colidx] = 1 + min(
                        dpmatrix[rowidx + 1][colidx],
                        dpmatrix[rowidx + 1][colidx + 1],
                        dpmatrix[rowidx][colidx + 1]
                    )
        return dpmatrix[0][0]