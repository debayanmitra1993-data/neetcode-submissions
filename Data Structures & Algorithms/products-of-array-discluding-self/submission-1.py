class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_cum_mul = [1]*len(nums)
        right_cum_mul = [1]*len(nums)

        left_cum_mul[0] = nums[0]
        for idx in range(1, len(left_cum_mul)):
            left_cum_mul[idx] = left_cum_mul[idx - 1]*nums[idx]

        right_cum_mul[len(nums) - 1] = nums[len(nums) - 1]
        for idx in range(len(right_cum_mul) - 2, -1, -1):
            right_cum_mul[idx] = right_cum_mul[idx + 1]*nums[idx]
        
        output = [1]*len(nums)

        for idx in range(len(output)):
            if idx == 0:
                output[idx] = right_cum_mul[idx + 1]
            elif idx == len(nums) - 1:
                output[idx] = left_cum_mul[idx - 1]
            else:
                output[idx] = left_cum_mul[idx - 1] * right_cum_mul[idx + 1]
        
        return output

        

        