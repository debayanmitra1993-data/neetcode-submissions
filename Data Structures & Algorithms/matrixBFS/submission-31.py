from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        bfsq = deque()
        bfsq.append((0, 0, 0)) # (row, col, depth)
        visited = set()

        while len(bfsq) > 0:
            rowidx, colidx, depth = bfsq.popleft()
            if (rowidx, colidx) in visited:
                continue
            
            visited.add((rowidx, colidx))
            if rowidx == len(grid) - 1 and colidx == len(grid[0]) - 1:
                return depth

            # add children to Q
            if self.checkvalidcell(rowidx + 1, colidx, grid, visited):
                bfsq.append((rowidx + 1, colidx, depth + 1))
            if self.checkvalidcell(rowidx, colidx + 1, grid, visited):
                bfsq.append((rowidx, colidx + 1, depth + 1))
            
            
        
        return -1
            
    def checkvalidcell(self, rowidx, colidx, grid, visited):
        if rowidx < 0 or colidx < 0 or rowidx > len(grid) - 1 or colidx > len(grid[0]) - 1:
            return False
        if grid[rowidx][colidx] == 1:
            return False
        if (rowidx, colidx) in visited:
            return False
        return True
            
