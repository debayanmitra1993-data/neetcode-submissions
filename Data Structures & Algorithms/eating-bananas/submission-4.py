import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # k = [1, 2, 3, 4, .....max(piles)]
        # k inversely proportional to hrs..
        # do a linear search, do a binary search...
        # go towards the minimum 'k' such that the hours is satisfied..
        mink = 1
        maxk = max(piles)
        optk = maxk

        while mink <= maxk:
            k = (mink + maxk)//2
            hrsk = self.hrstaken(k, piles)
            if hrsk > h:
                mink = k + 1
            elif hrsk <= h:
                maxk = k - 1
                if k < optk:
                    optk = k
        return optk

    def hrstaken(self, k, piles):
        hrs = 0
        for pile in piles:
            hrs += math.ceil(pile/k)
        return hrs