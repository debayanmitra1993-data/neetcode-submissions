class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        output_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

        for rowidx in range(len(matrix)):
            for colidx in range(len(matrix[rowidx])):
                ele = matrix[rowidx][colidx]
                output_matrix[colidx][rowidx] = ele 
        return output_matrix

        