class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        return Solution.dfshelper(grid, 0, 0, set())
    
    @staticmethod
    def dfshelper(grid, rowidx, colidx, visits):
        if rowidx < 0 or rowidx > len(grid) - 1 or colidx < 0 or colidx > len(grid[rowidx]) - 1 or grid[rowidx][colidx] == 1 or (rowidx, colidx) in visits:
            return 0 
        if rowidx == len(grid) - 1 and colidx == len(grid[rowidx]) - 1:
            return 1
        
        visits.add((rowidx, colidx))

        count = 0
        count = count + Solution.dfshelper(grid, rowidx - 1, colidx, visits)
        count = count + Solution.dfshelper(grid, rowidx, colidx - 1, visits)
        count = count + Solution.dfshelper(grid, rowidx + 1, colidx, visits)
        count = count + Solution.dfshelper(grid, rowidx, colidx + 1, visits)

        visits.remove((rowidx, colidx))
        return count

            
                

        