from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        bfsq = deque()
        bfsq.append((0, 0, 0))
        visited = set()

        while len(bfsq) > 0:
            rowidx, colidx, depth = bfsq.popleft()
            if rowidx == len(grid) - 1 and colidx == len(grid[0]) - 1:
                return depth + 1

            if (rowidx, colidx) in visited:
                continue
            
            visited.add((rowidx, colidx))
            if self.isvalidcell(rowidx + 1, colidx, grid, visited):
                bfsq.append((rowidx + 1, colidx, depth + 1))
            if self.isvalidcell(rowidx, colidx + 1, grid, visited):
                bfsq.append((rowidx, colidx + 1, depth + 1))
            if self.isvalidcell(rowidx + 1, colidx + 1, grid, visited):
                bfsq.append((rowidx + 1, colidx + 1, depth + 1))
        
        return -1
    
    def isvalidcell(self, rowidx, colidx, grid, visited):
        if rowidx < 0 or colidx < 0 or rowidx > len(grid) - 1 or colidx > len(grid[0]) - 1:
            return False
        if grid[rowidx][colidx] == 1:
            return False
        if (rowidx, colidx) in visited:
            return False
        return True
            
        