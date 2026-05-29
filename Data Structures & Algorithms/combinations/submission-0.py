class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = []
        for i in range(1, n + 1):
            nums.append(i)
        print("nums = ", nums, "with k = ", k)
        return self.get_combinations(nums, k)
    
    def get_combinations(self, nums, k):
        if k == 1:
            return [[ele] for ele in nums]
            
        if k > len(nums):
            return []
        elif k == len(nums):
            return [nums]
        elif k < len(nums):
            allcombs = []
            for idx in range(len(nums) - k + 1):
                ele = nums[idx]
                remaining_arr = nums[idx + 1:]
                remaining_arr_combs = self.get_combinations(remaining_arr, k - 1)
                for comb in remaining_arr_combs:
                    currcomb = [ele] + comb
                    allcombs.append(currcomb)
            return allcombs
        