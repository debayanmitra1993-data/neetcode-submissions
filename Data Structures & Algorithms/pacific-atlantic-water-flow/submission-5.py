class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        visited = set()
        for colidx in range(len(heights[0])):
            pacific.add((0, colidx))
            visited.add((0, colidx))
        for rowidx in range(len(heights)):
            pacific.add((rowidx, 0))
            visited.add((rowidx, 0))
        
        for rowidx in range(1, len(heights)):
            for colidx in range(1, len(heights[rowidx])):
                self.dfs(rowidx, colidx, heights, visited, pacific)
        # print("pacific set = ", pacific)

        atlantic = set()
        visited = set()
        for colidx in range(len(heights[0])):
            atlantic.add((len(heights) - 1, colidx))
            visited.add((len(heights) - 1, colidx))
        for rowidx in range(len(heights)):
            atlantic.add((rowidx, len(heights[0]) - 1))
            visited.add((rowidx, len(heights[0]) - 1))
        
        for rowidx in range(len(heights) - 1):
            for colidx in range(len(heights[rowidx]) - 1):
                self.dfs(rowidx, colidx, heights, visited, atlantic)
        # print("atlantic set = ", atlantic)

        # print("intersection set = ", atlantic.intersection(pacific))
        return list(atlantic.intersection(pacific))

    
    def dfs(self, rowidx, colidx, heights, visited, ocean):
        # print("ENTERING DFS AT r, c, = ",rowidx, colidx)
        if (rowidx, colidx) in visited:
            if (rowidx, colidx) in ocean:
                return True
            else:
                return False 
        
        can_flow_ocean_bool = False
        visited.add((rowidx, colidx))
        
        # TOP
        if self.checkvalididx(rowidx, colidx, rowidx - 1, colidx, heights):
            can_flow_ocean_bool = self.dfs(rowidx - 1, colidx, heights, visited, ocean)
            if can_flow_ocean_bool:
                visited.add((rowidx, colidx))
                ocean.add((rowidx, colidx))
                return True
        
        # BOTTOM
        if self.checkvalididx(rowidx, colidx, rowidx + 1, colidx, heights):
            can_flow_ocean_bool = self.dfs(rowidx + 1, colidx, heights, visited, ocean)
            if can_flow_ocean_bool:
                visited.add((rowidx, colidx))
                ocean.add((rowidx, colidx))
                return True
        
        # LEFT
        if self.checkvalididx(rowidx, colidx, rowidx, colidx - 1, heights):
            can_flow_ocean_bool = self.dfs(rowidx, colidx - 1, heights, visited, ocean)
            if can_flow_ocean_bool:
                visited.add((rowidx, colidx))
                ocean.add((rowidx, colidx))
                return True
        
        # RIGHT
        if self.checkvalididx(rowidx, colidx, rowidx, colidx + 1, heights):
            can_flow_ocean_bool = self.dfs(rowidx, colidx + 1, heights, visited, ocean)
            if can_flow_ocean_bool:
                visited.add((rowidx, colidx))
                ocean.add((rowidx, colidx))
                return True
        
        
        return can_flow_ocean_bool
        
    def checkvalididx(self, curr_rowidx, curr_colidx, new_rowidx, new_colidx, heights):
        if new_rowidx < 0 or new_rowidx > len(heights) - 1 or new_colidx < 0 or new_colidx > len(heights[0]) - 1:
            return False
        
        if heights[new_rowidx][new_colidx] <= heights[curr_rowidx][curr_colidx]:
            return True 
        else:
            return False 