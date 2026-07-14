class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        current_zero_cells = set()
        # get all zero cells..
        for rowidx in range(len(matrix)):
            for colidx in range(len(matrix[rowidx])):
                if matrix[rowidx][colidx] == 0:
                    current_zero_cells.add((rowidx, colidx))
        
        zero_rows_set = set()
        zero_cols_set = set()
        for zerocell in current_zero_cells:
            rowidx, colidx = zerocell[0], zerocell[1]
            if rowidx not in zero_rows_set:
                self.set_row_zero(matrix, rowidx)
                zero_rows_set.add(rowidx)
            if colidx not in zero_cols_set:
                self.set_col_zero(matrix, colidx)
                zero_cols_set.add(colidx)
    
        
    
    def set_row_zero(self, matrix, rowidx):
        for colidx in range(len(matrix[rowidx])):
            matrix[rowidx][colidx] = 0
    
    def set_col_zero(self, matrix, colidx):
        for rowidx in range(len(matrix)):
            matrix[rowidx][colidx] = 0
