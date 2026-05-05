class Solution:
    def climbStairs(self, n: int) -> int:
        return self.helper2(n)
    
    def helper(self, n):
        if n == 1 or n == 0:
            return 1
        else:
            return self.helper(n - 1) + self.helper(n - 2)
    
    def helper2(self, n):
        array = [1]*(n + 1)
        for idx in range(2, len(array)):
            array[idx] = array[idx - 1] + array[idx - 2]
        return array[-1]
        