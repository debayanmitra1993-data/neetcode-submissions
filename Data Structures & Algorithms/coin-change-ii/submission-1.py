class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dparr = [[0 for _ in range(1 + amount)] for _ in range(len(coins))]
        
        dparr[0][0] = 1
        for colidx in range(1, len(dparr[0])):
            if colidx % coins[0] == 0:
                dparr[0][colidx] = 1
        
        for rowidx in range(1, len(dparr)):
            coin = coins[rowidx]
            for colidx in range(len(dparr[rowidx])):
                if colidx == 0:
                    dparr[rowidx][colidx] = 1
                else:
                    if colidx < coin:
                        dparr[rowidx][colidx] = dparr[rowidx - 1][colidx]
                    else:
                        dparr[rowidx][colidx] = dparr[rowidx - 1][colidx] + dparr[rowidx][colidx - coin]
        # print("dparr = ", dparr)
        return dparr[-1][-1]