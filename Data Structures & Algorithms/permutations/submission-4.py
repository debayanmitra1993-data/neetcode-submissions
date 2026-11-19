class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        outputs = []
        path = []
        self.recursiontree(nums, visited, outputs, path)
        return outputs
    
    def recursiontree(self, nums, visited, outputs, path):
        if len(path) == len(nums):
            outputs.append(path.copy())
            return

        for idx in range(len(nums)):
            if idx not in visited:
                visited.add(idx)
                path.append(nums[idx])
                self.recursiontree(nums, visited, outputs, path)
                visited.remove(idx)
                path.pop()