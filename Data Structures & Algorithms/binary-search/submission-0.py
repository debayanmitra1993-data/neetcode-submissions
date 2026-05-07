class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftidx = 0
        rightidx = len(nums) - 1
        while leftidx <= rightidx:
            mididx = (leftidx + rightidx) // 2
            if nums[mididx] == target:
                return mididx
            elif target < nums[mididx]:
                rightidx = mididx - 1
            elif target > nums[mididx]:
                leftidx = mididx + 1
        return -1