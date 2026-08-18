class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count_islands = 0
        for rowidx in range(len(grid)):
            for colidx in range(len(grid[rowidx])):
                if (rowidx, colidx) not in visited and grid[rowidx][colidx] == "1":
                    self.dfstree(rowidx, colidx, grid, visited)
                    count_islands += 1
        return count_islands
    
    def dfstree(self, rowidx, colidx, grid, visited):
        if rowidx < 0 or colidx < 0 or rowidx > len(grid) - 1 or colidx > len(grid[0]) - 1:
            return 
        if grid[rowidx][colidx] == "0":
            return 
        if (rowidx, colidx) in visited:
            return 

        visited.add((rowidx, colidx))
        self.dfstree(rowidx - 1, colidx, grid, visited)
        self.dfstree(rowidx + 1, colidx, grid, visited)
        self.dfstree(rowidx, colidx - 1, grid, visited)
        self.dfstree(rowidx, colidx + 1, grid, visited)

        