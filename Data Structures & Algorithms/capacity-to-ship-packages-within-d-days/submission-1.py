class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # we can have ship capacity from 1, 2, .....26
        # max capacity = sum(weights) -> 1 day..
        # min capacity = 1 -> sum(weights) days..
        # as capacity increases, days decreases..so inverse relation... 
        # for each 'c' check -> days..and whether its within 'days' thres.

        minc = max(weights)
        maxc = sum(weights)
        optc = maxc

        while minc <= maxc:
            c = (minc + maxc) // 2 
            days_c = self.computedays(c, weights)
            if days_c > days:
                minc = c + 1
            elif days_c <= days:
                maxc = c - 1 
                if c < optc:
                    optc = c
        return optc
        
    def computedays(self, c, weights):

        days_taken = 0
        tot_wt_loaded = 0
        idx = 0
        while tot_wt_loaded < sum(weights) and idx < len(weights):
 
            weight_loaded = 0
            while weight_loaded < c and idx < len(weights):
                if weights[idx] <= (c - weight_loaded):
                    weight_loaded += weights[idx]
                    tot_wt_loaded += weights[idx]
                    idx += 1
                else:
                    break
            
            days_taken += 1
        return days_taken