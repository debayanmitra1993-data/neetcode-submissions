class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        storedict = {}
        for ele in nums:
            if ele in storedict:
                return True
            else:
                storedict[ele] = True 
        return False 
        