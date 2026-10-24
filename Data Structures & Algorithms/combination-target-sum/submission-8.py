class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        out = []
        path = []
        self.recursiontree(nums, target, path, out, 0)
        return out
    
    def recursiontree(self, nums, target, path, out, idx):
        if target == 0:
            if len(path) > 0:
                out.append(path.copy())
            return 
        
        for thisidx in range(idx, len(nums)):
            ele = nums[thisidx]
            if target - ele >= 0:
                path.append(ele)
                self.recursiontree(nums, target - ele, path, out, thisidx)
                path.pop()
            else:
                break
