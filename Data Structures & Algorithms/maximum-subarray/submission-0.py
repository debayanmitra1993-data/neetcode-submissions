class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxtillhere = [0]*len(nums)
        maxtillhere[0] = nums[0]
        maxsum = maxtillhere[0]
        for i in range(1, len(nums)):
            maxtillhere[i] = max(maxtillhere[i - 1] + nums[i], nums[i])
            print("maxsum = ", maxsum)
            print("maxtillhere[i] = ", maxtillhere[i])
            maxsum = max(maxsum, maxtillhere[i])
        return maxsum

        