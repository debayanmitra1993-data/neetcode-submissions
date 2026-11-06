class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        store = {}
        cumsum = [0]*len(nums)
        cumsum[0] = nums[0]
        for idx in range(1, len(cumsum)):
            cumsum[idx] = cumsum[idx - 1] + nums[idx]

        for idx in range(len(cumsum)):
            ele = cumsum[idx]
            if ele == k:
                cnt += 1
            
            if ele - k in store:
                cnt += store[ele - k]
            
            if ele not in store:
                store[ele] = 0
            store[ele] += 1
        
        return cnt