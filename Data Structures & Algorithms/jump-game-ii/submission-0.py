class Solution:
    def jump(self, nums: List[int]) -> int:
        dparr = [float("inf")]*len(nums)
        dparr[-1] = 0

        for idx in range(len(nums) - 2, -1, -1):
            maxjumps = nums[idx]
            for jump in range(1, maxjumps + 1):
                jumpdest = idx + jump
                if jumpdest <= len(nums) - 1:
                    dparr[idx] = min(
                        dparr[idx],
                        1 + dparr[jumpdest]
                    )
        return dparr[0]


        