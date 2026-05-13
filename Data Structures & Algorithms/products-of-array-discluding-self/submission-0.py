class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mulval = 1
        zero_indices = {}
        for idx in range(len(nums)):
            if nums[idx] == 0:
                zero_indices[idx] = 0
            else:
                mulval = mulval * nums[idx] 
        
        output = [1]*len(nums)

        for idx in range(len(nums)):
            if len(zero_indices) > 0:
                if idx in zero_indices:
                    if len(zero_indices) > 1:
                        output[idx] = 0 
                    else:
                        output[idx] = mulval 
                else:
                    if len(zero_indices) > 0:
                        output[idx] = 0
                    else:
                        output[idx] = mulval//nums[idx]
            else:
                output[idx] = mulval//nums[idx]

        return output 

        