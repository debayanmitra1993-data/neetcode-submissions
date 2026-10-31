import math 

class Solution:
    def numSquares(self, n: int) -> int:
        dparr = [0]*(n + 1)
        dparr[1] = 1

        for num in range(2, len(dparr)):
            # check if num is perfect square -> then '1'
            sqrt_num = math.sqrt(num)
            if sqrt_num == math.ceil(sqrt_num) and sqrt_num == math.floor(sqrt_num):
                dparr[num] = 1
                continue 

            startnum = num - 1
            endnum = int(math.ceil(num/2))
            minval = float("inf")
            for subnum in range(startnum, endnum - 1, -1):
                if dparr[subnum] + dparr[num - subnum] < minval:
                    minval = dparr[subnum] + dparr[num - subnum]
            dparr[num] = minval
        
        return dparr[-1]
            


                





        