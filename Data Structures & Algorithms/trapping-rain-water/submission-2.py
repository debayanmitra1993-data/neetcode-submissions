class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = [0]*len(height)
        rightmax = [0]*len(height)

        leftmax[0] = height[0]
        rightmax[-1] = height[-1]

        for idx in range(1, len(height)):
            leftmax[idx] = max(
                height[idx],
                leftmax[idx - 1]
            )
        
        for idx in range(len(height) - 2, -1, -1):
            rightmax[idx] = max(
                height[idx],
                rightmax[idx + 1]
            )
        
        totw = 0
        for idx in range(1, len(height) - 1):
            minval = min(
                leftmax[idx - 1], 
                rightmax[idx + 1]
            )
            if height[idx] < minval:
                totw += (minval - height[idx])
        return totw
