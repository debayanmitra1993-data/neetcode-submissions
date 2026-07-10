class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        idx = 0
        runsum = 0
        while True:
            runsum += nums[idx]
            if runsum >= target:
                break 
            else:
                idx += 1
                if idx == len(nums):
                    return 0
        
        idx1 = 0
        idx2 = idx
        # print("init idx2 = ", idx2)
        minlensofar = idx2 - idx1 + 1 

        while True:

            if (runsum - nums[idx1]) >= target:
                idx1 += 1
                # print("idx1 = ",idx1, " and idx2 = ", idx2)
                runsum = runsum - nums[idx1 - 1]
                # print("runsum = ", runsum)
                # print("\n")
                if idx2 - idx1 + 1 < minlensofar:
                    minlensofar = idx2 - idx1 + 1  
            else:
                idx2 += 1 
                if idx2 == len(nums):
                    return minlensofar
                else:
                    runsum = runsum + nums[idx2]
                    # print("runsum = ", runsum)
                    if idx2 - idx1 + 1 < minlensofar:
                        minlensofar = idx2 - idx1 + 1 
        return minlensofar




        