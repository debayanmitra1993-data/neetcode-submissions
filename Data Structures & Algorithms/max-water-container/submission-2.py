class Solution:
    def maxArea(self, heights: List[int]) -> int:
        idx = 0
        jdx = len(heights) - 1 

        maxarea = float("-inf")
        while idx < jdx:
            print("idx = ", idx)
            print("jdx = ", jdx)
            area = (jdx - idx)*min(heights[jdx], heights[idx])
            if area > maxarea:
                maxarea = area 
            

            if heights[idx] < heights[jdx]:
                idx += 1
            else:
                jdx -= 1 
        return maxarea    