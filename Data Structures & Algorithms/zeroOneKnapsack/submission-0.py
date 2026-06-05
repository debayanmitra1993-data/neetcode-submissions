class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp_matrix = [[0 for _ in range(capacity + 1)] for _ in range(len(profit) + 1)]

        for rowidx in range(1, len(dp_matrix)):
            for colidx in range(1, len(dp_matrix[rowidx])):
                item_wt = weight[rowidx - 1]
                item_profit = profit[rowidx - 1]
                curr_capacity = colidx
                if item_wt > curr_capacity:
                    dp_matrix[rowidx][colidx] = dp_matrix[rowidx - 1][colidx]
                elif item_wt <= curr_capacity:
                    dp_matrix[rowidx][colidx] = max(
                        dp_matrix[rowidx - 1][colidx],
                        dp_matrix[rowidx - 1][curr_capacity - item_wt] + item_profit
                    ) 
        return dp_matrix[-1][-1]