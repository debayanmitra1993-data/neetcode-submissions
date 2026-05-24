class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        count_islands = 0
        for rowidx in range(len(grid)):
            for colidx in range(len(grid[rowidx])):
                if grid[rowidx][colidx] == "1" and (rowidx, colidx) not in visited:
                    print("entering bfs at = ",(rowidx, colidx))
                    self.bfs(grid, rowidx, colidx, visited)
                    print("visited = ", visited,"\n")
                    count_islands += 1 
        return count_islands
        

    
    def bfs(self, grid, rowidx, colidx, visited):
        bfsqueue = [(rowidx, colidx)]

        while len(bfsqueue) > 0:

            ele = bfsqueue.pop(0)
            # print("ele popped = ", ele)
            visited.add(ele)
            rowidx, colidx = ele[0], ele[1]

            # get children of this "ele"
            if self.isvalididx(grid, rowidx + 1, colidx, visited):
                bfsqueue.append((rowidx + 1, colidx))
            if self.isvalididx(grid, rowidx, colidx + 1, visited):
                bfsqueue.append((rowidx, colidx + 1))
            if self.isvalididx(grid, rowidx - 1, colidx, visited):
                bfsqueue.append((rowidx - 1, colidx))
            if self.isvalididx(grid, rowidx, colidx - 1, visited):
                bfsqueue.append((rowidx, colidx - 1))
            # print("bfsqueue = ", bfsqueue)
        return visited
    
    def isvalididx(self, grid, rowidx, colidx, visited):
        if rowidx < 0 or colidx < 0 or rowidx > len(grid) - 1 or colidx > len(grid[0]) - 1:
            return False 
        
        if grid[rowidx][colidx] == "0":
            return False 
        
        if (rowidx, colidx) in visited:
            return False 
        
        return True 