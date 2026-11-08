class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        cumsum = [0]*len(nums)
        cumsum[0] = nums[0]
        maxlength = float("-inf")

        for idx in range(1, len(nums)):
            cumsum[idx] = cumsum[idx - 1] + nums[idx]
        
        store = {}

        for idx in range(len(cumsum)):
            cumsumval = cumsum[idx]
            if cumsumval == k:
                if maxlength < idx + 1:
                    maxlength = idx + 1
            
            if cumsumval - k in store:
                if idx - store[cumsumval - k] > maxlength:
                    maxlength = idx - store[cumsumval - k]
            
            if cumsumval not in store:
                store[cumsumval] = idx
        
        return maxlength if maxlength != float("-inf") else 0

