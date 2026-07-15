class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxwt = 0
        sumwt = 0
        for wt in weights:
            sumwt += wt
            if wt > maxwt:
                maxwt = wt
        
        leftwt, rightwt = maxwt, sumwt
        
        while leftwt <= rightwt:
            midwt = (leftwt + rightwt)//2
            midwt_days = self.compute_days(midwt, weights)
            if midwt_days <= days:
                res = midwt
                rightwt = midwt - 1 
            else:
                leftwt = midwt + 1
        return res
    
    def compute_days(self, capacity, weights):
        days = 0
        runsum = 0
        for weight in weights:
            if runsum + weight < capacity:
                runsum = runsum + weight
            elif runsum + weight == capacity:
                days += 1 
                runsum = 0
            elif runsum + weight > capacity:
                days += 1
                runsum = weight 
        
        if runsum > 0:
            days += 1
        
        return days


        