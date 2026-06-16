class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_arr = len(nums)
        indices = {}
        for idx in range(len(nums)):
            indices[idx] = nums[idx]
        
        for idx in range(len(nums)):
            newidx = (idx + k) % len_arr
            nums[newidx] = indices[idx]
        return nums