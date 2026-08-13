class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        if len(nums) == 2:
            if nums[0] == target:
                return 0
            if nums[1] == target:
                return 1
            return -1
        
        if nums[0] < nums[-1]:
            min_idx = 0
        else:
            min_idx = self.find_min_idx(nums)
        
        print("min_idx = ", min_idx)
        if target == nums[min_idx]:
            return min_idx

        if target < nums[-1]:
            # search between (min, len(nums) - 1)
            return self.binary_search(nums, min_idx, len(nums) - 1, target)
        elif target > nums[-1]:
            # search between (0, min - 1)
            return self.binary_search(nums, 0, min_idx - 1, target)
        elif target == nums[-1]:
            return len(nums) - 1
        
        return -1
    
    def binary_search(self, nums, l, r, target):
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
        return -1

    def find_min_idx(self, nums):
        l, r = 0, len(nums) - 1 
        while l <= r:
            m = (l + r) // 2 

            if m - 1 >= 0:
                if nums[m - 1] > nums[m]:
                    return m
            if m + 1 <= len(nums) - 1:
                if nums[m + 1] < nums[m]:
                    return m + 1
            
            if nums[m] < nums[0]:
                r = m - 1
            elif nums[m] > nums[0]:
                l = m + 1


        