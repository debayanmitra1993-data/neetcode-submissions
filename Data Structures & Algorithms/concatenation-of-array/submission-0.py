class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        len_arr = len(nums)
        for idx in range(len_arr):
            nums.append(nums[idx])
        return nums