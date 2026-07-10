class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.n_rows = len(self.matrix)
        self.n_cols = len(self.matrix[0])
        self.row_sum_matrix = self.compute_row_sum()
        self.col_sum_matrix = self.compute_col_sum()
        self.tot_sum_matrix = self.compute_tot_sum()
    
    def compute_row_sum(self):
        row_sum_matrix = [row[:] for row in self.matrix]
        for rowidx in range(self.n_rows):
            rowsum = 0
            for colidx in range(self.n_cols):
                rowsum += self.matrix[rowidx][colidx]
                row_sum_matrix[rowidx][colidx] = rowsum
        return row_sum_matrix
    
    def compute_col_sum(self):
        col_sum_matrix = [row[:] for row in self.matrix]
        for colidx in range(self.n_cols):
            colsum = 0
            for rowidx in range(self.n_rows):
                colsum += self.matrix[rowidx][colidx]
                col_sum_matrix[rowidx][colidx] = colsum
        return col_sum_matrix
    
    def compute_tot_sum(self):
        tot_sum_matrix = [row[:] for row in self.matrix]
        for colidx in range(self.n_cols):
            tot_sum_matrix[0][colidx] = self.row_sum_matrix[0][colidx]
        for rowidx in range(self.n_rows):
            tot_sum_matrix[rowidx][0] = self.col_sum_matrix[rowidx][0]
        for rowidx in range(1, self.n_rows):
            for colidx in range(1, self.n_cols):
                tot_sum_matrix[rowidx][colidx] = tot_sum_matrix[rowidx][colidx - 1] + self.col_sum_matrix[rowidx][colidx]
        return tot_sum_matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        val = self.tot_sum_matrix[row2][col2]
        if row1 - 1 >= 0:
            val = val - self.tot_sum_matrix[row1 - 1][col2]
        if col1 - 1 >= 0:
            val = val - self.tot_sum_matrix[row2][col1 - 1]
        if row1 - 1 >= 0 and col1 - 1 >= 0:
            val = val + self.tot_sum_matrix[row1 - 1][col1 - 1]
        return val

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)