class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rowidx, colidx = 0, 0
        outarr = [0]*(len(matrix)**2)
        visited = set()
        idx = 0
        directions = ["right", "down", "left", "up"]
        current_direction = "right"

        while True:
            outarr[idx] = matrix[rowidx][colidx]
            visited.add((rowidx, colidx))

            rowidx, colidx, current_direction = self.get_next_cell(rowidx, colidx, visited, matrix, current_direction)
            if rowidx == -1 and colidx == -1:
                break
            
            idx += 1
        print("outarr = ", outarr)

        rowidx, colidx = 0, len(matrix[0]) - 1
        current_direction = "right"
        visited = set()
        for idx in range(len(outarr)):
            matrix[rowidx][colidx] = outarr[idx]
            visited.add((rowidx, colidx))
            rowidx, colidx, current_direction = self.get_next_cell(rowidx, colidx, visited, matrix, current_direction)

    
    def get_next_cell(self, rowidx, colidx, visited, matrix, current_direction):
        if current_direction == "right":
            if self.isvalididx(rowidx, colidx + 1, visited, matrix):
                return rowidx, colidx + 1, "right"
            else:
                if self.isvalididx(rowidx + 1, colidx, visited, matrix):
                    return rowidx + 1, colidx, "down"
                else:
                    return -1, -1, None
        elif current_direction == "down":
            if self.isvalididx(rowidx + 1, colidx, visited, matrix):
                return rowidx + 1, colidx , "down"
            else:
                if self.isvalididx(rowidx, colidx - 1, visited, matrix):
                    return rowidx, colidx - 1, "left"
                else:
                    return -1, -1, None
        elif current_direction == "left":
            if self.isvalididx(rowidx, colidx - 1, visited, matrix):
                return rowidx, colidx - 1, "left"
            else:
                if self.isvalididx(rowidx - 1, colidx, visited, matrix):
                    return rowidx - 1, colidx, "up"
                else:
                    return -1, -1, None
        elif current_direction == "up":
            if self.isvalididx(rowidx - 1, colidx, visited, matrix):
                return rowidx - 1, colidx, "up"
            else:
                if self.isvalididx(rowidx, colidx + 1, visited, matrix):
                    return rowidx, colidx + 1, "right"
                else:
                    return -1, -1, None
    
    def isvalididx(self, rowidx, colidx, visited, matrix):
        if rowidx < 0 or colidx < 0 or rowidx > len(matrix) - 1 or colidx > len(matrix[0]) - 1:
            return False
        
        if (rowidx, colidx) in visited:
            return False
        
        return True