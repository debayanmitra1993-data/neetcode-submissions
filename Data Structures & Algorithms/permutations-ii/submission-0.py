class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        out = []
        self.dfsbacktrack(visited, [], out, -1, nums)
        print("out = ", out)
        return out
    
    def dfsbacktrack(self, visited, path, out, idx, nums):
        if idx != -1:
            visited.add(idx)
            path.append(nums[idx])

        for cidx in range(len(nums)):
            if cidx not in visited:
                self.dfsbacktrack(visited, path, out, cidx, nums)
        
        if len(visited) == len(nums):
            if path not in out:
                out.append(path.copy())
        
        if idx in visited:
            visited.remove(idx)
        if len(path) > 0:
            path.pop()