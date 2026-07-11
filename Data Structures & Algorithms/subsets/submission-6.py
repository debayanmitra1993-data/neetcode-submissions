class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        currstack = []
        allsubsets = []
        self.dfs(0, currstack, nums, allsubsets)
        print("allsubsets = ", allsubsets)
        return allsubsets
    
    def dfs(self, idx, currstack, nums, allsubsets):
        if idx == len(nums):
            allsubsets.append(currstack.copy())
            return 
        
        # include nums[idx]
        currstack.append(nums[idx]) 
        self.dfs(idx + 1, currstack, nums, allsubsets)

        # exclude nums[idx]
        currstack.pop()
        self.dfs(idx + 1, currstack, nums, allsubsets)
        