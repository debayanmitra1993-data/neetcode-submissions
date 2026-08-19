from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bfsdepthmatrix = [[float("inf") for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for rowidx in range(len(grid)):
            for colidx in range(len(grid[rowidx])):
                if grid[rowidx][colidx] == 2:
                    self.bfstraversal(rowidx, colidx, grid, bfsdepthmatrix, set())
        print("BFS depth matrix = ", bfsdepthmatrix)

        maxtime = 0
        for rowidx in range(len(bfsdepthmatrix)):
            for colidx in range(len(bfsdepthmatrix[rowidx])):
                if grid[rowidx][colidx] == 1 and bfsdepthmatrix[rowidx][colidx] == float("inf"):
                    return -1
                if grid[rowidx][colidx] == 1 and bfsdepthmatrix[rowidx][colidx] != float("inf"):
                    maxtime = max(maxtime, bfsdepthmatrix[rowidx][colidx])
        
        return maxtime


    def bfstraversal(self, rowidx, colidx, grid, bfsdepthmatrix, visited):
        bfsqueue = deque()
        bfsqueue.append((rowidx, colidx, 0))

        while len(bfsqueue) > 0:
            rowidx, colidx, depth = bfsqueue.popleft()
            visited.add((rowidx, colidx))
            if depth < bfsdepthmatrix[rowidx][colidx]:
                bfsdepthmatrix[rowidx][colidx] = depth
            
            # left
            if self.isvalididx(rowidx, colidx - 1, grid, visited):
                bfsqueue.append((rowidx, colidx - 1, depth + 1))

            # right
            if self.isvalididx(rowidx, colidx + 1, grid, visited):
                bfsqueue.append((rowidx, colidx + 1, depth + 1))

            # top
            if self.isvalididx(rowidx - 1, colidx, grid, visited):
                bfsqueue.append((rowidx - 1, colidx, depth + 1))

            # bottom
            if self.isvalididx(rowidx + 1, colidx, grid, visited):
                bfsqueue.append((rowidx + 1, colidx, depth + 1))
    
    def isvalididx(self, rowidx, colidx, grid, visited):
        if rowidx < 0 or colidx < 0 or rowidx > len(grid) - 1 or colidx > len(grid[0]) - 1:
            return False
        if (rowidx, colidx) in visited:
            return False
        
        if grid[rowidx][colidx] == 1:
            return True
        else:
            return False