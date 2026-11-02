class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dparray = [0]*(1 + capacity)

        for idx in range(1, len(dparray)):
            curr_capacity = idx
            maxval = 0
            for itemidx in range(len(weight)):
                item_profit = profit[itemidx]
                item_weight = weight[itemidx]
                if item_weight <= curr_capacity:
                    if item_profit + dparray[curr_capacity - item_weight] > maxval:
                        maxval = item_profit + dparray[curr_capacity - item_weight]
            dparray[idx] = maxval
        return dparray[-1]