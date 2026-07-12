class Solution:
    def climbStairs(self, n: int) -> int:
        # Dynamic Programming solution..
        # memoization (repetitive sub-problems - compute and store)
        dp_arr = [0]*(n + 1)
        dp_arr[0] = 1
        dp_arr[1] = 1

        for idx in range(2, len(dp_arr)):
            dp_arr[idx] = dp_arr[idx - 1] + dp_arr[idx - 2]
        return dp_arr[-1]


        