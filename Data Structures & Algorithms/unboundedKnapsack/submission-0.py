class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp_arr = [0]*(capacity + 1)

        for curr_capacity in range(len(dp_arr)):

            maxval = 0
            for itemidx in range(len(weight)):
                item_wt = weight[itemidx]
                item_profit = profit[itemidx]

                if item_wt <= curr_capacity:
                    maxval = max(
                        maxval, 
                        item_profit + dp_arr[curr_capacity - item_wt]
                    )

            dp_arr[curr_capacity] = maxval
        
        return dp_arr[-1]