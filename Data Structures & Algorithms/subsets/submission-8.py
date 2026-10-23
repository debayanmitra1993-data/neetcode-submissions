class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allsubsets = []
        path = []
        self.recursiontree(nums, allsubsets, path, 0)
        return allsubsets
    
    def recursiontree(self, nums, allsubsets, path, curridx):
        if curridx == len(nums):
            allsubsets.append(path.copy())
            return
        
        # choose ele
        ele = nums[curridx]
        path.append(ele)
        self.recursiontree(nums, allsubsets, path, curridx + 1)

        # do not choose ele
        path.pop()
        self.recursiontree(nums, allsubsets, path, curridx + 1)
        



        