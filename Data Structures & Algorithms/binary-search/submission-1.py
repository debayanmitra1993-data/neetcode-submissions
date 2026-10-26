class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lidx, ridx = 0, len(nums) - 1

        while lidx <= ridx:
            midx = (lidx + ridx) // 2
            if nums[midx] == target:
                return midx
            elif target > nums[midx]:
                lidx = midx + 1
            elif target < nums[midx]:
                ridx = midx - 1

        return -1          