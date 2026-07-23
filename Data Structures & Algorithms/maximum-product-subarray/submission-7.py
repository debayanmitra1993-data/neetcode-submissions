class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxarr = [0]*len(nums)
        minarr = [0]*len(nums)
        maxarr[0] = nums[0]
        minarr[0] = nums[0]
        maxsofar = nums[0]
        if nums[0] == 0:
            iszero = True
        else:
            iszero = False

        for idx in range(1, len(nums)):
            ele = nums[idx]
            if ele == 0:
                maxarr[idx], minarr[idx] = 0, 0
                iszero = True
            else:
                if iszero == True:
                    maxarr[idx], minarr[idx] = nums[idx], nums[idx]
                    iszero = False
                else:
                    maxarr[idx] = max(
                        ele, ele * maxarr[idx - 1], ele * minarr[idx - 1]
                    )
                    minarr[idx] = min(
                        ele, ele * maxarr[idx - 1], ele * minarr[idx - 1]
                    )
            
            if maxarr[idx] > maxsofar:
                maxsofar = maxarr[idx]
        return maxsofar

        