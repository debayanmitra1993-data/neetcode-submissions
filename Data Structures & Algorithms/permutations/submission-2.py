class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        outputperms = []
        lst = []
        visited = set()
        self.recursiontree(outputperms, lst, visited, nums)
        return outputperms
    
    def recursiontree(self, outputperms, lst, visited, nums):
        if len(visited) == len(nums):
            outputperms.append(lst.copy())
            return 
        
        for idx in range(len(nums)):
            if idx not in visited:
                visited.add(idx)
                lst.append(nums[idx])
                self.recursiontree(outputperms, lst, visited, nums)
                lst.pop()
                visited.remove(idx)


                
        
        
        