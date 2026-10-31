class Solution:
    def numDecodings(self, s: str) -> int:
        dparr = [0]*(len(s) + 1)
        dparr[-1] = 1
        if int(s[-1]) >= 1 and int(s[-1]) <= 9:
            dparr[-2] = 1

        for idx in range(len(dparr) - 3, -1, -1):
            char = s[idx]
            if char == "0":
                dparr[idx] = 0
                continue 
            
            cntval = 0
            if int(char) >= 1 and int(char) <= 9:
                cntval += dparr[idx + 1]
            if int(s[idx : idx + 2]) >= 1 and int(s[idx : idx + 2]) <= 26:
                cntval += dparr[idx + 2]
            
            dparr[idx] = cntval
        return dparr[0]