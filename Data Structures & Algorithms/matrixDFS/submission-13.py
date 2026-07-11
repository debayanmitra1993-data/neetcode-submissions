class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visited = set()
        return self.dfs(0, 0, grid, visited)
    
    def dfs(self, rowidx, colidx, grid, visited):
        if rowidx < 0 or colidx < 0 or rowidx > len(grid) - 1 or colidx > len(grid[0]) - 1:
            return 0
        if (rowidx, colidx) in visited:
            return 0
        if grid[rowidx][colidx] == 1:
            return 0
        if rowidx == len(grid) - 1 and colidx == len(grid[0]) - 1:
            return 1


        visited.add((rowidx, colidx))
        count_paths_top = self.dfs(rowidx - 1, colidx, grid, visited)
        count_paths_bottom = self.dfs(rowidx + 1, colidx, grid, visited)
        count_paths_left = self.dfs(rowidx, colidx - 1, grid, visited)
        count_paths_right = self.dfs(rowidx, colidx + 1, grid, visited)
        visited.remove((rowidx, colidx))
        return count_paths_top + count_paths_bottom + count_paths_left + count_paths_right