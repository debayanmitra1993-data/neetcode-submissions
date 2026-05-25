class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_oranges = set()
        rotten_oranges = set()
        for rowidx in range(len(grid)):
            for colidx in range(len(grid[rowidx])):
                if grid[rowidx][colidx] == 2:
                    rotten_oranges.add((rowidx, colidx))
                if grid[rowidx][colidx] == 1:
                    fresh_oranges.add((rowidx, colidx))
        
        minutes = 0
        

        while True:
            
            oranges_that_will_rot_this_min = set()
            for rotten_orange in rotten_oranges:
                rowidx, colidx = rotten_orange[0], rotten_orange[1]
                if self.isvalidfreshorange(rowidx + 1, colidx, grid, oranges_that_will_rot_this_min):
                    oranges_that_will_rot_this_min.add((rowidx + 1, colidx))
                if self.isvalidfreshorange(rowidx - 1, colidx, grid, oranges_that_will_rot_this_min):
                    oranges_that_will_rot_this_min.add((rowidx - 1, colidx))
                if self.isvalidfreshorange(rowidx, colidx + 1, grid, oranges_that_will_rot_this_min):
                    oranges_that_will_rot_this_min.add((rowidx, colidx + 1))
                if self.isvalidfreshorange(rowidx, colidx - 1, grid, oranges_that_will_rot_this_min):
                    oranges_that_will_rot_this_min.add((rowidx, colidx - 1))
            print("oranges that will rot in this min = ", oranges_that_will_rot_this_min)
            
            if len(oranges_that_will_rot_this_min) == 0:
                break 
            
            # rotten up the oranges..
            for fresh_orange in oranges_that_will_rot_this_min:
                rowidx, colidx = fresh_orange[0], fresh_orange[1]
                fresh_oranges.remove((rowidx, colidx))
                rotten_oranges.add((rowidx, colidx))
                grid[rowidx][colidx] = 2 
            
            minutes += 1 
            print("after minutes = ", minutes, " grid looks like = ", grid)
        
        print("minutes = ", minutes)
        print("fresh oranges = ", fresh_oranges)
        if len(fresh_oranges) == 0:
            return minutes
        else:
            return -1

            

    def isvalidfreshorange(self, rowidx, colidx, grid, visited):
        if rowidx < 0 or colidx < 0 or rowidx > len(grid) - 1 or colidx > len(grid[0]) - 1:
            return False 

        if (rowidx, colidx) in visited:
            return False 

        if grid[rowidx][colidx] == 1:
            return True          
