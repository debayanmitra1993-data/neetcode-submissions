class Solution:
    def canJump(self, nums: List[int]) -> bool:
        boolarr = [False]*len(nums)
        boolarr[-1] = True 

        for idx in range(len(nums) - 2, -1, -1):
            if nums[idx] == 0:
                boolarr[idx] = False 
            else:
                for jumpval in range(nums[idx], 0, -1):
                    if idx + jumpval < len(nums):
                        boolarr[idx] = boolarr[idx + jumpval]
                        if boolarr[idx] == True:
                            break 
            #print("boolarr = ", boolarr, "at idx = ", idx)
        #print("boolarr[0] = ", boolarr[0])
        return boolarr[0]
  