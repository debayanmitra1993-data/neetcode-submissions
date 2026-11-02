class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        self.dfs(image, sr, sc, visited, image[sr][sc])
        for r,c in visited:
            image[r][c] = color
        return image
    
    def dfs(self, image, rowidx, colidx, visited, colorvalue):
        if rowidx < 0 or colidx < 0 or rowidx > len(image) - 1 or colidx > len(image[0]) - 1:
            return 
        if (rowidx, colidx) in visited:
            return 
        if image[rowidx][colidx] != colorvalue:
            return 
        
        visited.add((rowidx, colidx))
        self.dfs(image, rowidx+1, colidx, visited, colorvalue)
        self.dfs(image, rowidx-1, colidx, visited, colorvalue)
        self.dfs(image, rowidx, colidx+1, visited, colorvalue)
        self.dfs(image, rowidx, colidx-1, visited, colorvalue)        