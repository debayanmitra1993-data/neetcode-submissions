class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sums = self.populate_prefix_sum()
        print("prefix_sums = ", self.prefix_sums)

    def populate_prefix_sum(self):
        prefix_sum = [0]*len(self.nums)
        prefix_sum[0] = self.nums[0]
        for idx in range(1, len(self.nums)):
            prefix_sum[idx] = self.nums[idx] + prefix_sum[idx - 1]
        return prefix_sum

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sums[right]
        return self.prefix_sums[right] - self.prefix_sums[left - 1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)