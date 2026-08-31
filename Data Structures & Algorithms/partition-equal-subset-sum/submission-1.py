class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        rs = 0
        for idx in range(len(nums)):
            rs += nums[idx]
        if rs % 2 != 0:
            return False
        
        possible_sets = set()
        possible_sets.add(0)

        for idx in range(len(nums)):
            ele = nums[idx]
            iterate_sets = possible_sets.copy()
            for setval in iterate_sets:
                possible_sets.add(setval + ele)
        
        if rs // 2 in possible_sets:
            return True
        else:
            return False
