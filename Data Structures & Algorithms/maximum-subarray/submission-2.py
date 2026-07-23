class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxarr = [0]*len(nums)
        maxarr[0] = nums[0]
        maxsofar = maxarr[0]
        for idx in range(1, len(nums)):
            ele = nums[idx]
            maxarr[idx] = max(
                ele, 
                ele + maxarr[idx - 1]
            )
            if maxarr[idx] > maxsofar:
                maxsofar = maxarr[idx]
        return maxsofar
        
        