class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        outputs = []
        self.recursiontree(nums, 0, path, outputs)
        return outputs
    
    def recursiontree(self, nums, idx, path, outputs):
        if idx == len(nums):
            outputs.append(path.copy())
            return 

        # include ele
        ele = nums[idx]
        path.append(ele)
        self.recursiontree(nums, idx + 1, path, outputs)
        

        # exclude ele
        path.pop()
        self.recursiontree(nums, idx + 1, path, outputs)

        