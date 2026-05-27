class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i in range(min(k + 1, len(nums))):
            ele = nums[i]
            if ele in hashmap:
                return True
            else:
                hashmap[ele] = True 
        
        for i in range(k + 1, len(nums)):
            idx_to_del = i - k - 1
            ele = nums[idx_to_del]
            del hashmap[ele]

            ele = nums[i]
            if ele in hashmap:
                return True
            else:
                hashmap[ele] = True 
        
        return False 

        