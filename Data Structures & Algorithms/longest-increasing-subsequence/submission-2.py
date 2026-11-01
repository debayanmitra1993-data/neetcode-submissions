class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dparr = [1]*len(nums)

        for idx in range(len(dparr) - 2, -1, -1):

            num = nums[idx]
            for jdx in range(idx + 1, len(dparr)):
                if nums[jdx] > num:
                    dparr[idx] = max(dparr[idx], 1 + dparr[jdx])
                    
        print("dparr = ", dparr)
        maxval = 1
        for idx in range(len(dparr)):
            if dparr[idx] > maxval:
                maxval = dparr[idx]
        return maxval