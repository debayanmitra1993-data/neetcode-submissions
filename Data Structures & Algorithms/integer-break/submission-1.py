import math 

class Solution:
    def integerBreak(self, n: int) -> int:
        dparr = [1]*(n + 1)
        dparr[0] = 0

        for num in range(2, len(dparr)):

            startsubnum = num - 1
            endsubnum = int(math.ceil(num/2))
            maxprod = 1
            for subnum in range(startsubnum, endsubnum - 1, -1):
                prod = max(
                    dparr[subnum]*dparr[num - subnum],
                    dparr[subnum]*(num - subnum),
                    subnum * (num - subnum),
                    subnum * dparr[num - subnum],
                )
                if prod > maxprod:
                    maxprod = prod
            dparr[num] = maxprod

        return dparr[-1]