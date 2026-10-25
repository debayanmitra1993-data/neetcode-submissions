class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxarea = 0
        for rowidx in range(len(grid)):
            for colidx in range(len(grid[rowidx])):
                if (rowidx, colidx) not in visited and grid[rowidx][colidx] == 1:
                    area = self.dfsrecursion(rowidx, colidx, grid, visited)
                    if area > maxarea:
                        maxarea = area
        return maxarea
    
    def dfsrecursion(self, rowidx, colidx, grid, visited):
        if rowidx < 0 or colidx < 0 or rowidx > len(grid) - 1 or colidx > len(grid[0]) - 1:
            return 0
        if (rowidx, colidx) in visited:
            return 0
        if grid[rowidx][colidx] == 0:
            return 0
        
        visited.add((rowidx, colidx))
        count = 1
        count += self.dfsrecursion(rowidx + 1, colidx, grid, visited)
        count += self.dfsrecursion(rowidx - 1, colidx, grid, visited)
        count += self.dfsrecursion(rowidx, colidx + 1, grid, visited)
        count += self.dfsrecursion(rowidx, colidx - 1, grid, visited)

        return count



        