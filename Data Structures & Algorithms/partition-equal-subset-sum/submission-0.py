class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        rs = 0
        for idx in range(len(nums)):
            rs += nums[idx]
        if rs % 2 != 0:
            return False
        
        boolchk = [False]
        self.combinationsum(nums, rs // 2, 0, 0, boolchk)
        return boolchk[0]
    

    def combinationsum(self, nums, target, idx, runningsum, boolchk):
        if runningsum == target:
            boolchk[0] = True
            return
        
        if boolchk[0] == True:
            return

        if idx <= len(nums) - 1:
            
            # include nums[idx]
            self.combinationsum(nums, target, idx + 1, runningsum + nums[idx], boolchk)

            # exclude nums[idx]
            self.combinationsum(nums, target, idx + 1, runningsum, boolchk)



