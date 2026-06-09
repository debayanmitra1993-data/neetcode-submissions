class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        if len(coins) == 1:
            if amount % coins[0] == 0:
                return amount // coins[0] 
            else:
                return -1 


        coins.sort()

        dp_arr = [float("inf")]*(amount + 1)
        dp_arr[0] = 0

        for idx in range(1, len(dp_arr)):
            curr_amount = idx

            min_coins = float("inf")
            for coin in coins:
                if coin <= curr_amount:
                    min_coins = min(min_coins, 1 + dp_arr[curr_amount - coin])
            
            if min_coins != float("inf"):
                dp_arr[idx] = min_coins
        
        print("dp_arr = ", dp_arr)
        return dp_arr[-1] if dp_arr[-1] != float("inf") else -1
         