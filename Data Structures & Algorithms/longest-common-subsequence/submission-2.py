class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp_matrix = [[0 for _ in range(len(text1))] for _ in range(len(text2))]
        
        # initialize first row...
        found = False 
        for colidx in range(len(dp_matrix[0])):
            if text1[colidx] == text2[0]:
                dp_matrix[0][colidx] = 1
                found = True 
            
            if found == True:
                dp_matrix[0][colidx] = 1

        # initialize first column....
        found = False
        for rowidx in range(len(dp_matrix)):
            if text1[0] == text2[rowidx]:
                dp_matrix[rowidx][0] = 1
                found = True 
            if found == True:
                dp_matrix[rowidx][0] = 1
        
        for rowidx in range(1, len(dp_matrix)):
            for colidx in range(1, len(dp_matrix[rowidx])):
                if text1[colidx] == text2[rowidx]:
                    dp_matrix[rowidx][colidx] = max(1 + dp_matrix[rowidx - 1][colidx - 1], dp_matrix[rowidx - 1][colidx], dp_matrix[rowidx][colidx - 1])
                else:
                    dp_matrix[rowidx][colidx] = max(dp_matrix[rowidx - 1][colidx], dp_matrix[rowidx][colidx - 1])
                
        return dp_matrix[-1][-1]