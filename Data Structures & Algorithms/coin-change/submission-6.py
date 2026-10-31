class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dparr = [float("inf")]*(1 + amount)
        dparr[0] = 0

        for idx in range(1, len(dparr)):
            target = idx
            for coin in coins:
                if coin <= target:
                    dparr[idx] = min(dparr[idx], 1 + dparr[target - coin])
        
        if dparr[-1] == float("inf"):
            return -1
        return dparr[-1]