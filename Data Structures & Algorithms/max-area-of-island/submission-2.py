class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = float("-inf")
        visited = set()
        for rowidx in range(len(grid)):
            for colidx in range(len(grid[rowidx])):
                if grid[rowidx][colidx] == 1:
                    before_visited_len = len(visited)
                    visited = self.bfs(rowidx, colidx, grid, visited)
                    after_visited_len = len(visited)
                    area = after_visited_len - before_visited_len
                    if area > maxarea:
                        maxarea = area 
        return maxarea if maxarea != float("-inf") else 0

    def bfs(self, rowidx, colidx, grid, visited):
        bfsqueue = [(rowidx, colidx)]
        while len(bfsqueue) > 0:
            ele = bfsqueue.pop(0)
            if ele not in visited:
                visited.add(ele)
                rowidx, colidx = ele[0], ele[1]
            else:
                continue

            # check for valid children..
            if self.isvalididx(rowidx + 1, colidx, grid, visited):
                bfsqueue.append((rowidx + 1, colidx))
            if self.isvalididx(rowidx, colidx + 1, grid, visited):
                bfsqueue.append((rowidx, colidx + 1))
            if self.isvalididx(rowidx - 1, colidx, grid, visited):
                bfsqueue.append((rowidx - 1, colidx))
            if self.isvalididx(rowidx, colidx - 1, grid, visited):
                bfsqueue.append((rowidx, colidx - 1))
        
        return visited
            
    def isvalididx(self, rowidx, colidx, grid, visited):
        if rowidx < 0 or colidx < 0 or rowidx > len(grid) - 1 or colidx > len(grid[0]) - 1:
            return False 
        
        if grid[rowidx][colidx] == 0:
            return False 
        
        if (rowidx, colidx) in visited:
            return False 
        
        return True 




        