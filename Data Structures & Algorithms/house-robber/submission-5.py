class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        dparr = [0]*len(nums)
        dparr[0] = nums[0]
        dparr[1] = max(nums[0], nums[1])
        
        for idx in range(2, len(nums)):
            dparr[idx] = max(
                nums[idx] + dparr[idx - 2],
                dparr[idx - 1]
            )
        return dparr[-1]