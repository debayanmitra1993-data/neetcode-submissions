class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        output = []
        self.recursiontree(nums, target, path, output, 0)
        return output
    
    def recursiontree(self, nums, target, path, output, idx):
        if target == 0:
            output.append(path.copy())
            return  

        for thisidx in range(idx, len(nums)):
            ele = nums[thisidx]
            if ele <= target:
                path.append(ele)
                self.recursiontree(nums, target - ele, path, output, thisidx)
                path.pop()
        

        