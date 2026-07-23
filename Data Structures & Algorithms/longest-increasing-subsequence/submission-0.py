class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dparr = [1]*len(nums)
        globalmaxsofar = 1
        for idx in range(len(nums) - 2, -1, -1):
            ele = nums[idx]
            maxsofar = dparr[idx]
            for jdx in range(idx + 1, len(nums)):
                if ele < nums[jdx]:
                    if dparr[jdx] + 1 > maxsofar:
                        maxsofar = dparr[jdx] + 1
            dparr[idx] = maxsofar
            if dparr[idx] > globalmaxsofar:
                globalmaxsofar = dparr[idx]
        return globalmaxsofar
        


        