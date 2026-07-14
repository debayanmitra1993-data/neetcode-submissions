class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction_order = ["right", "down", "left", "up"]
        curr_direction_idx = 0
        visited = set() 
        output_lst = []
        rowidx, colidx = 0, 0
        
        while True:
            print("r,c = ", rowidx, colidx)
            visited.add((rowidx, colidx))
            output_lst.append(matrix[rowidx][colidx])
            

            rowidx, colidx, curr_direction_idx = self.get_next_cell(curr_direction_idx, rowidx, colidx, matrix, visited)
            if not self.isvalididx(rowidx, colidx, matrix, visited):
                break
        
        return output_lst
            

    def get_next_cell(self, curr_direction_idx, rowidx, colidx, matrix, visited):
        if curr_direction_idx == 0:
            if self.isvalididx(rowidx, colidx + 1, matrix, visited):
                return rowidx, colidx + 1, curr_direction_idx
            else:
                return rowidx + 1, colidx, (curr_direction_idx + 1) % 4
        elif curr_direction_idx == 1:
            if self.isvalididx(rowidx + 1, colidx, matrix, visited):
                return rowidx + 1, colidx, curr_direction_idx
            else:
                return rowidx, colidx - 1, (curr_direction_idx + 1) % 4
        elif curr_direction_idx == 2:
            if self.isvalididx(rowidx, colidx - 1, matrix, visited):
                return rowidx, colidx - 1, curr_direction_idx
            else:
                return rowidx - 1, colidx, (curr_direction_idx + 1) % 4
        elif curr_direction_idx == 3:
            if self.isvalididx(rowidx - 1, colidx, matrix, visited):
                return rowidx - 1, colidx, curr_direction_idx
            else:
                return rowidx, colidx + 1, (curr_direction_idx + 1) % 4
    
    def isvalididx(self, rowidx, colidx, matrix, visited):
        if rowidx < 0 or colidx < 0 or rowidx > len(matrix) - 1 or colidx > len(matrix[0]) - 1:
            return False
        
        if (rowidx, colidx) in visited:
            return False
        else:
            return True 
        

        
        