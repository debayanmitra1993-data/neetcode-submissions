class Solution:
    def isHappy(self, n: int) -> bool:
        store = {}
        thisnum = n
        while True:
            thisnum = self.compute_sum_squares(thisnum)
            if thisnum == 1:
                return True
            else:
                if thisnum in store:
                    return False
                store[thisnum] = True
    
    def compute_sum_squares(self, n):
        sum_sq = 0
        while n > 0:
            rem = n % 10
            sum_sq += (rem*rem)
            n = n // 10
        return sum_sq


        