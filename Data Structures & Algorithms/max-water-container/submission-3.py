class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lidx = 0
        ridx = len(heights) - 1
        maxarea = 0

        while lidx < ridx:
            area = min(heights[ridx], heights[lidx])*(ridx - lidx)
            if area > maxarea:
                maxarea = area
            if heights[lidx] <= heights[ridx]:
                lidx += 1 
            elif heights[lidx] > heights[ridx]:
                ridx -= 1 
        return maxarea