class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        outputlst = []
        lst = []
        self.recursiontree(0, nums, lst, outputlst)
        return outputlst

    def recursiontree(self, curridx, nums, lst, outputlst):
        if curridx > len(nums) - 1:
            outputlst.append(lst.copy())
            return 
        
        # include the nums[curridx]
        lst.append(nums[curridx])
        self.recursiontree(curridx + 1, nums, lst, outputlst)

        # exclude the nums[curridx]
        lst.pop()
        self.recursiontree(curridx + 1, nums, lst, outputlst)