class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsubarr = [0]*len(nums)
        maxsubarr[0] = nums[0]
        maxsofar = maxsubarr[0]

        for idx in range(1, len(nums)):
            ele = nums[idx]
            maxsubarr[idx] = max(
                ele,
                ele + maxsubarr[idx - 1]
            )
            if maxsubarr[idx] > maxsofar:
                maxsofar = maxsubarr[idx]
        return maxsofar