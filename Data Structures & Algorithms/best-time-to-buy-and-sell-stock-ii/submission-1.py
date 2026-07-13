class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dparr = [0]*len(prices)

        for idx in range(len(prices) - 2, -1, -1):
            maxprofit = 0
            for jdx in range(idx + 1, len(prices)):
                if prices[jdx] > prices[idx]:
                    maxprofit = max(
                        maxprofit, 
                        prices[jdx] - prices[idx] + dparr[jdx]
                    )
            dparr[idx] = max(maxprofit, dparr[idx + 1])
            # print("dparr = ", dparr)
        return dparr[0]

        