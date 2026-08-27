class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dfscache = [None]*(1 + target)
        dfscache[0] = 1
        return self.dfsrecursiontree(dfscache, nums, target)
    
    def dfsrecursiontree(self, dfscache, nums, target):
        if dfscache[target] is not None:
            return dfscache[target]
        
        if target < 0:
            return 0

        totcnt = 0
        for ele in nums:
            if ele <= target:
                if dfscache[target - ele] is None: 
                    totcnt += self.dfsrecursiontree(dfscache, nums, target - ele)
                else:
                    totcnt += dfscache[target - ele]
        dfscache[target] = totcnt
        return totcnt