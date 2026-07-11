class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        currpath = set()
        allperms = []
        mystack = []
        self.dfs(nums, None, 0, currpath, mystack, allperms)
        return allperms
    
    def dfs(self, nums, ele, depth, currpath, mystack, allperms):
        if ele is not None:
            mystack.append(ele)
            currpath.add(ele)
        
        if depth >= len(nums):
            allperms.append(mystack.copy())
            # print("allperms = ", allperms)
            mystack.pop()
            currpath.remove(ele)
            return 

        for newele in nums:
            if newele not in currpath:
                self.dfs(nums, newele, depth + 1, currpath, mystack, allperms)
        
        if ele in currpath:
            currpath.remove(ele)
        if len(mystack) > 0:
            mystack.pop()

        