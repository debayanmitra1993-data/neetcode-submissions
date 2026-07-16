class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumsum = [0]*(len(nums) + 1)
        for idx in range(1, len(cumsum)):
            cumsum[idx] = cumsum[idx - 1] + nums[idx - 1]
        
        numstore = {}
        cnt = 0
        for idx in range(len(cumsum)):
            ele = cumsum[idx]
            if ele - k in numstore:
                cnt += numstore[ele - k]
            
            if ele not in numstore:
                numstore[ele] = 0
            numstore[ele] += 1
        return cnt

