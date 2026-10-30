class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max1 = self.hr(nums[:len(nums) - 1])
        max2 = self.hr(nums[1:])

        return max(max1, max2)
    
    def hr(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dparr = [0]*len(nums)
        dparr[0] = nums[0]
        dparr[1] = max(nums[0], nums[1])

        for idx in range(2, len(nums)):
            dparr[idx] = max(
                dparr[idx - 1],
                dparr[idx - 2] + nums[idx]
            )
        return dparr[-1]
        