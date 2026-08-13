class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])
        if nums[0] < nums[-1]:
            return nums[0]

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            # if found...
            if m - 1 >= 0:
                if nums[m] < nums[m - 1]:
                    return nums[m]
            if m + 1 <= len(nums) - 1:
                if nums[m + 1] < nums[m]:
                    return nums[m + 1]
            
            
            if nums[m] < nums[0]:
                r = m - 1
            elif nums[m] > nums[0]:
                l = m + 1
                 

        