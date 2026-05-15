class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        store = {}
        for ele in nums:
            store[ele] = True 
        
        longest_len = float("-inf")
        minglobal, maxglobal = float("inf"), float("-inf")

        for idx in range(len(nums)):
            ele = nums[idx]

            if ele >= minglobal and ele <= maxglobal:
                continue 

            minval = ele
            maxval = ele
            while (ele - 1) in store:
                minval = min(minval, ele - 1)
                ele = ele - 1
            while (ele + 1) in store:
                maxval = max(maxval, ele + 1)
                ele = ele + 1
            
            if maxval - minval + 1 > longest_len:
                longest_len = maxval - minval + 1
                minglobal = minval
                maxglobal = maxval
        
        print("printing here = ",list(range(minglobal, maxglobal + 1, 1)))
        return longest_len
            

            

                
        
        