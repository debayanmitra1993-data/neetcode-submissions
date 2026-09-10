import math

class Solution:
    def numSquares(self, n: int) -> int:
        dparr = [1]*(n + 1)
        for idx in range(2, len(dparr)):
            num = idx
            x = math.sqrt(num)
            if math.floor(x) == x:
                dparr[num] = 1
            else:
                dparr[num] = float("inf")
                max_x = math.floor(x)
                for x in range(1, max_x + 1):
                    dparr[num] = min(
                        dparr[num], 
                        1 + dparr[num - (x**2)]
                    )
        return dparr[-1]