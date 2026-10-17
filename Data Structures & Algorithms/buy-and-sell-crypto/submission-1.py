class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices_left = [0]*len(prices)
        min_prices_left[0] = prices[0]
        for idx in range(1, len(prices)):
            min_prices_left[idx] = min(prices[idx], min_prices_left[idx - 1])
        
        max_prices_right = [0]*len(prices)
        max_prices_right[-1] = prices[-1]
        for idx in range(len(prices) -2, -1, -1):
            max_prices_right[idx] = max(prices[idx], max_prices_right[idx + 1])
        
        maxprofit = 0
        for idx in range(len(prices) - 1):
            profit = max_prices_right[idx + 1] - min_prices_left[idx]
            if profit > maxprofit:
                maxprofit = profit
        
        return maxprofit
        

        