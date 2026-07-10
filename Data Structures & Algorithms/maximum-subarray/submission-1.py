class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = [0]*len(nums)
        maxsum[0] = nums[0]
        
        for idx in range(1, len(nums)):
            maxsum[idx] = max(maxsum[idx - 1] + nums[idx], nums[idx])
        
        maxsofar = float("-inf")
        for ele in maxsum:
            if ele > maxsofar:
                maxsofar = ele
        return maxsofar