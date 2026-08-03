class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        res = 1
        for _ in range(abs(n)):
            res = res * x
        return res if n > 0 else 1/res