class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        store = {}
        cumsum = [0]*len(nums)
        cumsum[0] = nums[0]
        for idx in range(1, len(nums)):
            cumsum[idx] = cumsum[idx - 1] + nums[idx]

        store[cumsum[0]] = 0

        for idx in range(1, len(cumsum)):
            ele = cumsum[idx]

            if ele % k == 0 or ele == 0:
                return True 
            
            for beforeele in store.keys():
                if idx - store[beforeele] >= 2:
                    if (ele - beforeele) % k == 0 or ele == beforeele:
                        return True
            
            if ele not in store:
                store[ele] = idx
        
        return False
        