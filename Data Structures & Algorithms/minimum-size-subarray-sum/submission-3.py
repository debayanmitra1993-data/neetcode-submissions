class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lidx, ridx = 0, 0
        minsubarrsize = 0
        subarrsum = nums[0]
        if subarrsum >= target:
            minsubarrsize = 1

        while True:

            if subarrsum < target:
                if ridx + 1 <= len(nums) - 1:
                    ridx += 1
                    subarrsum += nums[ridx]
                else:
                    break  
            elif subarrsum >= target:
                if lidx + 1 <= len(nums) - 1:
                    lidx += 1
                    subarrsum -= nums[lidx - 1]
                    if lidx > ridx:
                        ridx = lidx
                        subarrsum = nums[ridx]
                else:
                    break
            
            if subarrsum >= target:
                if minsubarrsize == 0:
                    minsubarrsize = ridx - lidx + 1
                else:
                    if ridx - lidx + 1 < minsubarrsize:
                        minsubarrsize = ridx - lidx + 1
        
        return minsubarrsize
            



