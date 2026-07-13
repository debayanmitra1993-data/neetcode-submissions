class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        store = {}
        for num in nums:
            if num not in store:
                store[num] = 0
            store[num] += 1
        
        ele = 1
        while ele in store:
            ele += 1
        return ele