class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxarr = [0]*len(prices)
        maxarr[-1] = prices[-1]

        for idx in range(len(prices) - 2, -1, -1):
            maxarr[idx] = max(
                maxarr[idx + 1], 
                prices[idx]
            )
        
        maxp = 0
        for idx in range(len(prices) - 1):
            profit = maxarr[idx + 1] - prices[idx]
            if profit > maxp:
                maxp = profit
        return maxp