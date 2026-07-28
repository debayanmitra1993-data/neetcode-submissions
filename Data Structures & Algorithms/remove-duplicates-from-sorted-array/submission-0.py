class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        i = 0
        j = 0

        while i < len(nums):
            j = i
            while j < len(nums):
                if j + 1 <= len(nums) - 1:
                    if nums[j + 1] == nums[i]:
                        j += 1
                    else:
                        break
                else:
                    break
            
            # assign
            nums[k] = nums[j]
            k += 1
            i = j + 1
        print("nums = ", nums)
        for popidx in range(len(nums) - 1, k-1, -1):
            nums.pop()
        return len(nums)