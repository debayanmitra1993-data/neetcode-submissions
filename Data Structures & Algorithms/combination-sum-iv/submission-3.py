class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dparr = [0]*(1 + target)
        dparr[0] = 1

        for idx in range(1, len(dparr)):
            target = idx
            for num in nums:
                if num <= target:
                    dparr[idx] += dparr[target - num]
        return dparr[-1]