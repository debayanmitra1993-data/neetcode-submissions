class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        self.dfsbacktrack(0, output, [], nums)
        print("output = ", output)
        return output

    
    def dfsbacktrack(self, idx, output, currpath, nums):
        if idx > len(nums) - 1:
            if currpath not in output:
                output.append(currpath.copy())
            return 
        
        if idx <= len(nums) - 1:
            currpath.append(nums[idx])
            self.dfsbacktrack(idx + 1, output, currpath, nums)

            currpath.pop()
            self.dfsbacktrack(idx + 1, output, currpath, nums)