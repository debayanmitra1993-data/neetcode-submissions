class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visited = set()
        return self.dfstree(grid, 0, 0, visited)
    
    def dfstree(self, grid, rowidx, colidx, visited):
        if rowidx < 0 or colidx < 0 or rowidx > len(grid) - 1 or colidx > len(grid[0]) - 1:
            return 0
        if grid[rowidx][colidx] == 1:
            return 0
        if (rowidx, colidx) in visited:
            return 0
        if rowidx == len(grid) - 1 and colidx == len(grid[0]) - 1:
            return 1

        visited.add((rowidx, colidx))
        count_left = self.dfstree(grid, rowidx, colidx - 1, visited)
        count_right = self.dfstree(grid, rowidx, colidx + 1, visited)
        count_top = self.dfstree(grid, rowidx - 1, colidx, visited)
        count_bottom = self.dfstree(grid, rowidx + 1, colidx, visited)
        visited.remove((rowidx, colidx))

        return count_left + count_right + count_top + count_bottom

        