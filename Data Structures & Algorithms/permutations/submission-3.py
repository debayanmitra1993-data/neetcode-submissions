class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        allperms = []
        path = []
        self.recursiontree(nums, visited, allperms, path)
        return allperms
    
    def recursiontree(self, nums, visited, allperms, path):
        if len(path) == len(nums):
            allperms.append(path.copy())
            return

        for idx in range(len(nums)):
            if idx not in visited:
                visited.add(idx)
                path.append(nums[idx])
                self.recursiontree(nums, visited, allperms, path)
                path.pop()
                visited.remove(idx)
        



        