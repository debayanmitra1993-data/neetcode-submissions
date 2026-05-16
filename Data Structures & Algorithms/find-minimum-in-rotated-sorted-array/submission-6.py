class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # case where array is rotated len(array) times, hence its already sorted..
        if nums[0] <= nums[1] and nums[0] <= nums[-1]:
            return nums[0]
        
        
        leftidx, rightidx = 0, len(nums) - 1 
        while leftidx < rightidx:
            mididx = (leftidx + rightidx)//2

            if leftidx == mididx or rightidx == mididx:
                return min(nums[leftidx], nums[rightidx])
            
            if nums[mididx] < nums[mididx - 1]:
                return nums[mididx]
            else:
                if nums[mididx] > nums[0]:
                    leftidx = mididx
                elif nums[mididx] < nums[0]:
                    rightidx = mididx
        