class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        outputs = []
        path = []
        self.recursiontree(0, nums, outputs, path)
        return outputs
    
    def recursiontree(self, idx, nums, outputs, path):
        if idx == len(nums):
            outputs.append(path.copy())
            return
        
        if idx > len(nums) - 1:
            return 
        
        path.append(nums[idx])
        self.recursiontree(idx + 1, nums, outputs, path)

        path.pop()
        self.recursiontree(idx + 1, nums, outputs, path)