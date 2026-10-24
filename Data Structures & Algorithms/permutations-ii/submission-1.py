class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited = set()
        store = {}
        path = []
        allperms = []
        self.recursiontree(nums, visited, path, allperms, store)
        return allperms
    
    def recursiontree(self, nums, visited, path, allperms, store):
        if len(path) == len(nums):
            if tuple(path) not in store:
                store[tuple(path)] = True
                allperms.append(path.copy())
            return

        for idx in range(len(nums)):
            if idx not in visited:
                path.append(nums[idx])
                visited.add(idx)
                self.recursiontree(nums, visited, path, allperms, store)     
                visited.remove(idx)
                path.pop()

        