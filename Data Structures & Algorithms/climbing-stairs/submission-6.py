class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        dparr = [0]*(n + 1)
        dparr[0] = 0
        dparr[1] = 1
        dparr[2] = 2

        for idx in range(3, len(dparr)):
            dparr[idx] = dparr[idx - 1] + dparr[idx - 2]
        return dparr[-1]
        