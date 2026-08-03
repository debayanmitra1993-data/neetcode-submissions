class Solution:
    def myPow(self, x: float, n: int) -> float:
        chkval = self.recursion(x, abs(n))
        if n == 0:
            return 1
        elif n > 0:
            return chkval
        else:
            return 1/chkval
        
    def recursion(self, x, n):
        if x == 0:
            return 0
        
        if n == 0:
            return 1
        elif n == 1:
            return x
        
        if n % 2 == 0:
            res = self.recursion(x, n // 2)
            return res*res
        else:
            res = self.recursion(x, n // 2)
            return res * res * x