class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minarray = [0]*len(prices)
        minarray[0] = prices[0]
        for idx in range(1, len(prices)):
            minarray[idx] = min(prices[idx], minarray[idx - 1])
        
        maxarray = [0]*len(prices)
        maxarray[-1] = prices[-1]
        for idx in range(len(prices) - 2, -1, -1):
            maxarray[idx] = max(maxarray[idx + 1], prices[idx])

        maxprofit = 0
        for idx in range(len(prices)):
            maxprofit = max(maxprofit, maxarray[idx] - minarray[idx])
        return maxprofit 
        

        