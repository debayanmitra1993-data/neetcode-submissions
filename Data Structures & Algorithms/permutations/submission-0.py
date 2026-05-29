class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.funcperms(nums)
    
    def funcperms(self, nums):
        if len(nums) == 1:
            return [nums]
        elif len(nums) == 2:
            return [nums, [nums[1], nums[0]]]
        elif len(nums) > 2:
            allperms = []
            for idx in range(len(nums)):
                ele = nums[idx]
                remaining_arr = nums[:idx] + nums[idx + 1:]
                perms_remaining_arr = self.funcperms(remaining_arr)
                for perm in perms_remaining_arr:
                    finalperm = [ele] + perm
                    allperms.append(finalperm)
            return allperms




        