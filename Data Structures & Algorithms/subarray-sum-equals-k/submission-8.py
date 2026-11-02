class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps = [0]*len(nums)
        ps[0] = nums[0]
        for idx in range(1, len(nums)):
            ps[idx] = nums[idx] + ps[idx - 1]
        
        cnt = 0
        store = {}
        for idx in range(len(ps)):
            ele = ps[idx]
            if ele == k:
                cnt += 1
            if ele - k in store:
                cnt += store[ele - k]
            
            if ele not in store:
                store[ele] = 0
            store[ele] += 1 

        return cnt

        
        