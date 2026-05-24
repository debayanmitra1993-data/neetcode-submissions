class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        return self.dfs(grid, 0, 0, set(), num_rows, num_cols)
    
    def dfs(self, grid, rowidx, colidx, visited, num_rows, num_cols):
        if rowidx < 0 or colidx < 0 or rowidx > num_rows - 1 or colidx > num_cols - 1:
            return 0 
        
        if (rowidx, colidx) in visited:
            return 0
        
        if rowidx == num_rows - 1 and colidx == num_cols - 1:
            if grid[rowidx][colidx] == 0:
                return 1
            else:
                return 0
        
        if grid[rowidx][colidx] == 1:
            return 0

        visited.add((rowidx, colidx))


        count_ways_left = self.dfs(grid, rowidx, colidx - 1, visited, num_rows, num_cols)
        count_ways_right = self.dfs(grid, rowidx, colidx + 1, visited, num_rows, num_cols)
        count_ways_top = self.dfs(grid, rowidx - 1, colidx, visited, num_rows, num_cols)
        count_ways_bottom = self.dfs(grid, rowidx + 1, colidx, visited, num_rows, num_cols)

        visited.remove((rowidx, colidx))
        return count_ways_left + count_ways_right + count_ways_top + count_ways_bottom



