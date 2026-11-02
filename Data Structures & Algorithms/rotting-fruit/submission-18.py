from collections import deque 

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_oranges = {}
        for rowidx in range(len(grid)):
            for colidx in range(len(grid[rowidx])):
                if grid[rowidx][colidx] == 1:
                    fresh_oranges[(rowidx, colidx)] = float("inf")
        
        for rowidx in range(len(grid)):
            for colidx in range(len(grid[rowidx])):
                if grid[rowidx][colidx] == 2:
                    self.bfs(rowidx, colidx, fresh_oranges, grid)
        
        print("fresh oranges = ", fresh_oranges)
        
        maxval = 0
        for key in fresh_oranges.keys():
            if fresh_oranges[key] == float("inf"):
                return -1
            if fresh_oranges[key] > maxval:
                maxval = fresh_oranges[key]
        return maxval
            

    
    def bfs(self, rowidx, colidx, fresh_oranges, grid):
        bfsqueue = deque()
        visited = set()
        bfsqueue.append((rowidx, colidx, 0)) # (r, c, depth)

        while len(bfsqueue) > 0:
            rowidx, colidx, depth = bfsqueue.popleft()
            print("r,c,d = ", rowidx, colidx, depth)
            if (rowidx, colidx) in visited:
                continue 
            
            visited.add((rowidx, colidx))
            if grid[rowidx][colidx] == 1:
                if depth < fresh_oranges[(rowidx, colidx)]:
                    print("fresh_oranges = ", fresh_oranges)
                    fresh_oranges[(rowidx, colidx)] = depth
            
            if self.isvalidfreshfruit(rowidx + 1, colidx, grid, visited):
                bfsqueue.append((rowidx + 1, colidx, depth + 1))
            if self.isvalidfreshfruit(rowidx - 1, colidx, grid, visited):
                bfsqueue.append((rowidx - 1, colidx, depth + 1))
            if self.isvalidfreshfruit(rowidx, colidx + 1, grid, visited):
                bfsqueue.append((rowidx, colidx + 1, depth + 1))
            if self.isvalidfreshfruit(rowidx, colidx - 1, grid, visited):
                bfsqueue.append((rowidx, colidx - 1, depth + 1))
    
    def isvalidfreshfruit(self, rowidx, colidx, grid, visited):
        if rowidx < 0 or colidx < 0 or rowidx > len(grid) - 1 or colidx > len(grid[0]) - 1:
            return False
        
        if (rowidx, colidx) in visited:
            return False
        
        if grid[rowidx][colidx] == 1:
            return True
        return False

            
            


        