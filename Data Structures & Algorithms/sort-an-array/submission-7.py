class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        minval = float("inf")
        for ele in nums:
            if ele < minval:
                minval = ele 
        
        readjust = 0
        if minval < 0:
            readjust = abs(minval)
        
        nums = [x + readjust for x in nums]

        maxval = 0
        for ele in nums:
            maxval = max(maxval, ele)
        countarr = [0]*(maxval + 1)
        
        for ele in nums:
            countarr[ele] += 1
        
        cumarr = [countarr[0]]*len(countarr)
        for idx in range(1, len(cumarr)):
            cumarr[idx] = cumarr[idx - 1] + countarr[idx]
        
        sortedarr = [0]*len(nums)

        for idx in range(len(nums) - 1, -1, -1):
            ele = nums[idx]
            idx_to_place = cumarr[ele] - 1
            sortedarr[idx_to_place] = ele
            cumarr[ele] -= 1


        return [x - readjust for x in sortedarr]
        


        