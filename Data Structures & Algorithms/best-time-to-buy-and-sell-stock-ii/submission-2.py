class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dparr = [0]*len(prices)
        dparr[-1] = 0

        for idx in range(len(prices) -2, -1, -1):
            dparr[idx] = dparr[idx + 1]
            maxval = float("-inf")
            for jdx in range(idx + 1, len(prices)):
                if prices[jdx] >= prices[idx]:
                    profit = prices[jdx] - prices[idx] + dparr[jdx]
                    if profit > maxval:
                        maxval = profit
            if maxval > dparr[idx]:
                dparr[idx] = maxval
        return dparr[0]