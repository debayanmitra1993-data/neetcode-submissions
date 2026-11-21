class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        dpmatrix = [[0 for _ in range(1 + amount)] for _ in range(len(coins))]
        for rowidx in range(len(dpmatrix)):
            dpmatrix[rowidx][0] = 1
        
        coin = coins[0]
        for colidx in range(len(dpmatrix[0])):
            if coin <= colidx and colidx % coin == 0:
                dpmatrix[0][colidx] = 1          
        
        for rowidx in range(1, len(dpmatrix)):
            coinval = coins[rowidx]
            for colidx in range(1, len(dpmatrix[rowidx])):
                if coinval <= colidx:
                    # include case + exclude case
                    val = dpmatrix[rowidx][colidx - coinval] + dpmatrix[rowidx - 1][colidx]
                    dpmatrix[rowidx][colidx] = val
                else:
                    dpmatrix[rowidx][colidx] = dpmatrix[rowidx - 1][colidx]     
        return dpmatrix[-1][-1]