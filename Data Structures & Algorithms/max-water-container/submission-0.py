class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = float("-inf")
        for idx in range(len(heights) - 1):
            for jdx in range(idx + 1, len(heights)):
                area = min(heights[jdx], heights[idx])
                area = area * (jdx - idx)
                maxarea = max(area, maxarea)
        return maxarea
        