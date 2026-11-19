class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        allsubsets = {}
        path = []
        self.recursiontree(nums, path, allsubsets, 0)
        return [list(k) for k,v in allsubsets.items()]
        
    
    def recursiontree(self, nums, path, allsubsets, curridx):
        if curridx == len(nums):
            if tuple(path) not in allsubsets:
                allsubsets[tuple(path)] = True
            return

        # choose ele
        ele = nums[curridx]
        path.append(ele)
        self.recursiontree(nums, path, allsubsets, curridx + 1)

        # do not choose ele
        path.pop()
        self.recursiontree(nums, path, allsubsets, curridx + 1)



        