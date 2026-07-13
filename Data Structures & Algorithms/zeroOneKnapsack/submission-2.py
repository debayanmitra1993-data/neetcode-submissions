class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dpmatrix = [[0 for _ in range(capacity + 1)] for _ in range(len(profit))]

        for rowidx in range(len(dpmatrix)):
            for colidx in range(len(dpmatrix[rowidx])):
                if rowidx == 0:
                    if weight[rowidx] <= colidx:
                        dpmatrix[rowidx][colidx] = profit[rowidx]
                    else:
                        dpmatrix[rowidx][colidx] = 0
                else:
                    if weight[rowidx] <= colidx:
                        dpmatrix[rowidx][colidx] = max(
                            dpmatrix[rowidx - 1][colidx],
                            dpmatrix[rowidx - 1][colidx - weight[rowidx]] + profit[rowidx]
                        )
                    else:
                        dpmatrix[rowidx][colidx] = dpmatrix[rowidx - 1][colidx]
        return dpmatrix[-1][-1]



