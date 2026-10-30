class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = [0]*len(nums)
        maxsub[0] = nums[0]

        for idx in range(1, len(nums)):
            maxsub[idx] = max(
                nums[idx],
                nums[idx] + maxsub[idx - 1]
            )
        
        maxsofar = maxsub[0]
        for idx in range(1, len(maxsub)):
            if maxsub[idx] > maxsofar:
                maxsofar = maxsub[idx]
        return maxsofar