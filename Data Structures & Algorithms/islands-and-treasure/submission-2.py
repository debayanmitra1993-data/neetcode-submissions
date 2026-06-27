class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        infval = 2147483647

        zero_indices = []
        for rowidx in range(len(grid)):
            for colidx in range(len(grid[rowidx])):
                if grid[rowidx][colidx] == 0:
                    zero_indices.append((rowidx, colidx))
        
        for zero_idx in zero_indices:
            rowidx, colidx = zero_idx[0], zero_idx[1]
            self.bfs(rowidx, colidx, grid)
            print("grid = ", grid)
    
    def bfs(self, rowidx, colidx, grid):
        bfsqueue = [(rowidx, colidx, 0)]
        visited = set()
        visited.add((rowidx, colidx))

        while len(bfsqueue) > 0:
            currcell = bfsqueue.pop(0)
            rowidx, colidx, currdist = currcell[0], currcell[1], currcell[2]
            visited.add((rowidx, colidx))

            if currdist < grid[rowidx][colidx]:
                grid[rowidx][colidx] = currdist

            if self.checkvalididx(rowidx - 1, colidx, grid, visited):
                bfsqueue.append((rowidx - 1, colidx, currdist + 1))
            if self.checkvalididx(rowidx + 1, colidx, grid, visited):
                bfsqueue.append((rowidx + 1, colidx, currdist + 1))
            if self.checkvalididx(rowidx, colidx - 1, grid, visited):
                bfsqueue.append((rowidx, colidx - 1, currdist + 1))
            if self.checkvalididx(rowidx, colidx + 1, grid, visited):
                bfsqueue.append((rowidx, colidx + 1, currdist + 1))
            
    def checkvalididx(self, rowidx, colidx, grid, visited):
        if rowidx < 0 or rowidx > len(grid) - 1 or colidx < 0 or colidx > len(grid[0]) - 1:
            return False 
        if (rowidx, colidx) in visited:
            return False 
        if grid[rowidx][colidx] == -1 or grid[rowidx][colidx] == 0:
            return False
        return True 
            


        