class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dpmatrix = [[0 for _ in range(1 + capacity)] for _ in range(1 + len(weight))]

        for rowidx in range(1, len(dpmatrix)):
            item_weight = weight[rowidx - 1]
            item_profit = profit[rowidx - 1]
            for colidx in range(1, len(dpmatrix[rowidx])):
                current_capacity = colidx
                if item_weight > current_capacity:
                    dpmatrix[rowidx][colidx] = dpmatrix[rowidx - 1][colidx]
                elif item_weight <= current_capacity:
                    dpmatrix[rowidx][colidx] = max(
                        item_profit + dpmatrix[rowidx - 1][colidx - item_weight],
                        dpmatrix[rowidx - 1][colidx]
                    )
        return dpmatrix[-1][-1]