class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dparr = [0]*(len(cost) + 1)
        
        for idx in range(2, len(dparr)):
            dparr[idx] = min(
                dparr[idx - 1] + cost[idx - 1],
                dparr[idx - 2] + cost[idx - 2]
            )
        
        return dparr[-1]