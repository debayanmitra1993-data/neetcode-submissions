class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        max1 = self.gethouserobber(nums[:len(nums) - 1])
        max2 = self.gethouserobber(nums[1:])
        return max(max1, max2)

    def gethouserobber(self, arr):
        maxarr = [0]*len(arr)
        maxarr[0] = arr[0]
        maxarr[1] = max(arr[0], arr[1])

        for idx in range(2, len(arr)):
            maxarr[idx] = max(
                maxarr[idx - 1], 
                maxarr[idx - 2] + arr[idx]
            )
        return maxarr[-1]
        