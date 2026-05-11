class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        maxsofararray = [0]*len(nums)
        maxsofararray[0], maxsofararray[1]  = nums[0], max(nums[1], nums[0])
        for i in range(2, len(nums)):
            maxsofararray[i] = max(
                maxsofararray[i - 1], 
                nums[i] + maxsofararray[i - 2]
            )
        return maxsofararray[-1]