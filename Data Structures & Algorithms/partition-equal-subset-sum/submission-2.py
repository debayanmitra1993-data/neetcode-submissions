class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        possible_sums = set()

        for ele in nums:
            iterate_subsets = possible_sums.copy()
            for poss_sum in iterate_subsets:
                possible_sums.add(ele + poss_sum)
            possible_sums.add(ele)
        
        if sum(nums) // 2 in possible_sums:
            return True
        else:
            return False