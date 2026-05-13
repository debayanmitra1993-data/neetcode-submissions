class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        for idx in range(len(nums)):
            num = nums[idx]

            if target - num in store:
                return [store[target - num], idx]
            else:
                store[num] = idx 
        