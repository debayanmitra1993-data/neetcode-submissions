class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        return self.bfs(grid, 0, 0, 0, set())
    
    def bfs(self, grid, rowidx, colidx, depth, visited):
        bfsqueue =  [(rowidx, colidx, depth)]

        while len(bfsqueue) > 0:
            ele = bfsqueue.pop(0)
            rowidx, colidx, depth = ele[0], ele[1], ele[2]
            if (rowidx, colidx) not in visited:
                visited.add((rowidx, colidx))
            else:
                continue 
            
            if rowidx == len(grid) - 1 and colidx == len(grid[0]) - 1:
                if grid[rowidx][colidx] == 0:
                    return ele[2]
                    print("final destination = ", ele)

            # add valid children
            if self.isvalididx(rowidx + 1, colidx, grid, visited):
                bfsqueue.append((rowidx + 1, colidx, depth + 1))
            #if self.isvalididx(rowidx - 1, colidx, grid, visited):
            #    bfsqueue.append((rowidx - 1, colidx, depth + 1))
            if self.isvalididx(rowidx, colidx + 1, grid, visited):
                bfsqueue.append((rowidx, colidx + 1, depth + 1))
            #if self.isvalididx(rowidx, colidx - 1, grid, visited):
            #    bfsqueue.append((rowidx, colidx - 1, depth + 1))
        
        return -1
            
    
    def isvalididx(self, rowidx, colidx, grid, visited):
        if rowidx < 0 or colidx < 0 or rowidx > len(grid) - 1 or colidx > len(grid[0]) - 1:
            return False 
        
        if grid[rowidx][colidx] == 1:
            return False 
        
        if (rowidx, colidx) in visited:
            return False 
        
        return True 