class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count_island = 0
        for rowidx in range(len(grid)):
            for colidx in range(len(grid[rowidx])):
                if (rowidx, colidx) not in visited and grid[rowidx][colidx] == "1":
                    self.dfs(rowidx, colidx, grid, visited)
                    count_island += 1
        return count_island
    
    def dfs(self, rowidx, colidx, grid, visited):
        if rowidx < 0 or colidx < 0 or rowidx > len(grid) - 1 or colidx > len(grid[0]) - 1:
            return 
        if (rowidx, colidx) in visited:
            return 
        if grid[rowidx][colidx] == "0":
            return 
        
        visited.add((rowidx, colidx))

        self.dfs(rowidx + 1, colidx, grid, visited)
        self.dfs(rowidx - 1, colidx, grid, visited)
        self.dfs(rowidx, colidx + 1, grid, visited)
        self.dfs(rowidx, colidx - 1, grid, visited)