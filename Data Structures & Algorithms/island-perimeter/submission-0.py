class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        for rowidx in range(len(grid)):
            for colidx in range(len(grid[rowidx])):
                if grid[rowidx][colidx] == 1:
                    visited = set()
                    return self.dfs(rowidx, colidx, grid, visited)

    def dfs(self, rowidx, colidx, grid, visited):
        if (rowidx, colidx) in visited:
            return 0
        if rowidx < 0 or colidx < 0 or rowidx > len(grid) - 1 or colidx > len(grid[0]) - 1:
            return 1
        if grid[rowidx][colidx] == 0:
            return 1

        visited.add((rowidx, colidx))
        count_top = self.dfs(rowidx - 1, colidx, grid, visited)
        count_left = self.dfs(rowidx, colidx - 1, grid, visited)
        count_right = self.dfs(rowidx , colidx + 1, grid, visited)
        count_bottom = self.dfs(rowidx + 1, colidx, grid, visited)

        return count_top + count_left + count_right + count_bottom



        