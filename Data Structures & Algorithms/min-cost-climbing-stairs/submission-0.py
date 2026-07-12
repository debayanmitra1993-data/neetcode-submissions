class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincostdp = [0]*len(cost)

        for idx in range(2, len(mincostdp)):
            mincostdp[idx] = min(
                mincostdp[idx - 1] + cost[idx - 1],
                mincostdp[idx - 2] + cost[idx - 2]
            )
        
        return min(
            mincostdp[-1] + cost[-1],
            mincostdp[-2] + cost[-2]
        )
        