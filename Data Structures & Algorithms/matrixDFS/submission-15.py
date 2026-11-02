class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        n_row = len(grid)
        n_col = len(grid[0])
        if grid[0][0] == 1 or grid[n_row-1][n_col-1] == 1:
            return 0
        
        visited = set()
        return self.dfsbacktrack(grid, 0, 0, visited)
    
    def dfsbacktrack(self, grid, rowidx, colidx, visited):
        if rowidx < 0 or colidx < 0 or rowidx > len(grid) - 1 or colidx > len(grid[0]) - 1:
            return 0 
        if (rowidx, colidx) in visited:
            return 0 
        if grid[rowidx][colidx] == 1:
            return 0
        
        if rowidx == len(grid) - 1 and colidx == len(grid[0])-1:
            return 1
        
        visited.add((rowidx, colidx))
        count = 0
        count += self.dfsbacktrack(grid, rowidx + 1, colidx, visited)
        count += self.dfsbacktrack(grid, rowidx - 1, colidx, visited)
        count += self.dfsbacktrack(grid, rowidx, colidx + 1, visited)
        count += self.dfsbacktrack(grid, rowidx, colidx - 1, visited)

        visited.remove((rowidx, colidx))
        return count