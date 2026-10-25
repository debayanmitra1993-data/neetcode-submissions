class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        for rowidx in range(len(grid)):
            for colidx in range(len(grid[rowidx])):
                if grid[rowidx][colidx] == 1:
                    visited = set()
                    return self.dfsrecursion(rowidx, colidx, grid, visited)
    
    def dfsrecursion(self, rowidx, colidx, grid, visited):
        if rowidx < 0 or colidx < 0 or rowidx > len(grid) - 1 or colidx > len(grid[0]) - 1:
            return 1
        
        if grid[rowidx][colidx] == 0:
            return 1
        
        visited.add((rowidx, colidx))
        
        subp = 0
        if (rowidx, colidx + 1) not in visited:
            subp += self.dfsrecursion(rowidx, colidx + 1, grid, visited)
        if (rowidx, colidx - 1) not in visited:
            subp += self.dfsrecursion(rowidx, colidx - 1, grid, visited)
        if (rowidx + 1, colidx) not in visited:
            subp += self.dfsrecursion(rowidx + 1, colidx, grid, visited)
        if (rowidx - 1, colidx) not in visited:
            subp += self.dfsrecursion(rowidx - 1, colidx, grid, visited)
        
        return subp
        