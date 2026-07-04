class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        store = [0]*3
        for ele in nums:
            store[ele] += 1
        
        ele = 0
        for idx in range(len(nums)):
            while store[ele] == 0:
                ele += 1 
            
            
            nums[idx] = ele
            store[ele] = store[ele] - 1 

        

            


        