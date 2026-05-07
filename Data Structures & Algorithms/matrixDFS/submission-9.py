class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        return Solution.dfs(grid, 0, 0, set())
    
    @staticmethod
    def dfs(grid, rowidx, colidx, visits):
        if rowidx < 0 or colidx < 0 or rowidx >= len(grid) or colidx >= len(grid[rowidx]) or grid[rowidx][colidx] == 1 or (rowidx, colidx) in visits:
            return 0
        if rowidx == len(grid) - 1 and colidx == len(grid[rowidx]) - 1:
            return 1
        
        visits.add((rowidx, colidx))

        count = 0
        count = count + Solution.dfs(grid, rowidx + 1, colidx, visits)
        count = count + Solution.dfs(grid, rowidx, colidx + 1, visits)
        count = count + Solution.dfs(grid, rowidx - 1, colidx, visits)
        count = count + Solution.dfs(grid, rowidx, colidx - 1, visits)

        visits.remove((rowidx, colidx))

        return count 
        