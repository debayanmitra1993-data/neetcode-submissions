class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dparr = [0]*(capacity + 1)

        for idx in range(1, len(dparr)):
            curr_capacity = idx

            maxprofit = 0
            for itemidx in range(len(profit)):
                item_profit = profit[itemidx]
                item_wt = weight[itemidx]
                if item_wt <= curr_capacity:
                    maxprofit = max(
                        maxprofit, 
                        item_profit + dparr[curr_capacity - item_wt]
                    )
            dparr[idx] = maxprofit
        return dparr[-1]
