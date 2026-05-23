class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = [[]]
        for k in range(1, len(nums) + 1):
            getval = self.pick_combination_helper(nums, k)
            # print("getval = ", getval, " for k = ", k)
            for getvalcomb in getval:
                power_set.append(getvalcomb)
        return power_set
    
    # pick 'k' combinations from 'n' where k <= n
    def pick_combination_helper(self, nums, k):
        if k > len(nums):
            return []

        if k == len(nums):
            return [nums]

        if k == 1:
            output = []
            for ele in nums:
                output.append([ele])
            return output 
        elif k > 1:
            all_combs = []
            for i in range(len(nums) - k + 1):
                ele = [nums[i]]
                remain_arr_combs = self.pick_combination_helper(nums[i + 1:], k - 1)
                for comb in remain_arr_combs:
                    newcomb = ele + comb
                    all_combs.append(newcomb)
                    # print("all_combs = ", all_combs)
            return all_combs


        