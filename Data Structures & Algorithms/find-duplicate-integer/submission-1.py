class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        store = {}
        for ele in nums:
            if ele in store:
                return ele
            store[ele] = True
        