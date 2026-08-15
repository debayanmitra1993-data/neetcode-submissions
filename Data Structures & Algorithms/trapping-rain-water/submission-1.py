class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = [0]*len(height)
        rightmax = [0]*len(height)

        for idx in range(1, len(height)):
            jdx = len(height) - 1 - idx 
            leftmax[idx] = max(leftmax[idx - 1], height[idx - 1])
            rightmax[jdx] = max(rightmax[jdx + 1], height[jdx + 1])
        # print("leftmax = ", leftmax)
        # print("rightmax = ", rightmax)     

        totwater = 0
        for idx in range(len(height)):
            if min(leftmax[idx], rightmax[idx]) - height[idx] > 0:
                totwater += min(leftmax[idx], rightmax[idx]) - height[idx]
        return totwater