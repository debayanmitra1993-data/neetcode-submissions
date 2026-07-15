class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxk = 0
        for pile in piles:
            if pile > maxk:
                maxk = pile
        
        left_k = 1
        right_k = maxk

        if self.get_hour_given_k(1, piles) <= h:
            return 1
        
        while left_k <= right_k:
            mid_k = (left_k + right_k)//2
            mid_h = self.get_hour_given_k(mid_k, piles)
            if mid_h <= h:
                res = mid_k
                right_k = mid_k - 1
            elif mid_h > h:
                left_k = mid_k + 1
            
        return res

    
    def get_hour_given_k(self, k, piles):
        tot_hour = 0
        for pile in piles:
            if pile % k == 0:
                tot_hour += pile // k 
            else:
                tot_hour += (pile // k) + 1
        return tot_hour


        