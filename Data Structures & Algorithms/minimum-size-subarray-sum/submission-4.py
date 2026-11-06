class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        minlength = float("inf")
        subarrsum = nums[0]

        while True:

            if subarrsum < target:
                j += 1
                if j > len(nums) - 1:
                    break
                else:
                    subarrsum += nums[j]
            elif subarrsum >= target:
                if j - i + 1 < minlength:
                    minlength = j - i + 1
                i += 1
                subarrsum -= nums[i - 1]
            
            if i > j:
                j = i
                if j > len(nums) - 1:
                    break

        

        return minlength if minlength != float("inf") else 0      