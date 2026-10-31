class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minarray = [0]*len(nums)
        maxarray = [0]*len(nums)

        minarray[0] = nums[0]
        maxarray[0] = nums[0]

        for idx in range(1, len(nums)):
            ele = nums[idx]

            if ele == 0:
                minarray[idx] = 0
                maxarray[idx] = 0
                continue
            
            if nums[idx - 1] == 0:
                minarray[idx] = nums[idx]
                maxarray[idx] = nums[idx]
                continue

            minarray[idx] = min(
                ele, 
                ele * minarray[idx - 1], 
                ele * maxarray[idx - 1]
            )

            maxarray[idx] = max(
                ele, 
                ele * maxarray[idx - 1], 
                ele * minarray[idx - 1]
            )
        
        maxval = maxarray[0]
        for idx in range(1, len(nums)):
            if maxarray[idx] > maxval:
                maxval = maxarray[idx]
        return maxval