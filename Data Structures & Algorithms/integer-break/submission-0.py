class Solution:
    def integerBreak(self, n: int) -> int:
        dparr = [1]*(n + 1)

        for num in range(3, len(dparr)):
            dparr[num] = float("-inf")
            for currnum in range(1, num):
                dparr[num] = max(
                    dparr[num],
                    currnum * (num - currnum), 
                    currnum * dparr[num - currnum]
                )
        return dparr[-1]
            



        