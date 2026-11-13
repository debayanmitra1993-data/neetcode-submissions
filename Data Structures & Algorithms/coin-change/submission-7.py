class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dparr = [float("inf")]*(1 + amount)
        dparr[0] = 0
        coins.sort()

        for targetamt in range(coins[0], len(dparr)):

            for coin in coins:
                minways = dparr[targetamt]
                if coin <= targetamt:
                    if dparr[targetamt - coin] + 1 < minways:
                        minways = dparr[targetamt - coin] + 1
                dparr[targetamt] = minways

        return dparr[-1] if dparr[-1] != float("inf") else -1