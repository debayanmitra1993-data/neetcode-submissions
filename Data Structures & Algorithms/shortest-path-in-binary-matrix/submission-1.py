class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1 
        if grid[-1][-1] != 0:
            return -1 
        
        return self.bfs(grid, 0, 0, set(), 1)
    
    def bfs(self, grid, rowidx, colidx, visited, depth):
        bfsqueue = [(rowidx, colidx, depth)]
        while len(bfsqueue) > 0:
            ele = bfsqueue.pop(0)
            rowidx, colidx, depth = ele[0], ele[1], ele[2]

            if rowidx == len(grid) - 1 and colidx == len(grid[0]) - 1:
                if grid[rowidx][colidx] == 0:
                    return depth
                else:
                    return -1

            if (rowidx, colidx) not in visited:
                visited.add((rowidx, colidx))
            else:
                continue

            # add 3 children (right, bottom, right-bottom)
            if self.isvalididx(grid, rowidx + 1, colidx, visited):
                bfsqueue.append((rowidx + 1, colidx, depth + 1))
            if self.isvalididx(grid, rowidx, colidx + 1, visited):
                bfsqueue.append((rowidx, colidx + 1, depth + 1))
            if self.isvalididx(grid, rowidx + 1, colidx + 1, visited):
                bfsqueue.append((rowidx + 1, colidx + 1, depth + 1))
        return -1
        
        

        

    
    def isvalididx(self, grid, rowidx, colidx, visited):
        if rowidx < 0 or colidx < 0 or rowidx > len(grid) - 1 or colidx > len(grid[0]) - 1:
            return False 
        if (rowidx, colidx) in visited:
            return False 
        if grid[rowidx][colidx] == 1:
            return False 
        return True 
        

        